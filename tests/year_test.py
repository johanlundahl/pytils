from datetime import datetime
import unittest
from pytils.date import Date, Week, Month, Year


class YearTest(unittest.TestCase):

    def test_year(self):
        year = Year.current()
        self.assertTrue(isinstance(year, Year))

    def test_first_date(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.first_date(), Date))
        self.assertEqual(year.first_date().datetime.day, 1)
        self.assertEqual(year.first_date().datetime.month, 1)

    def test_last_date(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.last_date(), Date))
        self.assertEqual(year.last_date().datetime.day, 31)
        self.assertEqual(year.last_date().datetime.month, 12)

    def test_prev(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.prev(), Year))
        self.assertEqual(year.prev().number, 2020)

    def test_next(self):
        year = Year(datetime(year=2021, month=3, day=15))
        self.assertTrue(isinstance(year.next(), Year))
        self.assertEqual(year.next().number, 2022)


if __name__ == '__main__':
    unittest.main()