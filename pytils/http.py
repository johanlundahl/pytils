import requests
import json

def post_json(url, obj):
	headers = {'content-type': 'application/json'}
	response = requests.post(url, data = obj, headers = headers)
	return response.status_code, response.text

def get_json(url):
	headers = {'content-type': 'application/json'}
    response = requests.get(url, headers = headers)
    return response.status_code, response.json()
