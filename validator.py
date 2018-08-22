class Rules:
    def __init__(self):
        self._rules = []
    
    def add_rule(self, func, result = None):
        self._rules.append(Rule(func, result))
    
    def validate(self, obj):
        try:
            return all(rule.func(obj) for rule in self._rules)
        except:
            return False

   	def evaluate(self, obj):
        for rule in self._rules:
		    if not rule.func(obj):
			    return rule.result
        return None
    
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
    pwd_rules = Rules()
    pwd_rules.add_rule(lambda s: any(x.isdigit() for x in s))
    pwd_rules.add_rule(lambda s: any(x.islower() for x in s))
    pwd_rules.add_rule(lambda s: any(x.isupper() for x in s))
    pwd_rules.add_rule(lambda s: len(s) >= 6)

    print(pwd_rules.validate("jOh12on"))

