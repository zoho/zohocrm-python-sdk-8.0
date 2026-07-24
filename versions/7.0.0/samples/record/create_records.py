from datetime import date, datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, ActionWrapper, \
    SuccessResponse, APIException, FileDetails, ImageUpload, Consent, Tax, LineItemProduct, LineTax, RemindAt, \
    RecurringActivity, Participants, PricingDetails
from zohocrmsdk.src.com.zoho.crm.api.tags import Tag
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_records(module_api_name):
        """
        This method is used to create records of a module and print the response.
        :param module_api_name: The API Name of the module to create records.
        """
        """
        example
        module_api_name = 'Leads'
        """
        record_operations = RecordOperations(module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record = Record()
        """
        Call add_field_value method that takes two arguments
        Import the zcrmsdk.src.com.zoho.crm.api.record.field file
        1 -> Call Field "." and choose the module from the displayed list and press "." and choose the 
             field name from the displayed list.
        2 -> Value
        """
        record.add_field_value(Field.Leads.last_name(), 'Python SDK')
        record.add_field_value(Field.Leads.first_name(), 'New')
        record.add_field_value(Field.Leads.company(), 'Zoho')
        record.add_field_value(Field.Leads.city(), 'City')
        record.add_field_value(Field.Leads.annual_revenue(), 1231.1)
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record.add_key_value('Custom_field', 'Value')
        record.add_key_value('Custom_field_2', 12)
        record.add_key_value('Date', date(2020, 4, 9))
        record.add_key_value('Total_Meetings_Created', 23.34)
        image_upload = ImageUpload()
        image_upload.set_file_id__s("ae9c7cefa41870aa54e793c5184e4b87")
        record.add_key_value("Image_Upload", [image_upload])
        file_details = []
        file_detail = FileDetails()
        file_detail.set_file_id__s('ae9c7cefa418aec1d59e756bf64b45f5ff128f1411ff')
        file_details.append(file_detail)
        file_detail = FileDetails()
        file_detail.set_file_id__s('ae9c7cefa418ae0ea1303d75859c')
        file_details.append(file_detail)
        file_detail = FileDetails()
        file_detail.set_file_id__s('479f0f5eebf0fb98c789f22579895383c8')
        file_details.append(file_detail)
        record.add_key_value('File_Upload', file_details)
        record_owner = MinifiedUser()
        record_owner.set_email("abc@zoho.com")
        record.add_key_value("Owner", record_owner)
        # Used when GDPR is enabled
        data_consent = Consent()
        data_consent.set_consent_remarks("Approved.")
        data_consent.set_consent_through('Email')
        data_consent.set_contact_through_email(True)
        data_consent.set_contact_through_social(False)
        record.add_key_value('Data_Processing_Basis_Details', data_consent)
        # Products
        tax = Tax()
        tax.set_value("15%")
        record.add_key_value("Tax", [tax])
        record.add_key_value("Product_Name", "AutomatedSDK")
        """
        Following methods are being used only by Inventory modules
        """
        deal_name = Record()
        deal_name.add_field_value(Field.Deals.id(), 3477061012416012)
        record.add_field_value(Field.Sales_Orders.deal_name(), deal_name)
        contact_name = Record()
        contact_name.add_field_value(Field.Contacts.id(), 3477061012263005)
        record.add_field_value(Field.Sales_Orders.contact_name(), contact_name)
        account_name = Record()
        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)
        account_name.add_key_value("name", "automatedAccount")
        record.add_field_value(Field.Sales_Orders.account_name(), account_name)
        record.add_key_value("Discount", 10.5)
        inventory_line_item_list = []
        inventory_line_item = Record()
        line_item_product = LineItemProduct()
        line_item_product.set_id(3477061012402032)
        line_item_product.add_key_value("Products_External", "ProductExternal")
        inventory_line_item.add_key_value("Product_Name", line_item_product)
        inventory_line_item.add_key_value("Quantity", 3.0)
        inventory_line_item.add_key_value("Description", 'productDescription')
        inventory_line_item.add_key_value("ListPrice", 10.0)
        inventory_line_item.add_key_value("Discount", '5.90')
        product_line_taxes = []
        product_line_tax = LineTax()
        product_line_tax.set_name('MyTax1134')
        product_line_tax.set_percentage(12.1)
        product_line_taxes.append(product_line_tax)
        inventory_line_item.add_key_value("Line_Tax", product_line_taxes)
        inventory_line_item_list.append(inventory_line_item)
        record.add_key_value('Quoted_Items', inventory_line_item_list)
        record.add_field_value(Field.Quotes.subject(), "Python- testing")
        line_taxes = []
        line_tax = LineTax()
        line_tax.set_name('MyTax1134')
        line_tax.set_percentage(5.0)
        line_taxes.append(line_tax)
        record.add_key_value("$line_tax", line_taxes)
        vendor_name = Record()
        vendor_name.set_id(3477061004996051)
        record.add_field_value(
            Field.Purchase_Orders.vendor_name(), vendor_name)
        """
        End Inventory
        """
        """
        Following methods are being used only by Activity modules
        """
        record.add_field_value(Field.Tasks.description(), "New Task")
        record.add_key_value('Currency', Choice('INR'))
        remind_at = RemindAt()
        remind_at.set_alarm("FREQ=NONE;ACTION=POPUP;TRIGGER=DATE-TIME:2021-01-18T12:45:00+05:30")
        record.add_field_value(Field.Tasks.remind_at(), remind_at)
        record.add_field_value(Field.Tasks.subject(), "Python - testing")
        record.add_field_value(Field.Calls.reminder(), Choice("5 mins"))
        record.add_field_value(Field.Calls.call_type(), Choice("Outbound"))
        record.add_field_value(Field.Calls.call_start_time(), datetime(2020, 12, 1, 1, 1, 1))
        who_id = Record()
        who_id.set_id(3477061012263005)
        record.add_field_value(Field.Tasks.who_id(), who_id)
        record.add_field_value(Field.Tasks.status(), Choice('Waiting for Input'))
        record.add_field_value(Field.Tasks.due_date(), date(2020, 10, 10))
        record.add_field_value(Field.Tasks.priority(), Choice('High'))
        what_id = Record()
        what_id.set_id(3477061012263002)
        record.add_field_value(Field.Tasks.what_id(), what_id)
        record.add_key_value("$se_module", "Accounts")
        # Recurring Activity can be provided in any activity module
        recurring_activity = RecurringActivity()
        recurring_activity.set_rrule('FREQ=DAILY;INTERVAL=10;UNTIL=2022-08-14;DTSTART=2022-07-03')
        record.add_field_value(Field.Events.recurring_activity(), recurring_activity)
        record.add_field_value(Field.Events.description(), "My Event")
        start_date_time = datetime.fromisoformat('2022-07-03T12:30:00+05:30')
        record.add_field_value(Field.Events.start_datetime(), start_date_time)
        participants_list = []
        participant = Participants()
        participant.set_participant('test@zoho.com')
        participant.set_type('email')
        participants_list.append(participant)
        participant = Participants()
        participant.set_participant('3477061012263005')
        participant.set_type('contact')
        participants_list.append(participant)
        record.add_field_value(Field.Events.participants(), participants_list)
        record.add_key_value("$send_notification", True)
        record.add_field_value(Field.Events.event_title(), "New Automated Event")
        end_date_time = datetime(2022, 9, 3, 10, 10, 10)
        record.add_field_value(Field.Events.end_datetime(), end_date_time)
        remind_at_value = datetime(2022, 7, 3, 8, 10, 10)
        record.add_field_value(Field.Events.remind_at(), remind_at_value)
        record.add_field_value(Field.Events.check_in_status(), 'PLANNED')
        what_id = Record()
        what_id.set_id(3477061012673010)
        record.add_field_value(Field.Events.what_id(), what_id)
        record.add_key_value("$se_module", "Leads")
        """
        End Activity
        """
        """
        Following methods are being used only by Price_Books module
        """
        pricing_details_list = []
        pricing_detail = PricingDetails()
        pricing_detail.set_from_range(1.0)
        pricing_detail.set_to_range(5.0)
        pricing_detail.set_discount(2.1)
        pricing_details_list.append(pricing_detail)
        pricing_detail = PricingDetails()
        pricing_detail.add_key_value('from_range', 6.0)
        pricing_detail.add_key_value('to_range', 11.0)
        pricing_detail.add_key_value('discount', 3.0)
        pricing_details_list.append(pricing_detail)
        record.add_field_value(Field.Price_Books.pricing_details(), pricing_details_list)
        record.add_key_value("Email", "abc@zoho.com")
        record.add_field_value(Field.Price_Books.description(), "My Price Book")
        record.add_field_value(Field.Price_Books.price_book_name(), 'book_name')
        record.add_field_value(Field.Price_Books.pricing_model(), Choice('Flat'))
        """
        End of Price_Books
        """
        # for custom fields
        record.add_key_value("External", "Value12345")
        record.add_key_value("CustomField", "custom_field")
        record.add_key_value("Longinteger", 1213212112321)
        record.add_key_value("Decimal", 100.12)
        record.add_key_value("Datetime", datetime(2020, 12, 20, 10, 29, 33))
        record.add_key_value("Date_1", date(2020, 10, 12))
        record.add_key_value("Subject", "AutomatedSDK")
        record.add_key_value("Product_Name", "Automated")
        fileDetails = []
        fileDetail = FileDetails()
        fileDetail.set_file_id__s("ae9c7cefa418aec1d6a5cc2d9ab35c32a6ae23d729ad87c6d90b0bd44183")
        fileDetails.append(fileDetail)
        fileDetail2 = FileDetails()
        fileDetail2.set_file_id__s("ae9c7cefa418aec1d6a5cc2d9ab35c32a6ae2329ad87c6d90b0bd44183")
        fileDetails.append(fileDetail2)
        record.add_key_value("file_Upload", fileDetails)
        # for Custom User LookUp
        user = MinifiedUser()
        user.set_id(4402800254001)
        record.add_key_value("User_1", user)
        # for Custom LookUp
        data = Record()
        data.set_id(44028001780047)
        record.add_key_value("Lookup_1", data)
        # for Custom PicKList
        record.add_key_value("Pick", Choice("true"))
        # for Custom MultiPickList
        record.add_key_value("Multiselect", [Choice("Option 1"), Choice("Option 2")])
        # for Subform
        subformList = []
        subform = Record()
        subform.add_key_value("customfield", "customValue")
        user1 = MinifiedUser()
        user1.set_id(4402800254001)
        subform.add_key_value("Userfield", user1)
        lookup = Record()
        lookup.set_id(44028001776029)
        subform.add_key_value("Test1", lookup)
        subformList.append(subform)
        record.add_key_value("Subform_2", subformList)
        # for MultiSelectLookUp / custom MultiSelectLookUp
        multiSelectList = []
        record = Record()
        record.add_key_value("id", 44028001659002)
        linkingRecord = Record()
        linkingRecord.add_key_value("MultiSelectLookup", record)
        multiSelectList.append(linkingRecord)
        record2 = Record()
        record2.add_key_value("id", 44028001655003)
        linkingRecord2 = Record()
        linkingRecord2.add_key_value("MultiSelectLookup", record2)
        multiSelectList.append(linkingRecord2)
        record.add_key_value("MultiSelectLookup", multiSelectList)

        tags_list = []
        tag = Tag()
        tag.set_name("My Record")
        tags_list.append(tag)
        record.set_tag(tags_list)
        # Add Record instance to the list
        records_list.append(record)
        request.set_data(records_list)
        trigger = ["approval", "workflow", "blueprint"]
        request.set_trigger(trigger)
        lar_id = '3409643002157065'
        request.set_lar_id(lar_id)
        process = ["review_process"]
        request.set_process(process)
        header_instance = HeaderMap()
        # header_instance.add(CreateRecordsHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External")
        # Call create_records method that takes module_api_name, BodyWrapper instance and header_instance as parameters
        response = record_operations.create_records(request, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


CreateRecords.initialize()
CreateRecords.create_records(module_api_name="Leads")
