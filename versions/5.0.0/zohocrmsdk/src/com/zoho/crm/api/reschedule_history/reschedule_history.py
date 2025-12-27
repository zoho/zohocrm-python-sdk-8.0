try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RescheduleHistory(object):
	def __init__(self):
		"""Creates an instance of RescheduleHistory"""

		self.__currency_symbol = None
		self.__rescheduled_to = None
		self.__review_process = None
		self.__reschedule_reason = None
		self.__sharing_permission = None
		self.__name = None
		self.__modified_by = None
		self.__review = None
		self.__rescheduled_by = None
		self.__state = None
		self.__canvas_id = None
		self.__process_flow = None
		self.__id = None
		self.__rescheduled_time = None
		self.__zia_visions = None
		self.__approved = None
		self.__modified_time = None
		self.__approval = None
		self.__created_time = None
		self.__rescheduled_from = None
		self.__appointment_name = None
		self.__editable = None
		self.__orchestration = None
		self.__in_merge = None
		self.__created_by = None
		self.__approval_state = None
		self.__reschedule_note = None
		self.__key_modified = dict()

	def get_currency_symbol(self):
		"""
		The method to get the currency_symbol

		Returns:
			string: A string representing the currency_symbol
		"""

		return self.__currency_symbol

	def set_currency_symbol(self, currency_symbol):
		"""
		The method to set the value to currency_symbol

		Parameters:
			currency_symbol (string) : A string representing the currency_symbol
		"""

		if currency_symbol is not None and not isinstance(currency_symbol, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency_symbol EXPECTED TYPE: str', None, None)
		
		self.__currency_symbol = currency_symbol
		self.__key_modified['$currency_symbol'] = 1

	def get_rescheduled_to(self):
		"""
		The method to get the rescheduled_to

		Returns:
			datetime: An instance of datetime
		"""

		return self.__rescheduled_to

	def set_rescheduled_to(self, rescheduled_to):
		"""
		The method to set the value to rescheduled_to

		Parameters:
			rescheduled_to (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if rescheduled_to is not None and not isinstance(rescheduled_to, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rescheduled_to EXPECTED TYPE: datetime', None, None)
		
		self.__rescheduled_to = rescheduled_to
		self.__key_modified['Rescheduled_To'] = 1

	def get_review_process(self):
		"""
		The method to get the review_process

		Returns:
			bool: A bool representing the review_process
		"""

		return self.__review_process

	def set_review_process(self, review_process):
		"""
		The method to set the value to review_process

		Parameters:
			review_process (bool) : A bool representing the review_process
		"""

		if review_process is not None and not isinstance(review_process, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: review_process EXPECTED TYPE: bool', None, None)
		
		self.__review_process = review_process
		self.__key_modified['$review_process'] = 1

	def get_reschedule_reason(self):
		"""
		The method to get the reschedule_reason

		Returns:
			string: A string representing the reschedule_reason
		"""

		return self.__reschedule_reason

	def set_reschedule_reason(self, reschedule_reason):
		"""
		The method to set the value to reschedule_reason

		Parameters:
			reschedule_reason (string) : A string representing the reschedule_reason
		"""

		if reschedule_reason is not None and not isinstance(reschedule_reason, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reschedule_reason EXPECTED TYPE: str', None, None)
		
		self.__reschedule_reason = reschedule_reason
		self.__key_modified['Reschedule_Reason'] = 1

	def get_sharing_permission(self):
		"""
		The method to get the sharing_permission

		Returns:
			string: A string representing the sharing_permission
		"""

		return self.__sharing_permission

	def set_sharing_permission(self, sharing_permission):
		"""
		The method to set the value to sharing_permission

		Parameters:
			sharing_permission (string) : A string representing the sharing_permission
		"""

		if sharing_permission is not None and not isinstance(sharing_permission, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sharing_permission EXPECTED TYPE: str', None, None)
		
		self.__sharing_permission = sharing_permission
		self.__key_modified['$sharing_permission'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['Name'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.reschedule_history.user import User
		except Exception:
			from .user import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['Modified_By'] = 1

	def get_review(self):
		"""
		The method to get the review

		Returns:
			bool: A bool representing the review
		"""

		return self.__review

	def set_review(self, review):
		"""
		The method to set the value to review

		Parameters:
			review (bool) : A bool representing the review
		"""

		if review is not None and not isinstance(review, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: review EXPECTED TYPE: bool', None, None)
		
		self.__review = review
		self.__key_modified['$review'] = 1

	def get_rescheduled_by(self):
		"""
		The method to get the rescheduled_by

		Returns:
			User: An instance of User
		"""

		return self.__rescheduled_by

	def set_rescheduled_by(self, rescheduled_by):
		"""
		The method to set the value to rescheduled_by

		Parameters:
			rescheduled_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.reschedule_history.user import User
		except Exception:
			from .user import User

		if rescheduled_by is not None and not isinstance(rescheduled_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rescheduled_by EXPECTED TYPE: User', None, None)
		
		self.__rescheduled_by = rescheduled_by
		self.__key_modified['Rescheduled_By'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['$state'] = 1

	def get_canvas_id(self):
		"""
		The method to get the canvas_id

		Returns:
			string: A string representing the canvas_id
		"""

		return self.__canvas_id

	def set_canvas_id(self, canvas_id):
		"""
		The method to set the value to canvas_id

		Parameters:
			canvas_id (string) : A string representing the canvas_id
		"""

		if canvas_id is not None and not isinstance(canvas_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: canvas_id EXPECTED TYPE: str', None, None)
		
		self.__canvas_id = canvas_id
		self.__key_modified['$canvas_id'] = 1

	def get_process_flow(self):
		"""
		The method to get the process_flow

		Returns:
			bool: A bool representing the process_flow
		"""

		return self.__process_flow

	def set_process_flow(self, process_flow):
		"""
		The method to set the value to process_flow

		Parameters:
			process_flow (bool) : A bool representing the process_flow
		"""

		if process_flow is not None and not isinstance(process_flow, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: process_flow EXPECTED TYPE: bool', None, None)
		
		self.__process_flow = process_flow
		self.__key_modified['$process_flow'] = 1

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

	def get_rescheduled_time(self):
		"""
		The method to get the rescheduled_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__rescheduled_time

	def set_rescheduled_time(self, rescheduled_time):
		"""
		The method to set the value to rescheduled_time

		Parameters:
			rescheduled_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if rescheduled_time is not None and not isinstance(rescheduled_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rescheduled_time EXPECTED TYPE: datetime', None, None)
		
		self.__rescheduled_time = rescheduled_time
		self.__key_modified['Rescheduled_Time'] = 1

	def get_zia_visions(self):
		"""
		The method to get the zia_visions

		Returns:
			bool: A bool representing the zia_visions
		"""

		return self.__zia_visions

	def set_zia_visions(self, zia_visions):
		"""
		The method to set the value to zia_visions

		Parameters:
			zia_visions (bool) : A bool representing the zia_visions
		"""

		if zia_visions is not None and not isinstance(zia_visions, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_visions EXPECTED TYPE: bool', None, None)
		
		self.__zia_visions = zia_visions
		self.__key_modified['$zia_visions'] = 1

	def get_approved(self):
		"""
		The method to get the approved

		Returns:
			bool: A bool representing the approved
		"""

		return self.__approved

	def set_approved(self, approved):
		"""
		The method to set the value to approved

		Parameters:
			approved (bool) : A bool representing the approved
		"""

		if approved is not None and not isinstance(approved, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approved EXPECTED TYPE: bool', None, None)
		
		self.__approved = approved
		self.__key_modified['$approved'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['Modified_Time'] = 1

	def get_approval(self):
		"""
		The method to get the approval

		Returns:
			Approval: An instance of Approval
		"""

		return self.__approval

	def set_approval(self, approval):
		"""
		The method to set the value to approval

		Parameters:
			approval (Approval) : An instance of Approval
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.reschedule_history.approval import Approval
		except Exception:
			from .approval import Approval

		if approval is not None and not isinstance(approval, Approval):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approval EXPECTED TYPE: Approval', None, None)
		
		self.__approval = approval
		self.__key_modified['$approval'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['Created_Time'] = 1

	def get_rescheduled_from(self):
		"""
		The method to get the rescheduled_from

		Returns:
			datetime: An instance of datetime
		"""

		return self.__rescheduled_from

	def set_rescheduled_from(self, rescheduled_from):
		"""
		The method to set the value to rescheduled_from

		Parameters:
			rescheduled_from (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if rescheduled_from is not None and not isinstance(rescheduled_from, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rescheduled_from EXPECTED TYPE: datetime', None, None)
		
		self.__rescheduled_from = rescheduled_from
		self.__key_modified['Rescheduled_From'] = 1

	def get_appointment_name(self):
		"""
		The method to get the appointment_name

		Returns:
			AppointmentName: An instance of AppointmentName
		"""

		return self.__appointment_name

	def set_appointment_name(self, appointment_name):
		"""
		The method to set the value to appointment_name

		Parameters:
			appointment_name (AppointmentName) : An instance of AppointmentName
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.reschedule_history.appointment_name import AppointmentName
		except Exception:
			from .appointment_name import AppointmentName

		if appointment_name is not None and not isinstance(appointment_name, AppointmentName):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: appointment_name EXPECTED TYPE: AppointmentName', None, None)
		
		self.__appointment_name = appointment_name
		self.__key_modified['Appointment_Name'] = 1

	def get_editable(self):
		"""
		The method to get the editable

		Returns:
			bool: A bool representing the editable
		"""

		return self.__editable

	def set_editable(self, editable):
		"""
		The method to set the value to editable

		Parameters:
			editable (bool) : A bool representing the editable
		"""

		if editable is not None and not isinstance(editable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editable EXPECTED TYPE: bool', None, None)
		
		self.__editable = editable
		self.__key_modified['$editable'] = 1

	def get_orchestration(self):
		"""
		The method to get the orchestration

		Returns:
			bool: A bool representing the orchestration
		"""

		return self.__orchestration

	def set_orchestration(self, orchestration):
		"""
		The method to set the value to orchestration

		Parameters:
			orchestration (bool) : A bool representing the orchestration
		"""

		if orchestration is not None and not isinstance(orchestration, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: orchestration EXPECTED TYPE: bool', None, None)
		
		self.__orchestration = orchestration
		self.__key_modified['$orchestration'] = 1

	def get_in_merge(self):
		"""
		The method to get the in_merge

		Returns:
			bool: A bool representing the in_merge
		"""

		return self.__in_merge

	def set_in_merge(self, in_merge):
		"""
		The method to set the value to in_merge

		Parameters:
			in_merge (bool) : A bool representing the in_merge
		"""

		if in_merge is not None and not isinstance(in_merge, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: in_merge EXPECTED TYPE: bool', None, None)
		
		self.__in_merge = in_merge
		self.__key_modified['$in_merge'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.reschedule_history.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['Created_By'] = 1

	def get_approval_state(self):
		"""
		The method to get the approval_state

		Returns:
			string: A string representing the approval_state
		"""

		return self.__approval_state

	def set_approval_state(self, approval_state):
		"""
		The method to set the value to approval_state

		Parameters:
			approval_state (string) : A string representing the approval_state
		"""

		if approval_state is not None and not isinstance(approval_state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approval_state EXPECTED TYPE: str', None, None)
		
		self.__approval_state = approval_state
		self.__key_modified['$approval_state'] = 1

	def get_reschedule_note(self):
		"""
		The method to get the reschedule_note

		Returns:
			string: A string representing the reschedule_note
		"""

		return self.__reschedule_note

	def set_reschedule_note(self, reschedule_note):
		"""
		The method to set the value to reschedule_note

		Parameters:
			reschedule_note (string) : A string representing the reschedule_note
		"""

		if reschedule_note is not None and not isinstance(reschedule_note, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reschedule_note EXPECTED TYPE: str', None, None)
		
		self.__reschedule_note = reschedule_note
		self.__key_modified['Reschedule_Note'] = 1

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
