from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.pipeline import PipelineOperations, TransferPipelineWrapper, TransferPipeline, TPipeline, Stages
from zohocrmsdk.src.com.zoho.crm.api.pipeline import TransferPipelineActionWrapper, TransferPipelineSuccessResponse, APIException


class TransferPipelines:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def transfer_pipelines(layout_id):
        """
        This method is used to transfer and delete pipelines and print the response.
        :param layout_id: The ID of the layout
        """
        try:
            pipeline_operations = PipelineOperations(layout_id)
            request = TransferPipelineWrapper()
            transfer_pipeline_list = []

            transfer_pipeline = TransferPipeline()

            t_pipeline = TPipeline()
            t_pipeline.set_from(3477061000000091093)
            t_pipeline.set_to(3477061000000006801)
            transfer_pipeline.set_pipeline(t_pipeline)

            stages_list = []

            stage = Stages()
            stage.set_from(3477061000000091097)
            stage.set_to(3477061000000006803)
            stages_list.append(stage)

            stage2 = Stages()
            stage2.set_from(3477061000000091099)
            stage2.set_to(3477061000000006805)
            stages_list.append(stage2)

            transfer_pipeline.set_stages(stages_list)
            transfer_pipeline_list.append(transfer_pipeline)
            request.set_transfer_pipeline(transfer_pipeline_list)

            response = pipeline_operations.transfer_pipelines(request)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, TransferPipelineActionWrapper):
                        action_response_list = response_object.get_transfer_pipeline()
                        for action_response in action_response_list:
                            if isinstance(action_response, TransferPipelineSuccessResponse):
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
            print("Exception when calling transfer_pipelines: " + str(e))


TransferPipelines.initialize()
TransferPipelines.transfer_pipelines(layout_id=1055806000000091023)
