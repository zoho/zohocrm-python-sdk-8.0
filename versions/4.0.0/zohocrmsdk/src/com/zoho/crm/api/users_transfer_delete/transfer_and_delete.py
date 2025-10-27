try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TransferAndDelete(object):
	def __init__(self):
		"""Creates an instance of TransferAndDelete"""

		self.__id = None
		self.__transfer = None
		self.__move_subordinate = None
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

	def get_transfer(self):
		"""
		The method to get the transfer

		Returns:
			Transfer: An instance of Transfer
		"""

		return self.__transfer

	def set_transfer(self, transfer):
		"""
		The method to set the value to transfer

		Parameters:
			transfer (Transfer) : An instance of Transfer
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_transfer_delete.transfer import Transfer
		except Exception:
			from .transfer import Transfer

		if transfer is not None and not isinstance(transfer, Transfer):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transfer EXPECTED TYPE: Transfer', None, None)
		
		self.__transfer = transfer
		self.__key_modified['transfer'] = 1

	def get_move_subordinate(self):
		"""
		The method to get the move_subordinate

		Returns:
			MoveSubordinate: An instance of MoveSubordinate
		"""

		return self.__move_subordinate

	def set_move_subordinate(self, move_subordinate):
		"""
		The method to set the value to move_subordinate

		Parameters:
			move_subordinate (MoveSubordinate) : An instance of MoveSubordinate
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_transfer_delete.move_subordinate import MoveSubordinate
		except Exception:
			from .move_subordinate import MoveSubordinate

		if move_subordinate is not None and not isinstance(move_subordinate, MoveSubordinate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: move_subordinate EXPECTED TYPE: MoveSubordinate', None, None)
		
		self.__move_subordinate = move_subordinate
		self.__key_modified['move_subordinate'] = 1

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
