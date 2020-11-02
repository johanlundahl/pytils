from datetime import datetime
import unittest
from pytils.date import Date, Week

class WeekTest(unittest.TestCase):

    def test_week_prev(self):
        week = Week(2020, 45)
        self.assertEqual(week.prev.number, 44)

    def test_week_next(self):
        week = Week(2020, 45)
        self.assertTrue(isinstance(week.next, Week))
        self.assertEqual(week.next.number, 46)

    def test_first_day(self):
        week = Week(2020, 45)
        self.assertTrue(isinstance(week.first_day, Date))
        self.assertTrue(week.first_day.datetime.day, 2)

    def test_last_day(self):
        week = Week(2020, 45)
        self.assertTrue(isinstance(week.first_day, Date))
        self.assertTrue(week.last_day.datetime.day, 8)


if __name__ == '__main__':
    unittest.main() 