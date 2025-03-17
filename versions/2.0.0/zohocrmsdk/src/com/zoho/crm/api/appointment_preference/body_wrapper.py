try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__appointment_preferences = None
		self.__key_modified = dict()

	def get_appointment_preferences(self):
		"""
		The method to get the appointment_preferences

		Returns:
			AppointmentPreference: An instance of AppointmentPreference
		"""

		return self.__appointment_preferences

	def set_appointment_preferences(self, appointment_preferences):
		"""
		The method to set the value to appointment_preferences

		Parameters:
			appointment_preferences (AppointmentPreference) : An instance of AppointmentPreference
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.appointment_preference.appointment_preference import AppointmentPreference
		except Exception:
			from .appointment_preference import AppointmentPreference

		if appointment_preferences is not None and not isinstance(appointment_preferences, AppointmentPreference):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: appointment_preferences EXPECTED TYPE: AppointmentPreference', None, None)
		
		self.__appointment_preferences = appointment_preferences
		self.__key_modified['appointment_preferences'] = 1

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
