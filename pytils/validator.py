from pytils import method_chaining


class Checker:
    def __init__(self):
        self._rules = []
        self._type = lambda x: all(x)

    @method_chaining.chainable
    def any(self):
        self._type = lambda x: any(x)

    @method_chaining.chainable
    def all(self):
        self._type = lambda x: all(x)

    def add_rule(self, func, result=None):
        self._rules.append(Rule(func, result))

    def validate(self, obj):
        try:
            return self._type(rule.func(obj) for rule in self._rules)
        except:
            return False

    def evaluate(self, obj):
        for rule in self._rules:
            if not rule.func(obj):
                return rule.result(obj) if callable(rule.result) else rule.result
        return None

    def transform(self, obj):
        for rule in self._rules:
            if rule.func(obj):
                return rule.result(obj)


class Rule:
    def __init__(self, func, result):
        self._func = func
        self._result = result

    @property
    def result(self):
        return self._result

    @property
    def func(self):
        return self._func


if __name__ == '__main__':
    # Example on how to use Rules to validate passwords
    pwd_rules = Checker()
    pwd_rules.add_rule(lambda s: any(x.isdigit() for x in s))
    pwd_rules.add_rule(lambda s: any(x.islower() for x in s))
    pwd_rules.add_rule(lambda s: any(x.isupper() for x in s))
    pwd_rules.add_rule(lambda s: len(s) >= 6)

    print(pwd_rules.validate("jOh12on"))

    nbr_plate = Checker()
    nbr_plate.add_rule(lambda r: len(r) == 6, 'Must be six tokens long')
    nbr_plate.add_rule(lambda r: all(x.isdigit() for x in r[-3:]), 'Must end with three digits')
    nbr_plate.add_rule(lambda r: all(x.isalpha() for x in r[:3]), 'Must start with three letters')

    if not nbr_plate.validate('ABC 123'):
        print(nbr_plate.evaluate('ABC 123'))
