try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class DownloadMailMerge(object):
	def __init__(self):
		"""Creates an instance of DownloadMailMerge"""

		self.__mail_merge_template = None
		self.__output_format = None
		self.__file_name = None
		self.__password = None
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

	def get_output_format(self):
		"""
		The method to get the output_format

		Returns:
			Choice: An instance of Choice
		"""

		return self.__output_format

	def set_output_format(self, output_format):
		"""
		The method to set the value to output_format

		Parameters:
			output_format (Choice) : An instance of Choice
		"""

		if output_format is not None and not isinstance(output_format, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_format EXPECTED TYPE: Choice', None, None)
		
		self.__output_format = output_format
		self.__key_modified['output_format'] = 1

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

	def get_password(self):
		"""
		The method to get the password

		Returns:
			string: A string representing the password
		"""

		return self.__password

	def set_password(self, password):
		"""
		The method to set the value to password

		Parameters:
			password (string) : A string representing the password
		"""

		if password is not None and not isinstance(password, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: password EXPECTED TYPE: str', None, None)
		
		self.__password = password
		self.__key_modified['password'] = 1

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
