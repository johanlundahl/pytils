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

	def first_in_month(self):
		year = self._datetime.year
		month = self._datetime.month
		return Date(datetime(year, month, 1))
	
	def last_in_month(self):
		year = self._datetime.year
		month = self._datetime.month
		day = calendar.monthrange(year, month)[1]
		return Date(datetime(year, month, day))

	@property
	def datetime(self):
		return self._datetime
		
	@property
	def prev(self):
		yesterday = self._datetime - timedelta(days=1)
		return Date(yesterday)

	@property
	def week(self):
		year = self._datetime.year
		week = self._datetime.isocalendar()[1]
		return Week(year, week)
	
	@property
	def next(self):
		tomorrow = self._datetime + timedelta(days=1)
		return Date(tomorrow)
	
	def __str__(self):
		return self._datetime.strftime(date_pattern)

class Week:

	def __init__(self, year, number):
		self._year = year
		self._number = number

	@property
	def first_day(self):
		week_str = '{}-{}-1'.format(self._year, self._number)
		monday = datetime.strptime(week_str, "%Y-%W-%w") 
		return Date(monday)
	
	@property
	def year(self):
		return self._year
	
	@property
	def number(self):
		return self._number
	

	@property
	def last_day(self):
		sunday = self.first_day.datetime + timedelta(days=7)
		return Date(sunday)
	
	@property
	def prev(self):
		return self.first_day.prev.week
	
	@property
	def next(self):
		return self.last_day.next.week
	
	def __str__(self):
		return 'Week {}, {}'.format(self._number, self._year)