try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class SignMailMerge(object):
	def __init__(self):
		"""Creates an instance of SignMailMerge"""

		self.__mail_merge_template = None
		self.__sign_in_order = None
		self.__file_name = None
		self.__signers = None
		self.__key_modified = dict()

	def get_mail_merge_template(self):
		"""
		The method to get the mail_merge_template

		Returns:
			MailMergeTemplate: An instance of MailMergeTemplate
		"""

		return self.__mail_merge_template

	def set_mail_merge_template(self, mail_merge_template):
		"""
		The method to set the value to mail_merge_template

		Parameters:
			mail_merge_template (MailMergeTemplate) : An instance of MailMergeTemplate
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.mail_merge_template import MailMergeTemplate
		except Exception:
			from .mail_merge_template import MailMergeTemplate

		if mail_merge_template is not None and not isinstance(mail_merge_template, MailMergeTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_merge_template EXPECTED TYPE: MailMergeTemplate', None, None)
		
		self.__mail_merge_template = mail_merge_template
		self.__key_modified['mail_merge_template'] = 1

	def get_sign_in_order(self):
		"""
		The method to get the sign_in_order

		Returns:
			bool: A bool representing the sign_in_order
		"""

		return self.__sign_in_order

	def set_sign_in_order(self, sign_in_order):
		"""
		The method to set the value to sign_in_order

		Parameters:
			sign_in_order (bool) : A bool representing the sign_in_order
		"""

		if sign_in_order is not None and not isinstance(sign_in_order, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sign_in_order EXPECTED TYPE: bool', None, None)
		
		self.__sign_in_order = sign_in_order
		self.__key_modified['sign_in_order'] = 1

	def get_file_name(self):
		"""
		The method to get the file_name

		Returns:
			string: A string representing the file_name
		"""

		return self.__file_name

	def set_file_name(self, file_name):
		"""
		The method to set the value to file_name

		Parameters:
			file_name (string) : A string representing the file_name
		"""

		if file_name is not None and not isinstance(file_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name EXPECTED TYPE: str', None, None)
		
		self.__file_name = file_name
		self.__key_modified['file_name'] = 1

	def get_signers(self):
		"""
		The method to get the signers

		Returns:
			list: An instance of list
		"""

		return self.__signers

	def set_signers(self, signers):
		"""
		The method to set the value to signers

		Parameters:
			signers (list) : An instance of list
		"""

		if signers is not None and not isinstance(signers, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signers EXPECTED TYPE: list', None, None)
		
		self.__signers = signers
		self.__key_modified['signers'] = 1

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
