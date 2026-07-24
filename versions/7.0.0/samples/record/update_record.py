import datetime

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, FileDetails, Consent, \
    LineItemProduct, LineTax, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_record(module_api_name, record_id):
        """
        This method is used to update a single record of a module with ID and print the response.
        :param module_api_name: The API Name of the record's module.
        :param record_id: The ID of the record to be updated
        """
        """
        example
        module_api_name = 'Leads'
        record_id = 3477061006603276
        """
        record_operations = RecordOperations(module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record = Record()
        """Call add_field_value method that takes two arguments Import the zcrmsdk.src.com.zoho.crm.api.record.field 
        file 1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field 
        name from the displayed list. 2 -> Value"""
        record.add_field_value(Field.Leads.last_name(), None)
        record.add_field_value(Field.Leads.first_name(), 'New')
        record.add_field_value(Field.Leads.company(), 'Zoho')
        record.add_field_value(Field.Leads.city(), 'City')
        record.add_field_value(Field.Leads.annual_revenue(), 3213.1)
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record.add_key_value('Custom_field', 'Value')
        record.add_key_value('Custom_field_2', 12)
        # record.add_key_value('Date', date(2020, 4, 9))
        record.add_key_value('Discounted', 23.34)
        file_details = []
        file_detail = FileDetails()
        file_detail.set_file_id__s('479f0f5579895383c8')
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
        # line_item_product.add_key_value("Products_External", "ProductExternal")
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

        # for custom fields
        record.add_key_value("External", "Value12345")
        record.add_key_value("CustomField", "custom_field")
        record.add_key_value("Long_Integer", 1213212112321)
        record.add_key_value("Decimal", 100.12)
        record.add_key_value("Datetime", datetime.datetime(2020, 12, 20, 10, 29, 33))
        record.add_key_value("Date_1", datetime.date(2020, 10, 12))
        record.add_key_value("Subject", "AutomatedSDK")
        record.add_key_value("Product_Name", "Automated")
        file_details = []
        file_detail = FileDetails()
        file_detail.set_file_id__s("ae9c7d729ad87c6d90b0bd44183")
        file_details.append(file_detail)
        file_detail2 = FileDetails()
        file_detail2.set_file_id__s("ae9c70bd44183")
        file_details.append(file_detail2)
        record.add_key_value("file_Upload", file_details)
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
        subform_list = []
        subform = Record()
        subform.add_key_value("custom_field", "customValue")
        user1 = MinifiedUser()
        user1.set_id(42393413434213)
        subform.add_key_value("User_field", user1)
        lookup = Record()
        lookup.set_id(44028001776029)
        subform.add_key_value("Test1", lookup)
        subform_list.append(subform)
        delete_subform = Record()
        delete_subform.set_id(44028001780062)
        delete_subform.add_key_value("_delete", None)
        subform_list.append(delete_subform)
        record.add_key_value("Subform_2", subform_list)
        # for MultiSelectLookUp / custom MultiSelectLookUp
        multi_select_list = []
        record1 = Record()
        record1.add_key_value("id", 44028001659002)
        linking_record = Record()
        linking_record.set_id(44028001787378)
        linking_record.add_key_value("_delete", None)
        linking_record.add_key_value("MultiSelectLookup", record1)
        multi_select_list.append(linking_record)
        record2 = Record()
        record2.add_key_value("id", 44028001655003)
        linking_record2 = Record()
        linking_record2.add_key_value("MultiSelectLookup", record2)
        multi_select_list.append(linking_record2)
        record.add_key_value("MultiSelectLookup", multi_select_list)

        # Add Record instance to the list
        records_list.append(record)
        request.set_data(records_list)
        trigger = ["approval", "workflow", "blueprint"]
        #
        request.set_trigger(trigger)
        header_instance = HeaderMap()
        # header_instance.add(UpdateRecordHeader.x_external, "Leads.External") header_instance.add(
        # UpdateRecordHeader.x_external, "Quotes.Quoted_Items.Product_Name.Products_External") Call updateRecord
        # method that takes record_id, module_api_name, BodyWrapper instance and header_instance as parameter.
        response = record_operations.update_record(
            record_id, request, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UpdateRecord.initialize()
UpdateRecord.update_record(module_api_name="Leads", record_id=44028001787377)
