try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Preference(object):
	def __init__(self):
		"""Creates an instance of Preference"""

		self.__consent_modules = None
		self.__restrict_tpt_fields = None
		self.__exclude_api_zoho = None
		self.__awaiting_period = None
		self.__consent_mail_send = None
		self.__exclude_export_fields = None
		self.__limit_actions = None
		self.__exclude_export = None
		self.__restrict_zoho_integ = None
		self.__exclude_api_zoho_fields = None
		self.__duration_timing = None
		self.__data_processing_duration = None
		self.__restrict_tpt_services = None
		self.__exclude_api_tpt_fields = None
		self.__restrict_zoho_integ_services = None
		self.__privacy_setting_status = None
		self.__double_opt_in = None
		self.__restrict_zoho_integ_fields = None
		self.__exclude_api_tpt = None
		self.__block_list = None
		self.__restrict_tpt = None
		self.__actions_while_awaiting = None
		self.__key_modified = dict()

	def get_consent_modules(self):
		"""
		The method to get the consent_modules

		Returns:
			string: A string representing the consent_modules
		"""

		return self.__consent_modules

	def set_consent_modules(self, consent_modules):
		"""
		The method to set the value to consent_modules

		Parameters:
			consent_modules (string) : A string representing the consent_modules
		"""

		if consent_modules is not None and not isinstance(consent_modules, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_modules EXPECTED TYPE: str', None, None)
		
		self.__consent_modules = consent_modules
		self.__key_modified['consent_modules'] = 1

	def get_restrict_tpt_fields(self):
		"""
		The method to get the restrict_tpt_fields

		Returns:
			string: A string representing the restrict_tpt_fields
		"""

		return self.__restrict_tpt_fields

	def set_restrict_tpt_fields(self, restrict_tpt_fields):
		"""
		The method to set the value to restrict_tpt_fields

		Parameters:
			restrict_tpt_fields (string) : A string representing the restrict_tpt_fields
		"""

		if restrict_tpt_fields is not None and not isinstance(restrict_tpt_fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_tpt_fields EXPECTED TYPE: str', None, None)
		
		self.__restrict_tpt_fields = restrict_tpt_fields
		self.__key_modified['restrict_tpt_fields'] = 1

	def get_exclude_api_zoho(self):
		"""
		The method to get the exclude_api_zoho

		Returns:
			string: A string representing the exclude_api_zoho
		"""

		return self.__exclude_api_zoho

	def set_exclude_api_zoho(self, exclude_api_zoho):
		"""
		The method to set the value to exclude_api_zoho

		Parameters:
			exclude_api_zoho (string) : A string representing the exclude_api_zoho
		"""

		if exclude_api_zoho is not None and not isinstance(exclude_api_zoho, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_api_zoho EXPECTED TYPE: str', None, None)
		
		self.__exclude_api_zoho = exclude_api_zoho
		self.__key_modified['exclude_api_zoho'] = 1

	def get_awaiting_period(self):
		"""
		The method to get the awaiting_period

		Returns:
			string: A string representing the awaiting_period
		"""

		return self.__awaiting_period

	def set_awaiting_period(self, awaiting_period):
		"""
		The method to set the value to awaiting_period

		Parameters:
			awaiting_period (string) : A string representing the awaiting_period
		"""

		if awaiting_period is not None and not isinstance(awaiting_period, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: awaiting_period EXPECTED TYPE: str', None, None)
		
		self.__awaiting_period = awaiting_period
		self.__key_modified['awaiting_period'] = 1

	def get_consent_mail_send(self):
		"""
		The method to get the consent_mail_send

		Returns:
			string: A string representing the consent_mail_send
		"""

		return self.__consent_mail_send

	def set_consent_mail_send(self, consent_mail_send):
		"""
		The method to set the value to consent_mail_send

		Parameters:
			consent_mail_send (string) : A string representing the consent_mail_send
		"""

		if consent_mail_send is not None and not isinstance(consent_mail_send, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_mail_send EXPECTED TYPE: str', None, None)
		
		self.__consent_mail_send = consent_mail_send
		self.__key_modified['consent_mail_send'] = 1

	def get_exclude_export_fields(self):
		"""
		The method to get the exclude_export_fields

		Returns:
			string: A string representing the exclude_export_fields
		"""

		return self.__exclude_export_fields

	def set_exclude_export_fields(self, exclude_export_fields):
		"""
		The method to set the value to exclude_export_fields

		Parameters:
			exclude_export_fields (string) : A string representing the exclude_export_fields
		"""

		if exclude_export_fields is not None and not isinstance(exclude_export_fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_export_fields EXPECTED TYPE: str', None, None)
		
		self.__exclude_export_fields = exclude_export_fields
		self.__key_modified['exclude_export_fields'] = 1

	def get_limit_actions(self):
		"""
		The method to get the limit_actions

		Returns:
			string: A string representing the limit_actions
		"""

		return self.__limit_actions

	def set_limit_actions(self, limit_actions):
		"""
		The method to set the value to limit_actions

		Parameters:
			limit_actions (string) : A string representing the limit_actions
		"""

		if limit_actions is not None and not isinstance(limit_actions, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: limit_actions EXPECTED TYPE: str', None, None)
		
		self.__limit_actions = limit_actions
		self.__key_modified['limit_actions'] = 1

	def get_exclude_export(self):
		"""
		The method to get the exclude_export

		Returns:
			string: A string representing the exclude_export
		"""

		return self.__exclude_export

	def set_exclude_export(self, exclude_export):
		"""
		The method to set the value to exclude_export

		Parameters:
			exclude_export (string) : A string representing the exclude_export
		"""

		if exclude_export is not None and not isinstance(exclude_export, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_export EXPECTED TYPE: str', None, None)
		
		self.__exclude_export = exclude_export
		self.__key_modified['exclude_export'] = 1

	def get_restrict_zoho_integ(self):
		"""
		The method to get the restrict_zoho_integ

		Returns:
			string: A string representing the restrict_zoho_integ
		"""

		return self.__restrict_zoho_integ

	def set_restrict_zoho_integ(self, restrict_zoho_integ):
		"""
		The method to set the value to restrict_zoho_integ

		Parameters:
			restrict_zoho_integ (string) : A string representing the restrict_zoho_integ
		"""

		if restrict_zoho_integ is not None and not isinstance(restrict_zoho_integ, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_zoho_integ EXPECTED TYPE: str', None, None)
		
		self.__restrict_zoho_integ = restrict_zoho_integ
		self.__key_modified['restrict_zoho_integ'] = 1

	def get_exclude_api_zoho_fields(self):
		"""
		The method to get the exclude_api_zoho_fields

		Returns:
			string: A string representing the exclude_api_zoho_fields
		"""

		return self.__exclude_api_zoho_fields

	def set_exclude_api_zoho_fields(self, exclude_api_zoho_fields):
		"""
		The method to set the value to exclude_api_zoho_fields

		Parameters:
			exclude_api_zoho_fields (string) : A string representing the exclude_api_zoho_fields
		"""

		if exclude_api_zoho_fields is not None and not isinstance(exclude_api_zoho_fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_api_zoho_fields EXPECTED TYPE: str', None, None)
		
		self.__exclude_api_zoho_fields = exclude_api_zoho_fields
		self.__key_modified['exclude_api_zoho_fields'] = 1

	def get_duration_timing(self):
		"""
		The method to get the duration_timing

		Returns:
			string: A string representing the duration_timing
		"""

		return self.__duration_timing

	def set_duration_timing(self, duration_timing):
		"""
		The method to set the value to duration_timing

		Parameters:
			duration_timing (string) : A string representing the duration_timing
		"""

		if duration_timing is not None and not isinstance(duration_timing, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duration_timing EXPECTED TYPE: str', None, None)
		
		self.__duration_timing = duration_timing
		self.__key_modified['duration_timing'] = 1

	def get_data_processing_duration(self):
		"""
		The method to get the data_processing_duration

		Returns:
			string: A string representing the data_processing_duration
		"""

		return self.__data_processing_duration

	def set_data_processing_duration(self, data_processing_duration):
		"""
		The method to set the value to data_processing_duration

		Parameters:
			data_processing_duration (string) : A string representing the data_processing_duration
		"""

		if data_processing_duration is not None and not isinstance(data_processing_duration, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_processing_duration EXPECTED TYPE: str', None, None)
		
		self.__data_processing_duration = data_processing_duration
		self.__key_modified['data_processing_duration'] = 1

	def get_restrict_tpt_services(self):
		"""
		The method to get the restrict_tpt_services

		Returns:
			string: A string representing the restrict_tpt_services
		"""

		return self.__restrict_tpt_services

	def set_restrict_tpt_services(self, restrict_tpt_services):
		"""
		The method to set the value to restrict_tpt_services

		Parameters:
			restrict_tpt_services (string) : A string representing the restrict_tpt_services
		"""

		if restrict_tpt_services is not None and not isinstance(restrict_tpt_services, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_tpt_services EXPECTED TYPE: str', None, None)
		
		self.__restrict_tpt_services = restrict_tpt_services
		self.__key_modified['restrict_tpt_services'] = 1

	def get_exclude_api_tpt_fields(self):
		"""
		The method to get the exclude_api_tpt_fields

		Returns:
			string: A string representing the exclude_api_tpt_fields
		"""

		return self.__exclude_api_tpt_fields

	def set_exclude_api_tpt_fields(self, exclude_api_tpt_fields):
		"""
		The method to set the value to exclude_api_tpt_fields

		Parameters:
			exclude_api_tpt_fields (string) : A string representing the exclude_api_tpt_fields
		"""

		if exclude_api_tpt_fields is not None and not isinstance(exclude_api_tpt_fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_api_tpt_fields EXPECTED TYPE: str', None, None)
		
		self.__exclude_api_tpt_fields = exclude_api_tpt_fields
		self.__key_modified['exclude_api_tpt_fields'] = 1

	def get_restrict_zoho_integ_services(self):
		"""
		The method to get the restrict_zoho_integ_services

		Returns:
			string: A string representing the restrict_zoho_integ_services
		"""

		return self.__restrict_zoho_integ_services

	def set_restrict_zoho_integ_services(self, restrict_zoho_integ_services):
		"""
		The method to set the value to restrict_zoho_integ_services

		Parameters:
			restrict_zoho_integ_services (string) : A string representing the restrict_zoho_integ_services
		"""

		if restrict_zoho_integ_services is not None and not isinstance(restrict_zoho_integ_services, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_zoho_integ_services EXPECTED TYPE: str', None, None)
		
		self.__restrict_zoho_integ_services = restrict_zoho_integ_services
		self.__key_modified['restrict_zoho_integ_services'] = 1

	def get_privacy_setting_status(self):
		"""
		The method to get the privacy_setting_status

		Returns:
			string: A string representing the privacy_setting_status
		"""

		return self.__privacy_setting_status

	def set_privacy_setting_status(self, privacy_setting_status):
		"""
		The method to set the value to privacy_setting_status

		Parameters:
			privacy_setting_status (string) : A string representing the privacy_setting_status
		"""

		if privacy_setting_status is not None and not isinstance(privacy_setting_status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: privacy_setting_status EXPECTED TYPE: str', None, None)
		
		self.__privacy_setting_status = privacy_setting_status
		self.__key_modified['privacy_setting_status'] = 1

	def get_double_opt_in(self):
		"""
		The method to get the double_opt_in

		Returns:
			string: A string representing the double_opt_in
		"""

		return self.__double_opt_in

	def set_double_opt_in(self, double_opt_in):
		"""
		The method to set the value to double_opt_in

		Parameters:
			double_opt_in (string) : A string representing the double_opt_in
		"""

		if double_opt_in is not None and not isinstance(double_opt_in, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: double_opt_in EXPECTED TYPE: str', None, None)
		
		self.__double_opt_in = double_opt_in
		self.__key_modified['double_opt_in'] = 1

	def get_restrict_zoho_integ_fields(self):
		"""
		The method to get the restrict_zoho_integ_fields

		Returns:
			string: A string representing the restrict_zoho_integ_fields
		"""

		return self.__restrict_zoho_integ_fields

	def set_restrict_zoho_integ_fields(self, restrict_zoho_integ_fields):
		"""
		The method to set the value to restrict_zoho_integ_fields

		Parameters:
			restrict_zoho_integ_fields (string) : A string representing the restrict_zoho_integ_fields
		"""

		if restrict_zoho_integ_fields is not None and not isinstance(restrict_zoho_integ_fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_zoho_integ_fields EXPECTED TYPE: str', None, None)
		
		self.__restrict_zoho_integ_fields = restrict_zoho_integ_fields
		self.__key_modified['restrict_zoho_integ_fields'] = 1

	def get_exclude_api_tpt(self):
		"""
		The method to get the exclude_api_tpt

		Returns:
			string: A string representing the exclude_api_tpt
		"""

		return self.__exclude_api_tpt

	def set_exclude_api_tpt(self, exclude_api_tpt):
		"""
		The method to set the value to exclude_api_tpt

		Parameters:
			exclude_api_tpt (string) : A string representing the exclude_api_tpt
		"""

		if exclude_api_tpt is not None and not isinstance(exclude_api_tpt, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exclude_api_tpt EXPECTED TYPE: str', None, None)
		
		self.__exclude_api_tpt = exclude_api_tpt
		self.__key_modified['exclude_api_tpt'] = 1

	def get_block_list(self):
		"""
		The method to get the block_list

		Returns:
			string: A string representing the block_list
		"""

		return self.__block_list

	def set_block_list(self, block_list):
		"""
		The method to set the value to block_list

		Parameters:
			block_list (string) : A string representing the block_list
		"""

		if block_list is not None and not isinstance(block_list, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: block_list EXPECTED TYPE: str', None, None)
		
		self.__block_list = block_list
		self.__key_modified['block_list'] = 1

	def get_restrict_tpt(self):
		"""
		The method to get the restrict_tpt

		Returns:
			string: A string representing the restrict_tpt
		"""

		return self.__restrict_tpt

	def set_restrict_tpt(self, restrict_tpt):
		"""
		The method to set the value to restrict_tpt

		Parameters:
			restrict_tpt (string) : A string representing the restrict_tpt
		"""

		if restrict_tpt is not None and not isinstance(restrict_tpt, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_tpt EXPECTED TYPE: str', None, None)
		
		self.__restrict_tpt = restrict_tpt
		self.__key_modified['restrict_tpt'] = 1

	def get_actions_while_awaiting(self):
		"""
		The method to get the actions_while_awaiting

		Returns:
			string: A string representing the actions_while_awaiting
		"""

		return self.__actions_while_awaiting

	def set_actions_while_awaiting(self, actions_while_awaiting):
		"""
		The method to set the value to actions_while_awaiting

		Parameters:
			actions_while_awaiting (string) : A string representing the actions_while_awaiting
		"""

		if actions_while_awaiting is not None and not isinstance(actions_while_awaiting, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actions_while_awaiting EXPECTED TYPE: str', None, None)
		
		self.__actions_while_awaiting = actions_while_awaiting
		self.__key_modified['actions_while_awaiting'] = 1

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
