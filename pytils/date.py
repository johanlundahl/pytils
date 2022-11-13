from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime, timedelta
import calendar


class Period(ABC):

    def __init__(self, dt=datetime.now()):
        self._datetime = datetime(dt.year, dt.month, dt.day)

    @classmethod
    def now(cls):
        return cls(datetime.now())

    @classmethod
    def parse(cls, date_str):
        date = datetime.strptime(date_str, cls._date_pattern)
        return cls(date)

    @classmethod
    def of(cls, period):
        return cls(period._datetime)

    @property
    @abstractproperty
    def date_pattern(cls):
        pass

    @property
    def name(self):
        return str(self)

    @property
    @abstractmethod
    def number(self):
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

    @property
    def date_pattern(cls):
        return Date._date_pattern

    @property
    def number(self):
        return self._datetime.day

    def prev(self):
        yesterday = self._datetime - timedelta(days=1)
        return Date(yesterday)

    def next(self):
        tomorrow = self._datetime + timedelta(days=1)
        return Date(tomorrow)

    def range(self):
        end = self._datetime.replace(hour=23,
                                     minute=59,
                                     second=59,
                                     microsecond=999)
        return (self._datetime, end)

    def __sub__(self, obj):
        if isinstance(obj, int):
            new_date = self._datetime - timedelta(days=obj)
            return Date(new_date)


class Week(Period):
    _date_pattern = '%V %Y'

    @property
    def date_pattern(self):
        return '%V %Y'

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
        return Week.of(monday.prev())

    def next(self):
        monday, sunday = self.range()
        return Week.of(sunday.next())


class Month(Period):
    _date_pattern = '%B %Y'

    @property
    def date_pattern(self):
        return '%B %Y'

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
        return Month.of(first.prev())

    def next(self):
        first, last = self.range()
        return Month.of(last.next())

    def range(self):
        year = self._datetime.year
        month = self._datetime.month
        last_day = calendar.monthrange(year, month)[1]
        return (Date(datetime(year, month, 1)),
                Date(datetime(year, month, last_day)))


class Year(Period):

    @property
    def date_pattern(self):
        return '%Y'

    @property
    def number(self):
        return self._datetime.year

    def prev(self):
        first, last = self.range()
        return Year.of(first.prev())

    def next(self):
        first, last = self.range()
        return Year.of(last.next())

    def range(self):
        year = self._datetime.year
        return (Date(datetime(year, 1, 1)), Date(datetime(year, 12, 31)))
