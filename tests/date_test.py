from datetime import datetime
import unittest
from pytils.date import Date, Month

class DateTest(unittest.TestCase):

    def test_date_parse(self):
        date = Date.parse('2020-11-01')
        self.assertTrue(isinstance(date, Date))

    def test_date_invalid_parse(self):
        with self.assertRaises(ValueError) as context:
            date = Date.parse('20-11-01')
            date = Date.parse('2020/11/01')

    def test_prev(self):
        date1 = Date(datetime(year=2020, month=9, day=21))
        self.assertEqual(date1.prev().datetime.day, 20)
        date2 = Date(datetime(year=2020, month=9, day=1))
        self.assertEqual(date2.prev().datetime.day, 31)
        
    def test_next(self):
        date1 = Date(datetime(year=2020, month=9, day=21))
        self.assertEqual(date1.next().datetime.day, 22)
        date2 = Date(datetime(year=2020, month=9, day=30))
        self.assertEqual(date2.next().datetime.day, 1)

    def test_month(self):
        date = Date(datetime(year=2021, month=2, day=7))
        self.assertTrue(isinstance(date.month(), Month))


if __name__ == '__main__':
    unittest.main() 