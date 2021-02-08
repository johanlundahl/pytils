from datetime import datetime
import unittest
from pytils.date import Date, Week


class WeekTest(unittest.TestCase):

    def test_week_prev(self):
        week = Week(datetime(year=2020, month=11, day=5))
        self.assertEqual(week.prev().number, 44)

    def test_week_next(self):
        week = Week(datetime(year=2020, month=11, day=4))
        self.assertTrue(isinstance(week.next(), Week))
        self.assertEqual(week.next().number, 46)

    def test_week_next_at_new_year(self):
        week = Week(datetime(year=2020, month=12, day=31))
        self.assertTrue(isinstance(week.next(), Week))
        self.assertEqual(week.year, 2020)
        self.assertEqual(week.number, 53)
        self.assertEqual(week.next().year, 2021)
        self.assertEqual(week.next().number, 1)

    def test_monday(self):
        week = Week(datetime(year=2020, month=11, day=4))
        self.assertTrue(isinstance(week.monday(), Date))
        self.assertTrue(week.monday().datetime.day, 2)
        self.assertEqual('2020-11-02', str(week.monday()))        

    def test_sunday(self):
        week = Week(datetime(year=2020, month=11, day=6))
        self.assertTrue(isinstance(week.sunday(), Date))
        self.assertTrue(week.sunday().datetime.day, 8)
        self.assertEqual(45, week.number) 

    def test_last_week_of_year(self):
        week = Week(datetime(year=2020, month=12, day=30))
        self.assertEqual('2020-12-28', str(week.monday()))
        self.assertEqual(53, week.number)        

    def test_first_week_of_year(self):
        week = Week(datetime(year=2021, month=1, day=8))
        self.assertEqual('2021-01-04', str(week.monday()))
        self.assertEqual(1, week.number)


if __name__ == '__main__':
    unittest.main() 