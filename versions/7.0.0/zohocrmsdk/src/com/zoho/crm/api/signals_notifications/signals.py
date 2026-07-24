try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Signals(object):
	def __init__(self):
		"""Creates an instance of Signals"""

		self.__signal_namespace = None
		self.__email = None
		self.__subject = None
		self.__message = None
		self.__module = None
		self.__id = None
		self.__actions = None
		self.__key_modified = dict()

	def get_signal_namespace(self):
		"""
		The method to get the signal_namespace

		Returns:
			string: A string representing the signal_namespace
		"""

		return self.__signal_namespace

	def set_signal_namespace(self, signal_namespace):
		"""
		The method to set the value to signal_namespace

		Parameters:
			signal_namespace (string) : A string representing the signal_namespace
		"""

		if signal_namespace is not None and not isinstance(signal_namespace, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signal_namespace EXPECTED TYPE: str', None, None)
		
		self.__signal_namespace = signal_namespace
		self.__key_modified['signal_namespace'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

	def get_subject(self):
		"""
		The method to get the subject

		Returns:
			string: A string representing the subject
		"""

		return self.__subject

	def set_subject(self, subject):
		"""
		The method to set the value to subject

		Parameters:
			subject (string) : A string representing the subject
		"""

		if subject is not None and not isinstance(subject, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject EXPECTED TYPE: str', None, None)
		
		self.__subject = subject
		self.__key_modified['subject'] = 1

	def get_message(self):
		"""
		The method to get the message

		Returns:
			string: A string representing the message
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (string) : A string representing the message
		"""

		if message is not None and not isinstance(message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: str', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			string: A string representing the module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_actions(self):
		"""
		The method to get the actions

		Returns:
			list: An instance of list
		"""

		return self.__actions

	def set_actions(self, actions):
		"""
		The method to set the value to actions

		Parameters:
			actions (list) : An instance of list
		"""

		if actions is not None and not isinstance(actions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actions EXPECTED TYPE: list', None, None)
		
		self.__actions = actions
		self.__key_modified['actions'] = 1

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
