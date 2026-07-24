from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.features.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.features.features_operations import FeaturesOperations
from zohocrmsdk.src.com.zoho.crm.api.features.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class GetDataEnrichment:
    @staticmethod
    def get_data_enrichment():
        features_operations = FeaturesOperations()
        response = features_operations.get_data_enrichment()

        if response is not None:
            print("Status Code:", response.get_status_code())

            if response.get_status_code() in [204, 304]:
                print("No Content" if response.get_status_code() == 204 else "Not Modified")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                features = response_wrapper.get_features()

                if features is not None:
                    for feature in features:
                        components = feature.get_components()

                        if components is not None:
                            for component in components:
                                print("Feature Component APIName:", component.get_api_name())
                                print("Feature Component ModuleSupported:", component.get_module_supported())

                                detail = component.get_details()
                                if detail is not None:
                                    limit = detail.get_limits()
                                    if limit is not None:
                                        print("Feature Component Detail Limit EditionLimit:", limit.get_edition_limit())
                                        print("Feature Component Detail Limit Total:", limit.get_total())

                                    used_count = detail.get_used_count()
                                    if used_count is not None:
                                        print("Feature Component Detail UsedCount EditionLimit:",
                                              used_count.get_edition_limit())
                                        print("Feature Component Detail UsedCount Total:", used_count.get_total())

                                print("Feature Component FeatureLabel:", component.get_feature_label())

                        print("Feature APIName:", feature.get_api_name())

                        parent_feature = feature.get_parent_feature()
                        if parent_feature is not None:
                            print("Feature ParentFeature APIName:", parent_feature.get_api_name())

                        print("Feature ModuleSupported:", feature.get_module_supported())

                        detail = feature.get_details()
                        if detail is not None:
                            limit = detail.get_limits()
                            if limit is not None:
                                print("Feature Detail Limit EditionLimit:", limit.get_edition_limit())
                                print("Feature Detail Limit Total:", limit.get_total())

                            used_count = detail.get_used_count()
                            if used_count is not None:
                                print("Feature Component Detail UsedCount EditionLimit:",
                                      used_count.get_edition_limit())
                                print("Feature Component Detail UsedCount Total:", used_count.get_total())

                        print("Feature FeatureLabel:", feature.get_feature_label())

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status:", exception.get_status().get_value())
                print("Code:", exception.get_code().get_value())
                print("Details:")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print("Message:", exception.get_message())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


GetDataEnrichment.initialize()
GetDataEnrichment.get_data_enrichment()
