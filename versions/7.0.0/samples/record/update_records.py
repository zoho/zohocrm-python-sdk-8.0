from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, UpdateRecordsHeader, \
    LineTax, LineItemProduct, Consent, ActionWrapper, SuccessResponse, APIException


class UpdateRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_records(module_api_name):
        """
        This method is used to update the records of a module with ID and print the response.
        :param module_api_name: The API Name of the module to update records.
        """
        """
        example
        module_api_name = 'Leads'
        """
        record_operations = RecordOperations(module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record1 = Record()
        # ID of the record to be updated
        record1.set_id(440280746050)
        """Call add_field_value method that takes two arguments Import the zcrmsdk.src.com.zoho.crm.api.record.field 
        file 1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field 
        name from the displayed list. 2 -> Value"""
        record1.add_field_value(Field.Leads.last_name(), 'Python SDK')
        record1.add_field_value(Field.Leads.company(), 'NNN')
        record1.add_field_value(Field.Leads.city(), 'hola')
        record1.add_field_value(Field.Leads.annual_revenue(), 1333.1)
        """
        # Call add_key_value method that takes two arguments
        # 1 -> A string that is the Field's API Name
        # 2 -> Value
        """
        record1.add_key_value('Custom_field', 'Value')
        record1.add_key_value('Custom_field_2', 90)
        # Add Record instance to the list
        # records_list.append(record1)
        record2 = Record()
        # ID of the record to be updated
        record2.set_id(34770610126805)
        # Value to Record's fields can be provided in any of the following ways
        """# Call add_field_value method that takes two arguments # Import the 
        zcrmsdk.src.com.zoho.crm.api.record.field file # 1 -> Call Field "." and choose the module from the displayed 
        list and press "." and choose the field name from the displayed list. # 2 -> Value #"""
        #
        # record2.add_field_value(Field.Leads.last_name(), 'Edited Name')
        # record2.add_field_value(Field.Leads.city(), 'Hola')
        #
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        # """
        #
        # record2.add_key_value('Custom_field_2', 90)
        # record2.add_key_value('Discounted', 19.8)
        # Used when GDPR is enabled
        data_consent = Consent()
        data_consent.set_consent_remarks("Approved.")
        data_consent.set_consent_through('Email')
        data_consent.set_contact_through_email(True)
        data_consent.set_contact_through_social(False)
        # record2.add_key_value('Data_Processing_Basis_Details', data_consent)

        """
        Following methods are being used only by Inventory modules
        """
        deal_name = Record()
        deal_name.add_field_value(Field.Deals.id(), 3477061012416012)
        record2.add_field_value(Field.Sales_Orders.deal_name(), deal_name)
        contact_name = Record()
        contact_name.add_field_value(Field.Contacts.id(), 3477061012263005)
        record2.add_field_value(
            Field.Sales_Orders.contact_name(), contact_name)
        account_name = Record()
        # account_name.add_field_value(Field.Accounts.id(), 34096430692007)
        account_name.add_key_value("name", "automatedAccount")
        record2.add_field_value(
            Field.Sales_Orders.account_name(), account_name)
        record2.add_key_value("Discount", 10.5)
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
        record2.add_key_value('Quoted_Items', inventory_line_item_list)
        record2.add_field_value(Field.Quotes.subject(), "Python- testing")
        line_taxes = []
        line_tax = LineTax()
        line_tax.set_name('MyTax1134')
        line_tax.set_percentage(5.0)
        line_taxes.append(line_tax)
        record2.add_key_value("$line_tax", line_taxes)
        vendor_name = Record()
        vendor_name.set_id(3477061004996051)
        # record2.add_field_value(Field.Purchase_Orders.vendor_name(), vendor_name)

        """
        End Inventory
        """
        # Add Record instance to the list
        records_list.append(record2)
        # request.set_data(records_list)
        trigger = ["approval", "workflow", "blueprint"]
        request.set_trigger(trigger)
        header_instance = HeaderMap()
        header_instance.add(UpdateRecordsHeader.x_external,
                            "Quotes.Quoted_Items.Product_Name.Products_External")
        # Call update_records method that takes module_api_name, BodyWrapper instance and header_instance as parameter.
        response = record_operations.update_records(request, header_instance)
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


UpdateRecords.initialize()
UpdateRecords.update_records(module_api_name="Leads")
