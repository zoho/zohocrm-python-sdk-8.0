from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.coql import CoqlOperations, BodyWrapper, ResponseWrapper, APIException


class GetRecords(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_records():

        """
        This method is used to get records from the module through a COQL query.
        """
        query_operations = CoqlOperations()
        body_wrapper = BodyWrapper()
        select_query = "select Last_Name, Account_Name.Parent_Account, Account_Name.Parent_Account.Account_Name," \
                       "First_Name, Full_Name, Created_Time from Contacts where Last_Name is not null limit 200"
        body_wrapper.set_select_query(select_query)
        response = query_operations.get_records(body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    record_list = response_object.get_data()
                    for record in record_list:
                        print("Record ID: " + str(record.get_id()))
                        created_by = record.get_created_by()
                        if created_by is not None:
                            print("Record Created By - Name: " + created_by.get_name())
                            print("Record Created By - ID: " + created_by.get_id())
                            print("Record Created By - Email: " + created_by.get_email())
                        print("Record CreatedTime: " + str(record.get_created_time()))
                        if record.get_modified_time() is not None:
                            print("Record ModifiedTime: " + str(record.get_modified_time()))
                        modified_by = record.get_modified_by()
                        if modified_by is not None:
                            print("Record Modified By - Name: " + modified_by.get_name())
                            print("Record Modified By - ID: " + modified_by.get_id())
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
                            if info.get_count() is not None:
                                print('Record Info Count: ' + str(info.get_count()))
                            if info.get_more_records() is not None:
                                print('Record Info MoreRecords: ' + str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetRecords.initialize()
GetRecords.get_records()
