try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AllowedFieldMap(object):
	def __init__(self):
		"""Creates an instance of AllowedFieldMap"""

		self.__output_data_field_mapping = None
		self.__input_data_field_mapping = None
		self.__key_modified = dict()

	def get_output_data_field_mapping(self):
		"""
		The method to get the output_data_field_mapping

		Returns:
			list: An instance of list
		"""

		return self.__output_data_field_mapping

	def set_output_data_field_mapping(self, output_data_field_mapping):
		"""
		The method to set the value to output_data_field_mapping

		Parameters:
			output_data_field_mapping (list) : An instance of list
		"""

		if output_data_field_mapping is not None and not isinstance(output_data_field_mapping, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_data_field_mapping EXPECTED TYPE: list', None, None)
		
		self.__output_data_field_mapping = output_data_field_mapping
		self.__key_modified['output_data_field_mapping'] = 1

	def get_input_data_field_mapping(self):
		"""
		The method to get the input_data_field_mapping

		Returns:
			list: An instance of list
		"""

		return self.__input_data_field_mapping

	def set_input_data_field_mapping(self, input_data_field_mapping):
		"""
		The method to set the value to input_data_field_mapping

		Parameters:
			input_data_field_mapping (list) : An instance of list
		"""

		if input_data_field_mapping is not None and not isinstance(input_data_field_mapping, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: input_data_field_mapping EXPECTED TYPE: list', None, None)
		
		self.__input_data_field_mapping = input_data_field_mapping
		self.__key_modified['input_data_field_mapping'] = 1

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
