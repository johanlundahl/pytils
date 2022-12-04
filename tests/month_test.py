from datetime import datetime
import unittest
from pytils.date import Date, Month


class MonthTest(unittest.TestCase):

    def test_month(self):
        month = Month(datetime(year=2021, month=2, day=7))
        self.assertTrue(isinstance(month, Month))
        self.assertEqual(month.number, 2)
        self.assertEqual(month.days, 28)

    def test_next(self):
        month = Month(datetime(year=2021, month=2, day=1))
        self.assertEqual(month.next().number, 3)

    def test_prev(self):
        month = Month(datetime(year=2021, month=1, day=10))
        self.assertEqual(month.prev().number, 12)

    def test_first_date(self):
        month = Month(datetime(year=2021, month=3, day=15))
        first_date, last_date = month.range()
        self.assertTrue(isinstance(first_date, Date))
        self.assertEqual(first_date._datetime.day, 1)

    def test_last_date(self):
        march = Month(datetime(year=2021, month=3, day=15))
        first_date, last_date = march.range()
        self.assertTrue(isinstance(last_date, Date))
        self.assertEqual(last_date._datetime.day, 31)
        february = Month(datetime(year=2021, month=2, day=15))
        first_date, last_date = february.range()
        self.assertEqual(last_date._datetime.day, 28)

    def test_month_parse(self):
        month = Month.parse('December 2022')
        self.assertTrue(isinstance(month, Month))


if __name__ == '__main__':
    unittest.main()
