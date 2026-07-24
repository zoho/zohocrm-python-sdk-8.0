from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.notes import NotesOperations, GetNoteParam, GetNoteHeader
from zohocrmsdk.src.com.zoho.crm.api.notes import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from datetime import datetime


class GetNote:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_note(note_id):
        try:
            notes_operations = NotesOperations()
            param_instance = ParameterMap()
            # param_instance.add(GetNoteParam.fields, "Note_Title,Note_Content")
            
            header_instance = HeaderMap()
            header_instance.add(GetNoteHeader.if_modified_since, datetime(2020, 1, 1, 10, 0, 0))
            
            response = notes_operations.get_note(note_id, param_instance, header_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        notes_list = response_object.get_data()
                        for note in notes_list:
                            print("Note ID: " + str(note.get_id()))
                            print("Note Title: " + str(note.get_note_title()))
                            print("Note Content: " + str(note.get_note_content()))
                            print("Note Created Time: " + str(note.get_created_time()))
                            print("Note Modified Time: " + str(note.get_modified_time()))
                            if note.get_created_by() is not None:
                                print("Created By: " + str(note.get_created_by().get_name()))
                            if note.get_modified_by() is not None:
                                print("Modified By: " + str(note.get_modified_by().get_name()))
                            if note.get_parent_id() is not None:
                                print("Parent ID: " + str(note.get_parent_id().get_id()))
                            print("Note Size: " + str(note.get_size()))
                            print("Note Editable: " + str(note.get_editable()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_note: " + str(e))


GetNote.initialize()
GetNote.get_note(1055806000009296005)