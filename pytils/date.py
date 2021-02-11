from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import calendar


class Period(ABC):
    
    def __init__(self, dt):
        self._datetime = dt.replace(hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def current(cls):
        return cls(datetime.now())

    @classmethod
    def create(cls, date):
        return cls(date._datetime)

    @property
    @abstractmethod
    def date_pattern(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def range(self):
        pass
        
    def __str__(self):
        return self._datetime.strftime(self.date_pattern)


class Date(Period):
    
    _date_pattern = '%Y-%m-%d'

    @classmethod
    def parse(cls, date_str):
        date = datetime.strptime(date_str, cls._date_pattern)
        return Date(date)

    @property
    def date_pattern(self):
        return Date._date_pattern

    @property
    def name(self):
        return str(self)
    
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
    
    def range(self):
        end = self._datetime.replace(hour=23, minute=59, second=59, microsecond=999)
        return (self._datetime, end)


class Week(Period):

    @property
    def date_pattern(self):
        return '%V %Y'

    @property    
    def name(self):
        return 'Week {}, {}'.format(self.number, self.year)

    @property
    def year(self):
        return self._datetime.year
    
    @property
    def number(self):
        return self._datetime.isocalendar()[1]

    def range(self):
        weekday = self._datetime.weekday()
        monday = self._datetime - timedelta(days=weekday)
        sunday = self._datetime + timedelta(days=(7-weekday))
        return (Date(monday), Date(sunday))
        
    def prev(self):
        monday, sunday = self.range()
        return Week.create(monday.prev())
    
    def next(self):
        monday, sunday = self.range()
        return Week.create(sunday.next())
    

class Month(Period):

    @property
    def date_pattern(self):
        return '%B %Y'

    @property
    def name(self):
        return str(self)

    @property
    def number(self):
        return self._datetime.month
        
    @property
    def days(self):
        year = self._datetime.year
        month = self._datetime.month
        return calendar.monthrange(year, month)[1]  

    def prev(self):
        first, last = self.range()
        return Month.create(first.prev())
    
    def next(self):
        first, last = self.range()
        return Month.create(last.next())
        
    def range(self):
        year = self._datetime.year
        month = self._datetime.month
        last_day = calendar.monthrange(year, month)[1]        
        return (Date(datetime(year, month, 1)), Date(datetime(year, month, last_day)))


class Year(Period):
    
    @property
    def date_pattern(self):
        return '%Y'

    @property    
    def name(self):
        return str(self)
    
    def prev(self):
        first, last = self.range()
        return Year.create(first.prev())

    def next(self):
        first, last = self.range()
        return Year.create(last.next())
        
    def range(self):
        year = self._datetime.year
        return (Date(datetime(year, 1, 1)), Date(datetime(year, 12, 31)))

