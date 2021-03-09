import requests
import json
import operator
from datetime import datetime
import re
from flask import request
from functools import wraps

def post_json(url, obj):
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data = obj, headers = headers)
    return response.status_code, response.text

def get_json(url):
    try:
        headers = {'content-type': 'application/json'}
        response = requests.get(url, headers = headers)
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return 400, ''

def get(url):
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers = headers)
    return response.status_code, response.text


def validate_querystrings(method='GET', parameters=[]):
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            for querystring in request.args:
                querystring, operator = Filter.split_name_operator(querystring)
                if querystring not in parameters:
                    return 'The requested argument {} is not supported.'.format(querystring), 400
            return f(*args, **kwargs)
        return wrapped_f
    return wrap


operators = { 'lt':(operator.lt, '<'), 'le':(operator.le, '<='), 'eq':(operator.eq, '=='), 'ne':(operator.ne, '!='), 'ge':(operator.ge, '>='), 'gt':(operator.gt, '>') }

class Filter:
    def __init__(self, name, operator='eq', value=None):
        self.name = name
        self.operator, self.operator_str = operators[operator]
        self.value = value

    @classmethod
    def from_querystring(cls, str, ignore_type=False):
        match = re.compile("(.+)\[(.+)\]=(.+)").match(str)
        if match:
            name, operator, value = match.groups()
            return Filter(name, operator, cls.value_parse(value, ignore_type))
        match = re.compile('(.+)=(.+)').match(str)
        if match:
            name, value = match.groups()
            return Filter(name, value=cls.value_parse(value, ignore_type))

    @classmethod
    def from_arg(cls, name, value, ignore_type=False):
        name, operator = Filter.split_name_operator(name)
        if operator is not None:
            return Filter(name, operator, cls.value_parse(value, ignore_type))
        return Filter(name, value=cls.value_parse(value, ignore_type))

    @classmethod
    def split_name_operator(cls, full_name):
        match = re.compile("(.+)\[(.+)\]").match(full_name)
        if match:
            name, operator = match.groups()
            return name, operator
        return full_name, None

    @classmethod
    def args_matching(cls, args, name):
        return [a for a in args if a[:len(name)] == name]

    @property
    def evaluate(self):
        return lambda x: self.operator(x.__dict__[self.name], self.value)

    def to_json(self):
        result = {'field': self.name, 'op': self.operator_str, 'value': self.value}
        return result

    def __str__(self):
        return 'Filter(name={}, operator={}, value={})'.format(self.name, self.operator, self.value)

    def __repr__(self):
        return str(self)

    @classmethod
    def value_parse(cls, str, ignore_type):
        if ignore_type:
            return str
        date = cls.parse_datetime(str)
        if not ignore_type and date is not None:
            return date 
        else:
            return json.loads(str)

    @classmethod
    def parse_datetime(cls, str):
        formats = ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S']
        for format in formats:
            try:
                return datetime.strptime(str, format)
            except:
                continue
        return None

class Navigation:

    def __init__(self, title, prev, next):
        self.title = title
        self.prev = prev
        self.next = next