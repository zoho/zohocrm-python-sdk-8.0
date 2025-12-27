from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_read import BulkReadOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from pprint import pprint


class GetBulkReadJobDetails(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_bulk_read_job_details(job_id):
        """
        This method is used to get the details of a bulk read job performed previously.
        :param job_id: The unique ID of the bulk read job.
        """
        """
        example
        job_id = 3409643000002461001
        """
        bulk_read_operations = BulkReadOperations()
        response = bulk_read_operations.get_bulk_read_job_details(job_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    job_details_list = response_object.get_data()
                    for job_detail in job_details_list:
                        print("Bulk read Job ID: " + str(job_detail.get_id()))
                        print("Bulk read Operation: " + job_detail.get_operation())
                        print("Bulk read State: " + job_detail.get_state().get_value())
                        result = job_detail.get_result()
                        if result is not None:
                            print("Bulkread Result Page: " + str(result.get_page()))
                            print("Bulkread Result Count: " + str(result.get_count()))
                            print("Bulkread Result Download URL: " + result.get_download_url())
                            print("Bulkread Result Per_Page: " + str(result.get_per_page()))
                            print("Bulkread Result MoreRecords: " + str(result.get_more_records()))
                        query = job_detail.get_query()
                        if query is not None:
                            print("Bulk read Query Module: ")
                            print(query.get_module().__dict__)
                            print("Bulk read Query Page: " + str(query.get_page()))
                            print("Bulk read Query cvid: " + str(query.get_cvid()))
                            fields = query.get_fields()
                            if fields is not None:
                                print("Bulk read fields")
                                for field in fields:
                                    print(field)
                            criteria = query.get_criteria()
                            if criteria is not None:
                                GetBulkReadJobDetails.print_criteria(criteria)
                            created_by = job_detail.get_created_by()
                            if created_by is not None:
                                print("Bulkread Created By - Name: " + created_by.get_name())
                                print("Bulkread Created By - ID: " + str(created_by.get_id()))
                            print("Bulkread CreatedTime: " + str(job_detail.get_created_time()))
                            print("Bulkread File Type: " + job_detail.get_file_type())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_api_name() is not None:
            print('BulkRead Criteria API Name: ' + criteria.get_api_name())
        if criteria.get_comparator() is not None:
            print('BulkRead Criteria Comparator: ' + criteria.get_comparator().get_value())
        if criteria.get_value() is not None:
            print('BulkRead Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetBulkReadJobDetails.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('BulkRead Criteria Group Operator: ' + criteria.get_group_operator().get_value())


GetBulkReadJobDetails.initialize()
GetBulkReadJobDetails.get_bulk_read_job_details(job_id=1055806000028546001)