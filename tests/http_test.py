from datetime import datetime
import unittest
from pytils.http import Filter

class FilterTest(unittest.TestCase):

    def test_value_parse_int(self):
        val = Filter.value_parse('12', ignore_type=False)
        self.assertEqual(val, 12)

    def test_value_parse_int_ignore_type(self):
        val = Filter.value_parse('11', ignore_type=True)
        self.assertEqual(val, '11')

    def test_value_parse_date(self):
        date = Filter.value_parse('2020-10-10', ignore_type=False)
        self.assertEqual(date, datetime.strptime('2020-10-10', '%Y-%m-%d'))

    def test_value_parse_date_ignore_type(self):
        val = Filter.value_parse('2020-01-23', ignore_type=True)
        self.assertEqual(val, '2020-01-23')

if __name__ == '__main__':
    unittest.main()