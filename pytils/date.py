from datetime import datetime, timedelta
import calendar

date_pattern = '%Y-%m-%d'


class Date:

    def __init__(self, dt):
        self._datetime = dt

    @classmethod
    def parse(cls, date_str):
        date = datetime.strptime(date_str, date_pattern)
        return Date(date)

    @classmethod
    def today(cls):
        return Date(datetime.now())

    @property
    def datetime(self):
        return self._datetime
        
    def prev(self):
        yesterday = self._datetime - timedelta(days=1)
        return Date(yesterday)
    
    def next(self):
        tomorrow = self._datetime + timedelta(days=1)
        return Date(tomorrow)

    def week(self):
        return Week(self._datetime)
    
    def month(self):
        return Month(self._datetime)

    def year(self):
        return Year(self._datetime)
    
    def __str__(self):
        return self._datetime.strftime(date_pattern)


class Week:

    def __init__(self, a_datetime):
        self._a_datetime = a_datetime

    @classmethod
    def from_date(cls, date):
        return Week(date.datetime)

    @classmethod
    def current(cls):
        return Week(datetime.now())

    @property
    def year(self):
        return self._a_datetime.year
    
    @property
    def number(self):
        return self._a_datetime.isocalendar()[1]

    def monday(self):
        weekday = self._a_datetime.weekday()
        monday = self._a_datetime - timedelta(days=weekday)
        return Date(monday)
    
    def sunday(self):
        weekday = self._a_datetime.weekday()
        sunday = self._a_datetime + timedelta(days=(7-weekday))
        return Date(sunday)
        
    def prev(self):
        return self.monday().prev().week()
    
    def next(self):
        return self.sunday().next().week()
    
    def __str__(self):
        return 'Week {}, {}'.format(self.number, self.year)

class Month:

    def __init__(self, a_datetime):
        self._datetime = a_datetime

    @classmethod
    def current(cls):
        return Month(datetime.now())

    @property
    def number(self):
        return self._datetime.month
        
    @property
    def days(self):
        year = self._datetime.year
        month = self._datetime.month
        return calendar.monthrange(year, month)[1]  

    def prev(self):
        return self.first_date().prev().month()
    
    def next(self):
        return self.last_date().next().month()
        
    def first_date(self):
        year = self._datetime.year
        month = self._datetime.month
        return Date(datetime(year, month, 1))

    def last_date(self):
        year = self._datetime.year
        month = self._datetime.month
        day = calendar.monthrange(year, month)[1]
        return Date(datetime(year, month, day))

    def range(self):
        return (self.first_date(), self.last_date())

    def __str__(self):
        return self._datetime.strftime('%B %Y')


class Year:
    
    def __init__(self, a_datetime):
        self._datetime = a_datetime

    @classmethod
    def current(cls):
        return Year(datetime.now())

    @property
    def number(self):
        return self._datetime.year
    
    def prev(self):
        return self.first_date().prev().year()

    def next(self):
        return self.last_date().next().year()

    def first_date(self):
        year = self._datetime.year
        return Date(datetime(year, 1, 1))

    def last_date(self):
        year = self._datetime.year
        return Date(datetime(year, 12, 31))

    def range(self):
        return (self.first_date(), self.last_date())

    def __str__(self):
        return self._datetime.strftime('%Y')
