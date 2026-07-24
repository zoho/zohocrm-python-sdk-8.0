from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.pipeline import PipelineOperations, ResponseWrapper, APIException


class GetPipeline:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_pipeline(layout_id, pipeline_id):
        """
        This method is used to get a single pipeline for a layout and print the response.
        :param layout_id: The ID of the layout
        :param pipeline_id: The ID of the pipeline
        """
        try:
            pipeline_operations = PipelineOperations(layout_id)
            response = pipeline_operations.get_pipeline(pipeline_id)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        pipeline_list = response_object.get_pipeline()
                        for pipeline in pipeline_list:
                            print("Pipeline ID: " + str(pipeline.get_id()))
                            print("Pipeline DisplayValue: " + str(pipeline.get_display_value()))
                            print("Pipeline ActualValue: " + str(pipeline.get_actual_value()))
                            print("Pipeline Default: " + str(pipeline.get_default()))
                            print("Pipeline ChildAvailable: " + str(pipeline.get_child_available()))
                            parent = pipeline.get_parent()
                            if parent is not None:
                                print("Pipeline Parent ID: " + str(parent.get_id()))
                            maps = pipeline.get_maps()
                            if maps is not None:
                                for stage in maps:
                                    print("Stage ID: " + str(stage.get_id()))
                                    print("Stage DisplayValue: " + str(stage.get_display_value()))
                                    print("Stage ActualValue: " + str(stage.get_actual_value()))
                                    print("Stage SequenceNumber: " + str(stage.get_sequence_number()))
                                    print("Stage Delete: " + str(stage.get_delete()))
                                    print("Stage ColourCode: " + str(stage.get_colour_code()))
                                    print("Stage ForecastType: " + str(stage.get_forecast_type()))
                                    forecast_category = stage.get_forecast_category()
                                    if forecast_category is not None:
                                        print("Stage ForecastCategory Name: " + str(forecast_category.get_name()))
                                        print("Stage ForecastCategory ID: " + str(forecast_category.get_id()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_pipeline: " + str(e))


GetPipeline.initialize()
GetPipeline.get_pipeline(layout_id=1055806000000091023, pipeline_id=1055806000029084005)
