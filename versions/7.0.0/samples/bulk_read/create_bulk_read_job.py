import os

from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
from zohocrmsdk.src.com.zoho.crm.api.fields import MinifiedField
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_read import BulkReadOperations, BodyWrapper, CallBack, Query, Criteria, \
    ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class CreateBulkReadJob(object):

    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_bulk_read_job(module_api_name):
        """
        This method is used to create a bulk read job to export records.
        :param module_api_name: The API Name of the record's module
        """
        """
        example
        module_api_name = 'Leads'
        """
        bulk_read_operations = BulkReadOperations()
        request = BodyWrapper()
        call_back = CallBack()
        call_back.set_url("https://www.example.com/callback")
        call_back.set_method(Choice('post'))
        request.set_callback(call_back)
        query = Query()
        module = MinifiedModule()
        module.set_api_name(module_api_name)
        query.set_module(module)
        field_api_names = ['Last_Name']
        query.set_fields(field_api_names)
        query.set_page(1)
        criteria = Criteria()
        field = MinifiedField()
        field.set_api_name('Created_Time')
        criteria.set_field(field)
        criteria.set_comparator(Choice('between'))
        time = ["2020-06-03T17:31:48+05:30", "2020-06-03T17:31:48+05:30"]
        criteria.set_value(time)
        query.set_criteria(criteria)
        request.set_query(query)
        response = bulk_read_operations.create_bulk_read_job(request)
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
                    print("Message: " + response_object.get_message())


CreateBulkReadJob.initialize()
CreateBulkReadJob.create_bulk_read_job(module_api_name='Leads')