try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class PickListValue(object):
	def __init__(self):
		"""Creates an instance of PickListValue"""

		self.__colour_code = None
		self.__actual_value = None
		self.__type = None
		self.__id = None
		self.__sequence_number = None
		self.__display_value = None
		self.__reference_value = None
		self.__deal_category = None
		self.__probability = None
		self.__forecast_category = None
		self.__expected_data_type = None
		self.__sys_ref_name = None
		self.__forecast_type = None
		self.__maps = None
		self.__delete = None
		self.__show_value = None
		self.__global_picklist_value = None
		self.__key_modified = dict()

	def get_colour_code(self):
		"""
		The method to get the colour_code

		Returns:
			string: A string representing the colour_code
		"""

		return self.__colour_code

	def set_colour_code(self, colour_code):
		"""
		The method to set the value to colour_code

		Parameters:
			colour_code (string) : A string representing the colour_code
		"""

		if colour_code is not None and not isinstance(colour_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: colour_code EXPECTED TYPE: str', None, None)
		
		self.__colour_code = colour_code
		self.__key_modified['colour_code'] = 1

	def get_actual_value(self):
		"""
		The method to get the actual_value

		Returns:
			string: A string representing the actual_value
		"""

		return self.__actual_value

	def set_actual_value(self, actual_value):
		"""
		The method to set the value to actual_value

		Parameters:
			actual_value (string) : A string representing the actual_value
		"""

		if actual_value is not None and not isinstance(actual_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_value EXPECTED TYPE: str', None, None)
		
		self.__actual_value = actual_value
		self.__key_modified['actual_value'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_reference_value(self):
		"""
		The method to get the reference_value

		Returns:
			string: A string representing the reference_value
		"""

		return self.__reference_value

	def set_reference_value(self, reference_value):
		"""
		The method to set the value to reference_value

		Parameters:
			reference_value (string) : A string representing the reference_value
		"""

		if reference_value is not None and not isinstance(reference_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reference_value EXPECTED TYPE: str', None, None)
		
		self.__reference_value = reference_value
		self.__key_modified['reference_value'] = 1

	def get_deal_category(self):
		"""
		The method to get the deal_category

		Returns:
			string: A string representing the deal_category
		"""

		return self.__deal_category

	def set_deal_category(self, deal_category):
		"""
		The method to set the value to deal_category

		Parameters:
			deal_category (string) : A string representing the deal_category
		"""

		if deal_category is not None and not isinstance(deal_category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_category EXPECTED TYPE: str', None, None)
		
		self.__deal_category = deal_category
		self.__key_modified['deal_category'] = 1

	def get_probability(self):
		"""
		The method to get the probability

		Returns:
			int: An int representing the probability
		"""

		return self.__probability

	def set_probability(self, probability):
		"""
		The method to set the value to probability

		Parameters:
			probability (int) : An int representing the probability
		"""

		if probability is not None and not isinstance(probability, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: probability EXPECTED TYPE: int', None, None)
		
		self.__probability = probability
		self.__key_modified['probability'] = 1

	def get_forecast_category(self):
		"""
		The method to get the forecast_category

		Returns:
			ForecastCategory: An instance of ForecastCategory
		"""

		return self.__forecast_category

	def set_forecast_category(self, forecast_category):
		"""
		The method to set the value to forecast_category

		Parameters:
			forecast_category (ForecastCategory) : An instance of ForecastCategory
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.forecast_category import ForecastCategory
		except Exception:
			from .forecast_category import ForecastCategory

		if forecast_category is not None and not isinstance(forecast_category, ForecastCategory):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: forecast_category EXPECTED TYPE: ForecastCategory', None, None)
		
		self.__forecast_category = forecast_category
		self.__key_modified['forecast_category'] = 1

	def get_expected_data_type(self):
		"""
		The method to get the expected_data_type

		Returns:
			string: A string representing the expected_data_type
		"""

		return self.__expected_data_type

	def set_expected_data_type(self, expected_data_type):
		"""
		The method to set the value to expected_data_type

		Parameters:
			expected_data_type (string) : A string representing the expected_data_type
		"""

		if expected_data_type is not None and not isinstance(expected_data_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expected_data_type EXPECTED TYPE: str', None, None)
		
		self.__expected_data_type = expected_data_type
		self.__key_modified['expected_data_type'] = 1

	def get_sys_ref_name(self):
		"""
		The method to get the sys_ref_name

		Returns:
			string: A string representing the sys_ref_name
		"""

		return self.__sys_ref_name

	def set_sys_ref_name(self, sys_ref_name):
		"""
		The method to set the value to sys_ref_name

		Parameters:
			sys_ref_name (string) : A string representing the sys_ref_name
		"""

		if sys_ref_name is not None and not isinstance(sys_ref_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sys_ref_name EXPECTED TYPE: str', None, None)
		
		self.__sys_ref_name = sys_ref_name
		self.__key_modified['sys_ref_name'] = 1

	def get_forecast_type(self):
		"""
		The method to get the forecast_type

		Returns:
			string: A string representing the forecast_type
		"""

		return self.__forecast_type

	def set_forecast_type(self, forecast_type):
		"""
		The method to set the value to forecast_type

		Parameters:
			forecast_type (string) : A string representing the forecast_type
		"""

		if forecast_type is not None and not isinstance(forecast_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: forecast_type EXPECTED TYPE: str', None, None)
		
		self.__forecast_type = forecast_type
		self.__key_modified['forecast_type'] = 1

	def get_maps(self):
		"""
		The method to get the maps

		Returns:
			list: An instance of list
		"""

		return self.__maps

	def set_maps(self, maps):
		"""
		The method to set the value to maps

		Parameters:
			maps (list) : An instance of list
		"""

		if maps is not None and not isinstance(maps, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: maps EXPECTED TYPE: list', None, None)
		
		self.__maps = maps
		self.__key_modified['maps'] = 1

	def get_delete(self):
		"""
		The method to get the delete

		Returns:
			bool: A bool representing the delete
		"""

		return self.__delete

	def set_delete(self, delete):
		"""
		The method to set the value to delete

		Parameters:
			delete (bool) : A bool representing the delete
		"""

		if delete is not None and not isinstance(delete, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete EXPECTED TYPE: bool', None, None)
		
		self.__delete = delete
		self.__key_modified['_delete'] = 1

	def get_show_value(self):
		"""
		The method to get the show_value

		Returns:
			bool: A bool representing the show_value
		"""

		return self.__show_value

	def set_show_value(self, show_value):
		"""
		The method to set the value to show_value

		Parameters:
			show_value (bool) : A bool representing the show_value
		"""

		if show_value is not None and not isinstance(show_value, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_value EXPECTED TYPE: bool', None, None)
		
		self.__show_value = show_value
		self.__key_modified['show_value'] = 1

	def get_global_picklist_value(self):
		"""
		The method to get the global_picklist_value

		Returns:
			Picklist: An instance of Picklist
		"""

		return self.__global_picklist_value

	def set_global_picklist_value(self, global_picklist_value):
		"""
		The method to set the value to global_picklist_value

		Parameters:
			global_picklist_value (Picklist) : An instance of Picklist
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists import Picklist
		except Exception:
			from ..global_picklists import Picklist

		if global_picklist_value is not None and not isinstance(global_picklist_value, Picklist):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: global_picklist_value EXPECTED TYPE: Picklist', None, None)
		
		self.__global_picklist_value = global_picklist_value
		self.__key_modified['_global_picklist_value'] = 1

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
