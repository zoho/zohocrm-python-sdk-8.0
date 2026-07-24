from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, GetMassUpdateStatusParam, \
    MassUpdateResponseWrapper, MassUpdate, APIException


class GetMassUpdateStatus:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_mass_update_status(module_api_name, job_id):
        """
        This method is used to get the status of the mass update job scheduled previously and print the response.
        :param module_api_name: The API Name of the module to obtain status of Mass Update.
        :param job_id: The ID of the job obtained from the response of Mass Update Records.
        """
        """
        example
        module_api_name = "Leads"
        job_id = "3477061005177002"
        """
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        # Possible parameters for Get MassUpdate Status operation
        param_instance.add(GetMassUpdateStatusParam.job_id, job_id)
        # Call getMassUpdateStatus method that takes ParameterMap instance and module_api_name as parameter
        response = record_operations.get_mass_update_status(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, MassUpdateResponseWrapper):
                    mass_update_responses = response_object.get_data()
                    for mass_update_response in mass_update_responses:
                        if isinstance(mass_update_response, MassUpdate):
                            print("MassUpdate Status: " +
                                  mass_update_response.get_status().get_value())
                            print("MassUpdate FailedCount: " +
                                  str(mass_update_response.get_failed_count()))
                            print("MassUpdate UpdatedCount: " +
                                  str(mass_update_response.get_updated_count()))
                            print("MassUpdate NotUpdatedCount: " +
                                  str(mass_update_response.get_not_updated_count()))
                            print("MassUpdate TotalCount: " +
                                  str(mass_update_response.get_total_count()))
                        elif isinstance(mass_update_response, APIException):
                            print(
                                "Status: " + mass_update_response.get_status().get_value())
                            print(
                                "Code: " + mass_update_response.get_code().get_value())
                            print("Details")
                            details = mass_update_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print(
                                "Message: " + mass_update_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetMassUpdateStatus.initialize()
GetMassUpdateStatus.get_mass_update_status(module_api_name="Leads", job_id=34234234324223)
