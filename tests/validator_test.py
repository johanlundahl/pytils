import unittest
from pytils.validator import Checker

class Search(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_validate_single_rule(self):
        rule = Checker()
        rule.add_rule(lambda s: any(x.isdigit() for x in s))
        self.assertTrue(rule.validate('123'))
        self.assertFalse(rule.validate('abc'))
    
    def test_validate_all_of_several_rules(self):
        rule = Checker().all()
        rule.add_rule(lambda s: any(x.isdigit() for x in s))
        rule.add_rule(lambda s: any(x.islower() for x in s))
        rule.add_rule(lambda s: any(x.isupper() for x in s))
        
        self.assertFalse(rule.validate('123'))
        self.assertFalse(rule.validate('1ab'))
        self.assertTrue(rule.validate('1Ab'))
    
    def test_validate_any_of_several_rules(self):
        rules = Checker()
        rules.add_rule(lambda s: any(x.isdigit() for x in s))
        rules.add_rule(lambda s: any(x.islower() for x in s))
        rules.add_rule(lambda s: any(x.isupper() for x in s))
        
        self.assertTrue(rules.any().validate('abc'))
        self.assertFalse(rules.any().validate('...'))
        self.assertTrue(rules.any().validate('1'))
        
    def test_evaluate_to_message(self):
        age = Checker().all()
        age.add_rule(lambda i: i >= 0, 'Must be positive int')
        age.add_rule(lambda i: i < 130, 'No one is that old')
        
        self.assertEqual(age.evaluate(-1), 'Must be positive int')
        self.assertEqual(age.evaluate(1), None)
        
        
    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
