try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class AppointmentPreference(object):
	def __init__(self):
		"""Creates an instance of AppointmentPreference"""

		self.__show_job_sheet = None
		self.__when_duration_exceeds = None
		self.__when_appointment_completed = None
		self.__allow_booking_outside_service_availability = None
		self.__allow_booking_outside_businesshours = None
		self.__deal_record_configuration = None
		self.__key_modified = dict()

	def get_show_job_sheet(self):
		"""
		The method to get the show_job_sheet

		Returns:
			bool: A bool representing the show_job_sheet
		"""

		return self.__show_job_sheet

	def set_show_job_sheet(self, show_job_sheet):
		"""
		The method to set the value to show_job_sheet

		Parameters:
			show_job_sheet (bool) : A bool representing the show_job_sheet
		"""

		if show_job_sheet is not None and not isinstance(show_job_sheet, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_job_sheet EXPECTED TYPE: bool', None, None)
		
		self.__show_job_sheet = show_job_sheet
		self.__key_modified['show_job_sheet'] = 1

	def get_when_duration_exceeds(self):
		"""
		The method to get the when_duration_exceeds

		Returns:
			string: A string representing the when_duration_exceeds
		"""

		return self.__when_duration_exceeds

	def set_when_duration_exceeds(self, when_duration_exceeds):
		"""
		The method to set the value to when_duration_exceeds

		Parameters:
			when_duration_exceeds (string) : A string representing the when_duration_exceeds
		"""

		if when_duration_exceeds is not None and not isinstance(when_duration_exceeds, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: when_duration_exceeds EXPECTED TYPE: str', None, None)
		
		self.__when_duration_exceeds = when_duration_exceeds
		self.__key_modified['when_duration_exceeds'] = 1

	def get_when_appointment_completed(self):
		"""
		The method to get the when_appointment_completed

		Returns:
			Choice: An instance of Choice
		"""

		return self.__when_appointment_completed

	def set_when_appointment_completed(self, when_appointment_completed):
		"""
		The method to set the value to when_appointment_completed

		Parameters:
			when_appointment_completed (Choice) : An instance of Choice
		"""

		if when_appointment_completed is not None and not isinstance(when_appointment_completed, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: when_appointment_completed EXPECTED TYPE: Choice', None, None)
		
		self.__when_appointment_completed = when_appointment_completed
		self.__key_modified['when_appointment_completed'] = 1

	def get_allow_booking_outside_service_availability(self):
		"""
		The method to get the allow_booking_outside_service_availability

		Returns:
			bool: A bool representing the allow_booking_outside_service_availability
		"""

		return self.__allow_booking_outside_service_availability

	def set_allow_booking_outside_service_availability(self, allow_booking_outside_service_availability):
		"""
		The method to set the value to allow_booking_outside_service_availability

		Parameters:
			allow_booking_outside_service_availability (bool) : A bool representing the allow_booking_outside_service_availability
		"""

		if allow_booking_outside_service_availability is not None and not isinstance(allow_booking_outside_service_availability, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allow_booking_outside_service_availability EXPECTED TYPE: bool', None, None)
		
		self.__allow_booking_outside_service_availability = allow_booking_outside_service_availability
		self.__key_modified['allow_booking_outside_service_availability'] = 1

	def get_allow_booking_outside_businesshours(self):
		"""
		The method to get the allow_booking_outside_businesshours

		Returns:
			bool: A bool representing the allow_booking_outside_businesshours
		"""

		return self.__allow_booking_outside_businesshours

	def set_allow_booking_outside_businesshours(self, allow_booking_outside_businesshours):
		"""
		The method to set the value to allow_booking_outside_businesshours

		Parameters:
			allow_booking_outside_businesshours (bool) : A bool representing the allow_booking_outside_businesshours
		"""

		if allow_booking_outside_businesshours is not None and not isinstance(allow_booking_outside_businesshours, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allow_booking_outside_businesshours EXPECTED TYPE: bool', None, None)
		
		self.__allow_booking_outside_businesshours = allow_booking_outside_businesshours
		self.__key_modified['allow_booking_outside_businesshours'] = 1

	def get_deal_record_configuration(self):
		"""
		The method to get the deal_record_configuration

		Returns:
			DealRecordConfiguration: An instance of DealRecordConfiguration
		"""

		return self.__deal_record_configuration

	def set_deal_record_configuration(self, deal_record_configuration):
		"""
		The method to set the value to deal_record_configuration

		Parameters:
			deal_record_configuration (DealRecordConfiguration) : An instance of DealRecordConfiguration
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.appointment_preference.deal_record_configuration import DealRecordConfiguration
		except Exception:
			from .deal_record_configuration import DealRecordConfiguration

		if deal_record_configuration is not None and not isinstance(deal_record_configuration, DealRecordConfiguration):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_record_configuration EXPECTED TYPE: DealRecordConfiguration', None, None)
		
		self.__deal_record_configuration = deal_record_configuration
		self.__key_modified['deal_record_configuration'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
