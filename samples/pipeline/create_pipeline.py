from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.pipeline import PipelineOperations, BodyWrapper, Pipeline, Maps
from zohocrmsdk.src.com.zoho.crm.api.pipeline import ActionWrapper, SuccessResponse, APIException


class CreatePipeline:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_pipeline(layout_id):
        """
        This method is used to create a pipeline for a layout and print the response.
        :param layout_id: The ID of the layout
        """
        try:
            pipeline_operations = PipelineOperations(layout_id)
            request = BodyWrapper()
            pipeline_list = []

            pipeline = Pipeline()
            pipeline.set_display_value("New Pipeline21")

            maps_list = []

            stage1 = Maps()
            stage1.set_id(1055806000000006805)
            stage1.set_display_value("Value Proposition")
            stage1.set_sequence_number(1)
            maps_list.append(stage1)

            pipeline.set_maps(maps_list)
            pipeline_list.append(pipeline)
            request.set_pipeline(pipeline_list)

            response = pipeline_operations.create_pipeline(request)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_pipeline()
                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                for key, value in details.items():
                                    print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message())
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
        except Exception as e:
            print("Exception when calling create_pipeline: " + str(e))


CreatePipeline.initialize()
CreatePipeline.create_pipeline(layout_id=1055806000000091023)
