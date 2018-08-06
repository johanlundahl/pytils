class Rules:
    def __init__(self):
        self._rules = []
    
    def add_rule(self, func):
        self._rules.append(func)
    
    def validate(self, obj):
        try:
            return all(rule(obj) for rule in self._rules)
        except:
            return False
    

if __name__ == '__main__':    
    # Example on how to use Rules to validate passwords
    rules = Rules()
    rules.add_rule(lambda s: any(x.isdigit() for x in s))
    rules.add_rule(lambda s: any(x.islower() for x in s))
    rules.add_rule(lambda s: any(x.isupper() for x in s))
    rules.add_rule(lambda s: len(s) >= 6)

    print(rules.validate("jOh12on"))

