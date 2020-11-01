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
	def next(self):
		tomorrow = self._datetime + timedelta(days=1)
		return Date(tomorrow)
	
	def __str__(self):
		return self._datetime.strftime(date_pattern)
