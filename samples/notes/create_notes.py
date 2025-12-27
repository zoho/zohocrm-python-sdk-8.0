from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.notes import NotesOperations, BodyWrapper, Note, ParentId,SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.notes import ActionWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.modules.minified_module import MinifiedModule


class CreateNotes:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_notes():
        try:
            notes_operations = NotesOperations()
            request = BodyWrapper()
            notes_list = []
            note = Note()
            note.set_note_title("Sample Note Title")
            note.set_note_content("Sample note content for testing purposes")
            
            parent_record = ParentId()
            parent_record.set_id(1055806000005844005)
            module = MinifiedModule()
            module.set_id(1055806000000002175)
            module.set_api_name("Leads")
            parent_record.set_module(module)
            note.set_parent_id(parent_record)
            
            notes_list.append(note)
            request.set_data(notes_list)
            
            response = notes_operations.create_notes(request)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
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
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling create_notes: " + str(e))


CreateNotes.initialize()
CreateNotes.create_notes()