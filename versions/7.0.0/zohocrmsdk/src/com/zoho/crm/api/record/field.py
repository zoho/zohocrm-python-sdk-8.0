try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Field(object):
	def __init__(self, api_name):
		"""
		Creates an instance of Field with the given parameters

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name


	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name


	class Products(object):
		
		@classmethod
		def product_category(cls):
			return Field('Product_Category')

		@classmethod
		def qty_in_demand(cls):
			return Field('Qty_in_Demand')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def vendor_name(cls):
			return Field('Vendor_Name')

		@classmethod
		def sales_start_date(cls):
			return Field('Sales_Start_Date')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def product_active(cls):
			return Field('Product_Active')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def product_code(cls):
			return Field('Product_Code')

		@classmethod
		def manufacturer(cls):
			return Field('Manufacturer')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def support_expiry_date(cls):
			return Field('Support_Expiry_Date')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def commission_rate(cls):
			return Field('Commission_Rate')

		@classmethod
		def product_name(cls):
			return Field('Product_Name')

		@classmethod
		def handler(cls):
			return Field('Handler')

		@classmethod
		def support_start_date(cls):
			return Field('Support_Start_Date')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def usage_unit(cls):
			return Field('Usage_Unit')

		@classmethod
		def qty_ordered(cls):
			return Field('Qty_Ordered')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def qty_in_stock(cls):
			return Field('Qty_in_Stock')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def sales_end_date(cls):
			return Field('Sales_End_Date')

		@classmethod
		def unit_price(cls):
			return Field('Unit_Price')

		@classmethod
		def reorder_level(cls):
			return Field('Reorder_Level')

		@classmethod
		def taxable(cls):
			return Field('Taxable')




	class Consents(object):
		
		@classmethod
		def contact_through_email(cls):
			return Field('Contact_Through_Email')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def email(cls):
			return Field('Email')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def consent_through(cls):
			return Field('Consent_Through')

		@classmethod
		def contact_through_survey(cls):
			return Field('Contact_Through_Survey')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def data_processing_basis(cls):
			return Field('Data_Processing_Basis')

		@classmethod
		def contact_through_phone(cls):
			return Field('Contact_Through_Phone')

		@classmethod
		def lawful_reason(cls):
			return Field('Lawful_Reason')

		@classmethod
		def mail_sent_time(cls):
			return Field('Mail_Sent_Time')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def consent_date(cls):
			return Field('Consent_Date')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def consent_remarks(cls):
			return Field('Consent_Remarks')




	class Tasks(object):
		
		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def due_date(cls):
			return Field('Due_Date')

		@classmethod
		def priority(cls):
			return Field('Priority')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def closed_time(cls):
			return Field('Closed_Time')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def send_notification_email(cls):
			return Field('Send_Notification_Email')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def recurring_activity(cls):
			return Field('Recurring_Activity')

		@classmethod
		def what_id(cls):
			return Field('What_Id')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def remind_at(cls):
			return Field('Remind_At')

		@classmethod
		def who_id(cls):
			return Field('Who_Id')




	class Data_Subject_Requests(object):
		
		@classmethod
		def request_type(cls):
			return Field('Request_Type')

		@classmethod
		def is_closed(cls):
			return Field('Is_Closed')

		@classmethod
		def parent_id(cls):
			return Field('Parent_Id')

		@classmethod
		def request_source(cls):
			return Field('Request_Source')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def closed_by(cls):
			return Field('Closed_By')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def requested_by(cls):
			return Field('Requested_By')

		@classmethod
		def requested_date(cls):
			return Field('Requested_Date')

		@classmethod
		def closed_date(cls):
			return Field('Closed_Date')




	class Vendors(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def email(cls):
			return Field('Email')

		@classmethod
		def category(cls):
			return Field('Category')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def vendor_name(cls):
			return Field('Vendor_Name')

		@classmethod
		def website(cls):
			return Field('Website')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def unsubscribed_mode(cls):
			return Field('Unsubscribed_Mode')

		@classmethod
		def phone(cls):
			return Field('Phone')

		@classmethod
		def street(cls):
			return Field('Street')

		@classmethod
		def zip_code(cls):
			return Field('Zip_Code')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def email_opt_out(cls):
			return Field('Email_Opt_Out')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def unsubscribed_time(cls):
			return Field('Unsubscribed_Time')

		@classmethod
		def city(cls):
			return Field('City')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def state(cls):
			return Field('State')

		@classmethod
		def gl_account(cls):
			return Field('GL_Account')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def country(cls):
			return Field('Country')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')




	class Appointments__s(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def address(cls):
			return Field('Address')

		@classmethod
		def appointment_start_time(cls):
			return Field('Appointment_Start_Time')

		@classmethod
		def cancellation_reason(cls):
			return Field('Cancellation_Reason')

		@classmethod
		def appointment_for(cls):
			return Field('Appointment_For')

		@classmethod
		def rescheduled_to(cls):
			return Field('Rescheduled_To')

		@classmethod
		def reschedule_reason(cls):
			return Field('Reschedule_Reason')

		@classmethod
		def job_sheet_name__s(cls):
			return Field('Job_Sheet_Name__s')

		@classmethod
		def additional_information(cls):
			return Field('Additional_Information')

		@classmethod
		def job_sheet_created__s(cls):
			return Field('Job_Sheet_Created__s')

		@classmethod
		def cancelled_time(cls):
			return Field('Cancelled_Time')

		@classmethod
		def cancellation_note(cls):
			return Field('Cancellation_Note')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def reschedule_count(cls):
			return Field('Reschedule_Count')

		@classmethod
		def rescheduled_by(cls):
			return Field('Rescheduled_By')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def rescheduled_time(cls):
			return Field('Rescheduled_Time')

		@classmethod
		def remind_at(cls):
			return Field('Remind_At')

		@classmethod
		def appointment_end_time(cls):
			return Field('Appointment_End_Time')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def service_name(cls):
			return Field('Service_Name')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def rescheduled_from(cls):
			return Field('Rescheduled_From')

		@classmethod
		def cancelled_by(cls):
			return Field('Cancelled_By')

		@classmethod
		def appointment_name(cls):
			return Field('Appointment_Name')

		@classmethod
		def duration(cls):
			return Field('Duration')

		@classmethod
		def job_sheet_section__s(cls):
			return Field('Job_Sheet_Section__s')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def job_sheet_description__s(cls):
			return Field('Job_Sheet_Description__s')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def location(cls):
			return Field('Location')

		@classmethod
		def reschedule_note(cls):
			return Field('Reschedule_Note')




	class Calls(object):
		
		@classmethod
		def call_duration(cls):
			return Field('Call_Duration')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def cti_entry(cls):
			return Field('CTI_Entry')

		@classmethod
		def caller_id(cls):
			return Field('Caller_ID')

		@classmethod
		def call_agenda(cls):
			return Field('Call_Agenda')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def call_purpose(cls):
			return Field('Call_Purpose')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def who_id(cls):
			return Field('Who_Id')

		@classmethod
		def outgoing_call_status(cls):
			return Field('Outgoing_Call_Status')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def reminder(cls):
			return Field('Reminder')

		@classmethod
		def voice_recording__s(cls):
			return Field('Voice_Recording__s')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def call_start_time(cls):
			return Field('Call_Start_Time')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def call_type(cls):
			return Field('Call_Type')

		@classmethod
		def call_result(cls):
			return Field('Call_Result')

		@classmethod
		def scheduled_in_crm(cls):
			return Field('Scheduled_In_CRM')

		@classmethod
		def what_id(cls):
			return Field('What_Id')

		@classmethod
		def call_duration_in_seconds(cls):
			return Field('Call_Duration_in_seconds')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def dialled_number(cls):
			return Field('Dialled_Number')




	class Leads(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def company(cls):
			return Field('Company')

		@classmethod
		def email(cls):
			return Field('Email')

		@classmethod
		def visitor_score(cls):
			return Field('Visitor_Score')

		@classmethod
		def last_activity_time(cls):
			return Field('Last_Activity_Time')

		@classmethod
		def industry(cls):
			return Field('Industry')

		@classmethod
		def unsubscribed_mode(cls):
			return Field('Unsubscribed_Mode')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def street(cls):
			return Field('Street')

		@classmethod
		def zip_code(cls):
			return Field('Zip_Code')

		@classmethod
		def data_processing_basis_details(cls):
			return Field('Data_Processing_Basis_Details')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def data_source(cls):
			return Field('Data_Source')

		@classmethod
		def enrich_status__s(cls):
			return Field('Enrich_Status__s')

		@classmethod
		def first_visited_url(cls):
			return Field('First_Visited_URL')

		@classmethod
		def days_visited(cls):
			return Field('Days_Visited')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def change_log_time__s(cls):
			return Field('Change_Log_Time__s')

		@classmethod
		def city(cls):
			return Field('City')

		@classmethod
		def no_of_employees(cls):
			return Field('No_of_Employees')

		@classmethod
		def data_processing_basis(cls):
			return Field('Data_Processing_Basis')

		@classmethod
		def converted__s(cls):
			return Field('Converted__s')

		@classmethod
		def converted_date_time(cls):
			return Field('Converted_Date_Time')

		@classmethod
		def converted_account(cls):
			return Field('Converted_Account')

		@classmethod
		def state(cls):
			return Field('State')

		@classmethod
		def country(cls):
			return Field('Country')

		@classmethod
		def last_visited_time(cls):
			return Field('Last_Visited_Time')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def annual_revenue(cls):
			return Field('Annual_Revenue')

		@classmethod
		def secondary_email(cls):
			return Field('Secondary_Email')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def number_of_chats(cls):
			return Field('Number_Of_Chats')

		@classmethod
		def rating(cls):
			return Field('Rating')

		@classmethod
		def website(cls):
			return Field('Website')

		@classmethod
		def twitter(cls):
			return Field('Twitter')

		@classmethod
		def average_time_spent_minutes(cls):
			return Field('Average_Time_Spent_Minutes')

		@classmethod
		def salutation(cls):
			return Field('Salutation')

		@classmethod
		def first_name(cls):
			return Field('First_Name')

		@classmethod
		def lead_status(cls):
			return Field('Lead_Status')

		@classmethod
		def full_name(cls):
			return Field('Full_Name')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def converted_deal(cls):
			return Field('Converted_Deal')

		@classmethod
		def lead_conversion_time(cls):
			return Field('Lead_Conversion_Time')

		@classmethod
		def skype_id(cls):
			return Field('Skype_ID')

		@classmethod
		def phone(cls):
			return Field('Phone')

		@classmethod
		def email_opt_out(cls):
			return Field('Email_Opt_Out')

		@classmethod
		def designation(cls):
			return Field('Designation')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def unsubscribed_time(cls):
			return Field('Unsubscribed_Time')

		@classmethod
		def converted_contact(cls):
			return Field('Converted_Contact')

		@classmethod
		def mobile(cls):
			return Field('Mobile')

		@classmethod
		def territories(cls):
			return Field('Territories')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def first_visited_time(cls):
			return Field('First_Visited_Time')

		@classmethod
		def last_name(cls):
			return Field('Last_Name')

		@classmethod
		def layout(cls):
			return Field('Layout')

		@classmethod
		def referrer(cls):
			return Field('Referrer')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def lead_source(cls):
			return Field('Lead_Source')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def fax(cls):
			return Field('Fax')

		@classmethod
		def last_enriched_time__s(cls):
			return Field('Last_Enriched_Time__s')




	class Deals(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def campaign_source(cls):
			return Field('Campaign_Source')

		@classmethod
		def closing_date(cls):
			return Field('Closing_Date')

		@classmethod
		def last_activity_time(cls):
			return Field('Last_Activity_Time')

		@classmethod
		def reason_for_loss__s(cls):
			return Field('Reason_For_Loss__s')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def lead_conversion_time(cls):
			return Field('Lead_Conversion_Time')

		@classmethod
		def deal_name(cls):
			return Field('Deal_Name')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def expected_revenue(cls):
			return Field('Expected_Revenue')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def overall_sales_duration(cls):
			return Field('Overall_Sales_Duration')

		@classmethod
		def stage(cls):
			return Field('Stage')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def territory(cls):
			return Field('Territory')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def amount(cls):
			return Field('Amount')

		@classmethod
		def probability(cls):
			return Field('Probability')

		@classmethod
		def next_step(cls):
			return Field('Next_Step')

		@classmethod
		def change_log_time__s(cls):
			return Field('Change_Log_Time__s')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def contact_name(cls):
			return Field('Contact_Name')

		@classmethod
		def pipeline(cls):
			return Field('Pipeline')

		@classmethod
		def sales_cycle_duration(cls):
			return Field('Sales_Cycle_Duration')

		@classmethod
		def type(cls):
			return Field('Type')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def lead_source(cls):
			return Field('Lead_Source')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')




	class Quotes(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def discount(cls):
			return Field('Discount')

		@classmethod
		def shipping_state(cls):
			return Field('Shipping_State')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def deal_name(cls):
			return Field('Deal_Name')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def valid_till(cls):
			return Field('Valid_Till')

		@classmethod
		def billing_country(cls):
			return Field('Billing_Country')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def team(cls):
			return Field('Team')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def carrier(cls):
			return Field('Carrier')

		@classmethod
		def quoted_items(cls):
			return Field('Quoted_Items')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def quote_stage(cls):
			return Field('Quote_Stage')

		@classmethod
		def grand_total(cls):
			return Field('Grand_Total')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def adjustment(cls):
			return Field('Adjustment')

		@classmethod
		def billing_street(cls):
			return Field('Billing_Street')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def terms_and_conditions(cls):
			return Field('Terms_and_Conditions')

		@classmethod
		def sub_total(cls):
			return Field('Sub_Total')

		@classmethod
		def billing_code(cls):
			return Field('Billing_Code')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def contact_name(cls):
			return Field('Contact_Name')

		@classmethod
		def shipping_city(cls):
			return Field('Shipping_City')

		@classmethod
		def shipping_country(cls):
			return Field('Shipping_Country')

		@classmethod
		def shipping_code(cls):
			return Field('Shipping_Code')

		@classmethod
		def billing_city(cls):
			return Field('Billing_City')

		@classmethod
		def quote_number(cls):
			return Field('Quote_Number')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def billing_state(cls):
			return Field('Billing_State')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def shipping_street(cls):
			return Field('Shipping_Street')




	class Invoices(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def discount(cls):
			return Field('Discount')

		@classmethod
		def shipping_state(cls):
			return Field('Shipping_State')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def invoice_date(cls):
			return Field('Invoice_Date')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def invoiced_items(cls):
			return Field('Invoiced_Items')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def billing_country(cls):
			return Field('Billing_Country')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def sales_order(cls):
			return Field('Sales_Order')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def sales_commission(cls):
			return Field('Sales_Commission')

		@classmethod
		def grand_total(cls):
			return Field('Grand_Total')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def due_date(cls):
			return Field('Due_Date')

		@classmethod
		def adjustment(cls):
			return Field('Adjustment')

		@classmethod
		def billing_street(cls):
			return Field('Billing_Street')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def terms_and_conditions(cls):
			return Field('Terms_and_Conditions')

		@classmethod
		def sub_total(cls):
			return Field('Sub_Total')

		@classmethod
		def invoice_number(cls):
			return Field('Invoice_Number')

		@classmethod
		def billing_code(cls):
			return Field('Billing_Code')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def excise_duty(cls):
			return Field('Excise_Duty')

		@classmethod
		def contact_name(cls):
			return Field('Contact_Name')

		@classmethod
		def shipping_city(cls):
			return Field('Shipping_City')

		@classmethod
		def shipping_country(cls):
			return Field('Shipping_Country')

		@classmethod
		def shipping_code(cls):
			return Field('Shipping_Code')

		@classmethod
		def billing_city(cls):
			return Field('Billing_City')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def purchase_order(cls):
			return Field('Purchase_Order')

		@classmethod
		def billing_state(cls):
			return Field('Billing_State')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def shipping_street(cls):
			return Field('Shipping_Street')




	class Campaigns(object):
		
		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def campaign_name(cls):
			return Field('Campaign_Name')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def end_date(cls):
			return Field('End_Date')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def type(cls):
			return Field('Type')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def num_sent(cls):
			return Field('Num_sent')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def expected_revenue(cls):
			return Field('Expected_Revenue')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def actual_cost(cls):
			return Field('Actual_Cost')

		@classmethod
		def expected_response(cls):
			return Field('Expected_Response')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def parent_campaign(cls):
			return Field('Parent_Campaign')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def start_date(cls):
			return Field('Start_Date')

		@classmethod
		def budgeted_cost(cls):
			return Field('Budgeted_Cost')




	class Attachments(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def file_name(cls):
			return Field('File_Name')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def size(cls):
			return Field('Size')

		@classmethod
		def parent_id(cls):
			return Field('Parent_Id')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')




	class Price_Books(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def pricing_details(cls):
			return Field('Pricing_Details')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def active(cls):
			return Field('Active')

		@classmethod
		def pricing_model(cls):
			return Field('Pricing_Model')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def price_book_name(cls):
			return Field('Price_Book_Name')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def id(cls):
			return Field('id')




	class Sales_Orders(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def discount(cls):
			return Field('Discount')

		@classmethod
		def customer_no(cls):
			return Field('Customer_No')

		@classmethod
		def shipping_state(cls):
			return Field('Shipping_State')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def deal_name(cls):
			return Field('Deal_Name')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def billing_country(cls):
			return Field('Billing_Country')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def carrier(cls):
			return Field('Carrier')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def ordered_items(cls):
			return Field('Ordered_Items')

		@classmethod
		def quote_name(cls):
			return Field('Quote_Name')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def sales_commission(cls):
			return Field('Sales_Commission')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def due_date(cls):
			return Field('Due_Date')

		@classmethod
		def adjustment(cls):
			return Field('Adjustment')

		@classmethod
		def billing_street(cls):
			return Field('Billing_Street')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def terms_and_conditions(cls):
			return Field('Terms_and_Conditions')

		@classmethod
		def sub_total(cls):
			return Field('Sub_Total')

		@classmethod
		def billing_code(cls):
			return Field('Billing_Code')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def contact_name(cls):
			return Field('Contact_Name')

		@classmethod
		def excise_duty(cls):
			return Field('Excise_Duty')

		@classmethod
		def shipping_city(cls):
			return Field('Shipping_City')

		@classmethod
		def shipping_country(cls):
			return Field('Shipping_Country')

		@classmethod
		def shipping_code(cls):
			return Field('Shipping_Code')

		@classmethod
		def billing_city(cls):
			return Field('Billing_City')

		@classmethod
		def so_number(cls):
			return Field('SO_Number')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def purchase_order(cls):
			return Field('Purchase_Order')

		@classmethod
		def billing_state(cls):
			return Field('Billing_State')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def pending(cls):
			return Field('Pending')

		@classmethod
		def shipping_street(cls):
			return Field('Shipping_Street')




	class Services__s(object):
		
		@classmethod
		def job_sheet_required(cls):
			return Field('Job_Sheet_Required')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def available_days(cls):
			return Field('Available_Days')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def unavailable_from(cls):
			return Field('Unavailable_From')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def available_dates(cls):
			return Field('Available_Dates')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def available_timings(cls):
			return Field('Available_Timings')

		@classmethod
		def service_name(cls):
			return Field('Service_Name')

		@classmethod
		def available_from(cls):
			return Field('Available_From')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def available_till(cls):
			return Field('Available_Till')

		@classmethod
		def duration(cls):
			return Field('Duration')

		@classmethod
		def job_sheet_section__s(cls):
			return Field('Job_Sheet_Section__s')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def price(cls):
			return Field('Price')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def availability_type(cls):
			return Field('Availability_Type')

		@classmethod
		def members(cls):
			return Field('Members')

		@classmethod
		def location(cls):
			return Field('Location')

		@classmethod
		def unavailable_till(cls):
			return Field('Unavailable_Till')




	class Contacts(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def email(cls):
			return Field('Email')

		@classmethod
		def visitor_score(cls):
			return Field('Visitor_Score')

		@classmethod
		def other_phone(cls):
			return Field('Other_Phone')

		@classmethod
		def mailing_state(cls):
			return Field('Mailing_State')

		@classmethod
		def other_state(cls):
			return Field('Other_State')

		@classmethod
		def other_country(cls):
			return Field('Other_Country')

		@classmethod
		def last_activity_time(cls):
			return Field('Last_Activity_Time')

		@classmethod
		def department(cls):
			return Field('Department')

		@classmethod
		def unsubscribed_mode(cls):
			return Field('Unsubscribed_Mode')

		@classmethod
		def assistant(cls):
			return Field('Assistant')

		@classmethod
		def mailing_country(cls):
			return Field('Mailing_Country')

		@classmethod
		def data_processing_basis_details(cls):
			return Field('Data_Processing_Basis_Details')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def data_source(cls):
			return Field('Data_Source')

		@classmethod
		def reporting_to(cls):
			return Field('Reporting_To')

		@classmethod
		def enrich_status__s(cls):
			return Field('Enrich_Status__s')

		@classmethod
		def first_visited_url(cls):
			return Field('First_Visited_URL')

		@classmethod
		def days_visited(cls):
			return Field('Days_Visited')

		@classmethod
		def other_city(cls):
			return Field('Other_City')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def change_log_time__s(cls):
			return Field('Change_Log_Time__s')

		@classmethod
		def data_processing_basis(cls):
			return Field('Data_Processing_Basis')

		@classmethod
		def home_phone(cls):
			return Field('Home_Phone')

		@classmethod
		def last_visited_time(cls):
			return Field('Last_Visited_Time')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def secondary_email(cls):
			return Field('Secondary_Email')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def vendor_name(cls):
			return Field('Vendor_Name')

		@classmethod
		def mailing_zip(cls):
			return Field('Mailing_Zip')

		@classmethod
		def reports_to(cls):
			return Field('Reports_To')

		@classmethod
		def number_of_chats(cls):
			return Field('Number_Of_Chats')

		@classmethod
		def other_zip(cls):
			return Field('Other_Zip')

		@classmethod
		def twitter(cls):
			return Field('Twitter')

		@classmethod
		def mailing_street(cls):
			return Field('Mailing_Street')

		@classmethod
		def average_time_spent_minutes(cls):
			return Field('Average_Time_Spent_Minutes')

		@classmethod
		def salutation(cls):
			return Field('Salutation')

		@classmethod
		def first_name(cls):
			return Field('First_Name')

		@classmethod
		def asst_phone(cls):
			return Field('Asst_Phone')

		@classmethod
		def full_name(cls):
			return Field('Full_Name')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def skype_id(cls):
			return Field('Skype_ID')

		@classmethod
		def phone(cls):
			return Field('Phone')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def email_opt_out(cls):
			return Field('Email_Opt_Out')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def date_of_birth(cls):
			return Field('Date_of_Birth')

		@classmethod
		def mailing_city(cls):
			return Field('Mailing_City')

		@classmethod
		def unsubscribed_time(cls):
			return Field('Unsubscribed_Time')

		@classmethod
		def title(cls):
			return Field('Title')

		@classmethod
		def other_street(cls):
			return Field('Other_Street')

		@classmethod
		def mobile(cls):
			return Field('Mobile')

		@classmethod
		def territories(cls):
			return Field('Territories')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def first_visited_time(cls):
			return Field('First_Visited_Time')

		@classmethod
		def last_name(cls):
			return Field('Last_Name')

		@classmethod
		def referrer(cls):
			return Field('Referrer')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def lead_source(cls):
			return Field('Lead_Source')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def fax(cls):
			return Field('Fax')

		@classmethod
		def last_enriched_time__s(cls):
			return Field('Last_Enriched_Time__s')




	class Solutions(object):
		
		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def comments(cls):
			return Field('Comments')

		@classmethod
		def no_of_comments(cls):
			return Field('No_of_comments')

		@classmethod
		def product_name(cls):
			return Field('Product_Name')

		@classmethod
		def add_comment(cls):
			return Field('Add_Comment')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def solution_number(cls):
			return Field('Solution_Number')

		@classmethod
		def answer(cls):
			return Field('Answer')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def solution_title(cls):
			return Field('Solution_Title')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def published(cls):
			return Field('Published')

		@classmethod
		def question(cls):
			return Field('Question')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def id(cls):
			return Field('id')




	class Events(object):
		
		@classmethod
		def all_day(cls):
			return Field('All_day')

		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def check_in_state(cls):
			return Field('Check_In_State')

		@classmethod
		def check_in_address(cls):
			return Field('Check_In_Address')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def remind_participants(cls):
			return Field('Remind_Participants')

		@classmethod
		def start_datetime(cls):
			return Field('Start_DateTime')

		@classmethod
		def latitude(cls):
			return Field('Latitude')

		@classmethod
		def participants(cls):
			return Field('Participants')

		@classmethod
		def event_title(cls):
			return Field('Event_Title')

		@classmethod
		def check_in_by(cls):
			return Field('Check_In_By')

		@classmethod
		def end_datetime(cls):
			return Field('End_DateTime')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def check_in_city(cls):
			return Field('Check_In_City')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def check_in_comment(cls):
			return Field('Check_In_Comment')

		@classmethod
		def remind_at(cls):
			return Field('Remind_At')

		@classmethod
		def who_id(cls):
			return Field('Who_Id')

		@classmethod
		def check_in_status(cls):
			return Field('Check_In_Status')

		@classmethod
		def check_in_country(cls):
			return Field('Check_In_Country')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def venue(cls):
			return Field('Venue')

		@classmethod
		def zip_code(cls):
			return Field('ZIP_Code')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def longitude(cls):
			return Field('Longitude')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def check_in_time(cls):
			return Field('Check_In_Time')

		@classmethod
		def recurring_activity(cls):
			return Field('Recurring_Activity')

		@classmethod
		def what_id(cls):
			return Field('What_Id')

		@classmethod
		def check_in_sub_locality(cls):
			return Field('Check_In_Sub_Locality')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')




	class Purchase_Orders(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def discount(cls):
			return Field('Discount')

		@classmethod
		def vendor_name(cls):
			return Field('Vendor_Name')

		@classmethod
		def shipping_state(cls):
			return Field('Shipping_State')

		@classmethod
		def tax(cls):
			return Field('Tax')

		@classmethod
		def po_date(cls):
			return Field('PO_Date')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def billing_country(cls):
			return Field('Billing_Country')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def purchase_items(cls):
			return Field('Purchase_Items')

		@classmethod
		def carrier(cls):
			return Field('Carrier')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def sales_commission(cls):
			return Field('Sales_Commission')

		@classmethod
		def grand_total(cls):
			return Field('Grand_Total')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def po_number(cls):
			return Field('PO_Number')

		@classmethod
		def due_date(cls):
			return Field('Due_Date')

		@classmethod
		def adjustment(cls):
			return Field('Adjustment')

		@classmethod
		def billing_street(cls):
			return Field('Billing_Street')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def terms_and_conditions(cls):
			return Field('Terms_and_Conditions')

		@classmethod
		def sub_total(cls):
			return Field('Sub_Total')

		@classmethod
		def billing_code(cls):
			return Field('Billing_Code')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def tracking_number(cls):
			return Field('Tracking_Number')

		@classmethod
		def contact_name(cls):
			return Field('Contact_Name')

		@classmethod
		def excise_duty(cls):
			return Field('Excise_Duty')

		@classmethod
		def shipping_city(cls):
			return Field('Shipping_City')

		@classmethod
		def shipping_country(cls):
			return Field('Shipping_Country')

		@classmethod
		def shipping_code(cls):
			return Field('Shipping_Code')

		@classmethod
		def billing_city(cls):
			return Field('Billing_City')

		@classmethod
		def requisition_no(cls):
			return Field('Requisition_No')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def billing_state(cls):
			return Field('Billing_State')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def shipping_street(cls):
			return Field('Shipping_Street')




	class Accounts(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def ownership(cls):
			return Field('Ownership')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def account_type(cls):
			return Field('Account_Type')

		@classmethod
		def rating(cls):
			return Field('Rating')

		@classmethod
		def sic_code(cls):
			return Field('SIC_Code')

		@classmethod
		def shipping_state(cls):
			return Field('Shipping_State')

		@classmethod
		def website(cls):
			return Field('Website')

		@classmethod
		def employees(cls):
			return Field('Employees')

		@classmethod
		def last_activity_time(cls):
			return Field('Last_Activity_Time')

		@classmethod
		def industry(cls):
			return Field('Industry')

		@classmethod
		def record_image(cls):
			return Field('Record_Image')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def account_site(cls):
			return Field('Account_Site')

		@classmethod
		def exchange_rate(cls):
			return Field('Exchange_Rate')

		@classmethod
		def phone(cls):
			return Field('Phone')

		@classmethod
		def billing_country(cls):
			return Field('Billing_Country')

		@classmethod
		def currency(cls):
			return Field('Currency')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def account_number(cls):
			return Field('Account_Number')

		@classmethod
		def ticker_symbol(cls):
			return Field('Ticker_Symbol')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def billing_street(cls):
			return Field('Billing_Street')

		@classmethod
		def enrich_status__s(cls):
			return Field('Enrich_Status__s')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def change_log_time__s(cls):
			return Field('Change_Log_Time__s')

		@classmethod
		def billing_code(cls):
			return Field('Billing_Code')

		@classmethod
		def territories(cls):
			return Field('Territories')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def parent_account(cls):
			return Field('Parent_Account')

		@classmethod
		def shipping_city(cls):
			return Field('Shipping_City')

		@classmethod
		def shipping_country(cls):
			return Field('Shipping_Country')

		@classmethod
		def shipping_code(cls):
			return Field('Shipping_Code')

		@classmethod
		def billing_city(cls):
			return Field('Billing_City')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def billing_state(cls):
			return Field('Billing_State')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def fax(cls):
			return Field('Fax')

		@classmethod
		def annual_revenue(cls):
			return Field('Annual_Revenue')

		@classmethod
		def last_enriched_time__s(cls):
			return Field('Last_Enriched_Time__s')

		@classmethod
		def shipping_street(cls):
			return Field('Shipping_Street')




	class Cases(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def email(cls):
			return Field('Email')

		@classmethod
		def description(cls):
			return Field('Description')

		@classmethod
		def internal_comments(cls):
			return Field('Internal_Comments')

		@classmethod
		def no_of_comments(cls):
			return Field('No_of_comments')

		@classmethod
		def reported_by(cls):
			return Field('Reported_By')

		@classmethod
		def case_number(cls):
			return Field('Case_Number')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def deal_name(cls):
			return Field('Deal_Name')

		@classmethod
		def phone(cls):
			return Field('Phone')

		@classmethod
		def account_name(cls):
			return Field('Account_Name')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def solution(cls):
			return Field('Solution')

		@classmethod
		def status(cls):
			return Field('Status')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def priority(cls):
			return Field('Priority')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def comments(cls):
			return Field('Comments')

		@classmethod
		def product_name(cls):
			return Field('Product_Name')

		@classmethod
		def add_comment(cls):
			return Field('Add_Comment')

		@classmethod
		def case_origin(cls):
			return Field('Case_Origin')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')

		@classmethod
		def case_reason(cls):
			return Field('Case_Reason')

		@classmethod
		def subject(cls):
			return Field('Subject')

		@classmethod
		def type(cls):
			return Field('Type')

		@classmethod
		def locked__s(cls):
			return Field('Locked__s')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def tag(cls):
			return Field('Tag')

		@classmethod
		def related_to(cls):
			return Field('Related_To')




	class Notes(object):
		
		@classmethod
		def owner(cls):
			return Field('Owner')

		@classmethod
		def modified_by(cls):
			return Field('Modified_By')

		@classmethod
		def modified_time(cls):
			return Field('Modified_Time')

		@classmethod
		def created_time(cls):
			return Field('Created_Time')

		@classmethod
		def parent_id(cls):
			return Field('Parent_Id')

		@classmethod
		def associated_id__s(cls):
			return Field('Associated_Id__s')

		@classmethod
		def created_by(cls):
			return Field('Created_By')

		@classmethod
		def id(cls):
			return Field('id')

		@classmethod
		def note_title(cls):
			return Field('Note_Title')

		@classmethod
		def note_content(cls):
			return Field('Note_Content')

		@classmethod
		def record_status__s(cls):
			return Field('Record_Status__s')


