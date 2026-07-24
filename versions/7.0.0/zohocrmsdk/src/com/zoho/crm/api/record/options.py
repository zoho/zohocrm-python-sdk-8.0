try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Options(object):
	def __init__(self):
		"""Creates an instance of Options"""
		pass



	class RecordLockLockSourceS(object):
		
		@classmethod
		def manual(cls):
			return Choice('Manual')

		@classmethod
		def automatic(cls):
			return Choice('Automatic')




	class UsersTimeFormat(object):
		
		@classmethod
		def hhmm(cls):
			return Choice('HH:mm')

		@classmethod
		def hhmma(cls):
			return Choice('hh:mm a')




	class UsersDateFormat(object):
		
		@classmethod
		def mmmdyyyy(cls):
			return Choice('MMM d, yyyy')




	class UsersDecimalSeparator(object):
		
		@classmethod
		def comma(cls):
			return Choice('Comma')

		@classmethod
		def period(cls):
			return Choice('Period')




	class UsersNumberSeparator(object):
		
		@classmethod
		def space(cls):
			return Choice('Space')




	class UsersNameFormatS(object):
		
		@classmethod
		def salutationfirstnamelastname(cls):
			return Choice('Salutation,First Name,Last Name')

		@classmethod
		def saluationlastnamefirstname(cls):
			return Choice('Saluation,Last Name,First Name')

		@classmethod
		def firstnamelastnamesaluation(cls):
			return Choice('First Name,Last Name,Saluation')


