from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import DealContactRolesOperations, GetAssociatedContactRolesParam
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetAssociatedContactRoles:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)
    
    @staticmethod
    def get_associated_contact_roles(deal_id):
        """
        Get all contact roles associated with a deal
        :param deal_id: ID of the deal
        """
        try:
            deal_contact_roles_operations = DealContactRolesOperations()
            param_instance = ParameterMap()
            # param_instance.add(GetAssociatedContactRolesParam.fields, "Contact_Role,Contact")
            param_instance.add(GetAssociatedContactRolesParam.ids, "1055806000028482004")
            response = deal_contact_roles_operations.get_associated_contact_roles(deal_id, param_instance)
            
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print("No Content" if response.get_status_code() == 204 else "Not Modified")
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        record_list = response_object.get_data()
                        for record in record_list:
                            print("Record ID: ")
                            print(record.get_id())
                            created_by = record.get_created_by()
                            if created_by is not None:
                                print("Record Created By - Name: " + created_by.get_name())
                                print("Record Created By - ID: ")
                                print(created_by.get_id())
                                print("Record Created By - Email: " + created_by.get_email())
                            print("Record CreatedTime: " + str(record.get_created_time()))
                            if record.get_modified_time() is not None:
                                print("Record ModifiedTime: " + str(record.get_modified_time()))
                            modified_by = record.get_modified_by()
                            if modified_by is not None:
                                print("Record Modified By - Name: " + modified_by.get_name())
                                print("Record Modified By - ID: ")
                                print(modified_by.get_id())
                                print("Record Modified By - Email: " + modified_by.get_email())
                            print('Record KeyValues: ')
                            key_values = record.get_key_values()
                            for key_name, value in key_values.items():
                                if isinstance(value, list):
                                    print("Record KeyName : " + key_name)
                                    for data in value:
                                        if isinstance(data, dict):
                                            for dict_key, dict_value in data.items():
                                                print(dict_key + " : " + str(dict_value))
                                        else:
                                            print(str(data))
                                elif isinstance(value, dict):
                                    print("Record KeyName : " + key_name + " -  Value : ")
                                    for dict_key, dict_value in value.items():
                                        print(dict_key + " : " + str(dict_value))
                                else:
                                    print("Record KeyName : " + key_name + " -  Value : " + str(value))
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print('Record Info PerPage: ' +
                              str(info.get_per_page()))
                    if info.get_page() is not None:
                        print('Record Info Page: ' + str(info.get_page()))
                    if info.get_count() is not None:
                        print('Record Info Count: ' +
                              str(info.get_count()))
                    if info.get_more_records() is not None:
                        print('Record Info MoreRecords: ' +
                              str(info.get_more_records()))

                # Check if the request returned an exception
                elif isinstance(response_object, APIException):
                    # Get the Status
                    print("Status: " + response_object.get_status().get_value())

                    # Get the Code
                    print("Code: " + response_object.get_code().get_value())

                    print("Details")

                    # Get the details dict
                    details = response_object.get_details()

                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_associated_contact_roles: " + str(e))

GetAssociatedContactRoles.initialize()
GetAssociatedContactRoles.get_associated_contact_roles(1055806000028482009)  # Replace with actual deal ID