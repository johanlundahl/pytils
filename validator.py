class Rules:
    def __init__(self):
        self._rules = []
    
    def add_rule(self, func, feedback = None):
        self._rules.append(Rule(func, feedback))
    
    def validate(self, obj):
        try:
            return all(rule.func(obj) for rule in self._rules)
        except:
            return False

class Rule:
    def __init__(self, func, feedback):
        self._func = func
        self._feedback = feedback
    
    @property
    def feedback(self):
        return self._feedback
    
    @property
    def func(self):
        return self._func
    
if __name__ == '__main__':    
    # Example on how to use Rules to validate passwords
    rules = Rules()
    rules.add_rule(lambda s: any(x.isdigit() for x in s))
    rules.add_rule(lambda s: any(x.islower() for x in s))
    rules.add_rule(lambda s: any(x.isupper() for x in s))
    rules.add_rule(lambda s: len(s) >= 6)

    print(rules.validate("jOh12on"))

