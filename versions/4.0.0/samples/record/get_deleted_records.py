from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, GetDeletedRecordsParam, DeletedRecordsWrapper, \
    APIException


class GetRelatedRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_deleted_records(module_api_name):
        """
        This method is used to get the deleted records of a module and print the response.
        :param module_api_name: The API Name of the module to get the deleted records.
        """
        """
        example
        module_api_name = "Deals"
        """
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        # Possible parameters for Get Deleted Records operation
        param_instance.add(GetDeletedRecordsParam.page, 1)
        param_instance.add(GetDeletedRecordsParam.per_page, 200)
        # can be all/recycle/permanent
        param_instance.add(GetDeletedRecordsParam.type, 'permanent')
        header_instance = HeaderMap()
        # Possible headers for Get Deleted Records operation header_instance.add(
        # GetDeletedRecordsHeader.if_modified_since, datetime.fromisoformat('2020-01-15T10:35:32+05:30')) Call
        # getDeletedRecords method that takes param_instance, header_instance and module_api_name as parameter
        response = record_operations.get_deleted_records(param_instance, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, DeletedRecordsWrapper):
                    deleted_records = response_object.get_data()
                    for deleted_record in deleted_records:
                        deleted_by = deleted_record.get_deleted_by()
                        if deleted_by is not None:
                            print("Record Deleted By - Name: " +
                                  deleted_by.get_name())
                            print("Record Deleted By - ID: " +
                                  str(deleted_by.get_id()))
                        print("DeletedRecord ID: " +
                              str(deleted_record.get_id()))
                        print("DeletedRecord DisplayName: " +
                              str(deleted_record.get_display_name()))
                        print("DeletedRecord Type: " +
                              str(deleted_record.get_type()))
                        print("DeletedRecord DeletedTime: " +
                              str(deleted_record.get_deleted_time()))
                        created_by = deleted_record.get_created_by()
                        if created_by is not None:
                            print("Record Created By - Name: " +
                                  created_by.get_name())
                            print("Record Created By - ID: " +
                                  str(created_by.get_id()))
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
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetRelatedRecords.initialize()
GetRelatedRecords.get_deleted_records(module_api_name="Leads")
