try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TransferTerritory(object):
	def __init__(self):
		"""Creates an instance of TransferTerritory"""

		self.__id = None
		self.__transfer_to_id = None
		self.__delete_previous_forecasts = None
		self.__key_modified = dict()

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

	def get_transfer_to_id(self):
		"""
		The method to get the transfer_to_id

		Returns:
			int: An int representing the transfer_to_id
		"""

		return self.__transfer_to_id

	def set_transfer_to_id(self, transfer_to_id):
		"""
		The method to set the value to transfer_to_id

		Parameters:
			transfer_to_id (int) : An int representing the transfer_to_id
		"""

		if transfer_to_id is not None and not isinstance(transfer_to_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transfer_to_id EXPECTED TYPE: int', None, None)
		
		self.__transfer_to_id = transfer_to_id
		self.__key_modified['transfer_to_id'] = 1

	def get_delete_previous_forecasts(self):
		"""
		The method to get the delete_previous_forecasts

		Returns:
			bool: A bool representing the delete_previous_forecasts
		"""

		return self.__delete_previous_forecasts

	def set_delete_previous_forecasts(self, delete_previous_forecasts):
		"""
		The method to set the value to delete_previous_forecasts

		Parameters:
			delete_previous_forecasts (bool) : A bool representing the delete_previous_forecasts
		"""

		if delete_previous_forecasts is not None and not isinstance(delete_previous_forecasts, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete_previous_forecasts EXPECTED TYPE: bool', None, None)
		
		self.__delete_previous_forecasts = delete_previous_forecasts
		self.__key_modified['delete_previous_forecasts'] = 1

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
