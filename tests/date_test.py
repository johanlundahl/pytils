from datetime import datetime
import unittest
from pytils.date import Date, Month

class DateTest(unittest.TestCase):

    def test_constructor(self):
        date = Date(datetime.now())
        self.assertEqual(date._datetime.hour, 0)
        self.assertEqual(date._datetime.minute, 0)
        self.assertEqual(date._datetime.second, 0)

    def test_date_parse(self):
        date = Date.parse('2020-11-01')
        self.assertTrue(isinstance(date, Date))

    def test_date_invalid_parse(self):
        with self.assertRaises(ValueError) as context:
            date = Date.parse('20-11-01')
            date = Date.parse('2020/11/01')

    def test_prev(self):
        date1 = Date(datetime(year=2020, month=9, day=21))
        self.assertEqual(date1.prev()._datetime.day, 20)
        date2 = Date(datetime(year=2020, month=9, day=1))
        self.assertEqual(date2.prev()._datetime.day, 31)
        
    def test_next(self):
        date1 = Date(datetime(year=2020, month=9, day=21))
        self.assertEqual(date1.next()._datetime.day, 22)
        date2 = Date(datetime(year=2020, month=9, day=30))
        self.assertEqual(date2.next()._datetime.day, 1)

    def test_month(self):
        date = Date(datetime(year=2021, month=2, day=7))
        self.assertTrue(isinstance(Month.of(date), Month))

    def test_parse_week_from_date(self):
        week = Date.parse('2021-03-17')
        self.assertTrue(isinstance(week, Date))


if __name__ == '__main__':
    unittest.main() 