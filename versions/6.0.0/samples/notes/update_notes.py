from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.notes import NotesOperations, BodyWrapper, Note
from zohocrmsdk.src.com.zoho.crm.api.notes import ActionWrapper, APIException,SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class UpdateNotes:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_notes():
        try:
            notes_operations = NotesOperations()
            request = BodyWrapper()
            notes_list = []
            
            # First note
            note1 = Note()
            note1.set_id(1055806000028568001)
            note1.set_note_title("Updated Bulk Note 1")
            note1.set_note_content("Updated bulk note content 1")
            notes_list.append(note1)
            
            # Second note
            note2 = Note()
            note2.set_id(1055806000028209028)
            note2.set_note_title("Updated Bulk Note 2")
            note2.set_note_content("Updated bulk note content 2")
            notes_list.append(note2)
            
            request.set_data(notes_list)
            
            response = notes_operations.update_notes(request)
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
            print("Exception when calling update_notes: " + str(e))


UpdateNotes.initialize()
UpdateNotes.update_notes()