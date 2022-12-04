from datetime import datetime
import unittest
from pytils.date import Date, Year


class YearTest(unittest.TestCase):

    def test_year(self):
        year = Year.now()
        self.assertTrue(isinstance(year, Year))

    def test_first_date(self):
        year = Year(datetime(year=2021, month=3, day=15))
        first_date, last_date = year.range()
        self.assertTrue(isinstance(first_date, Date))
        self.assertEqual(first_date._datetime.day, 1)
        self.assertEqual(first_date._datetime.month, 1)

    def test_last_date(self):
        year = Year(datetime(year=2021, month=3, day=15))
        first_date, last_date = year.range()
        self.assertTrue(isinstance(last_date, Date))
        self.assertEqual(last_date._datetime.day, 31)
        self.assertEqual(last_date._datetime.month, 12)

    def test_prev(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.prev(), Year))
        # self.assertEqual(year.prev().number, 2020)

    def test_next(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.next(), Year))
        # self.assertEqual(year.next().number, 2022)

    def test_year_number(self):
        year = Year(datetime(year=2022, month=12, day=4))
        self.assertEqual(year.number, 2022)

    def test_year_parse(self):
        date = Year.parse('2022')
        self.assertTrue(isinstance(date, Year))


if __name__ == '__main__':
    unittest.main()
