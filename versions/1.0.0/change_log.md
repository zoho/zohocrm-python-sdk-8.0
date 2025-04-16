# Migrating from Zoho CRM PYTHON SDK 7.0-v4.0.0 to 8.0-v1.0.0

1. [Attachments](#attachments)
   - [Get Attachments](#get-attachments)

2. [ConversionOptions](#conversionOptions)
   - [LeadConversionOptions](#leadconversionoptions)

3. [Fields](#fields)
   - [Get Fields](#get-fields)
   
4. [Layouts](#layouts)
   - [Get Layouts](#get-layouts)

5. [Notification](#notification)
   - [Disable Notification](#disable-notification)
   
6. [ZiaOrgEnrichment](#ziaOrgEnrichment)
    - [Create ZiaOrgEnrichment](#create-ziaorgenrichment)
    - [Get ZiaOrgEnrichment](#get-ziaorgenrichment)
    - [Get ZiaOrgEnrichments](#get-ziaorgenrichments)

7. [ZiaPeopleEnrichment](#ziaPeopleEnrichment)
   - [Create ZiaPeopleEnrichment](#create-ziapeopleenrichment)
   - [Get ZiaPeopleEnrichment](#get-ziapeopleenrichment)
   - [Get ZiaPeopleEnrichments](#get-ziapeopleenrichments)
   
8. [FromAddresses](#fromAddresses)
   - [Get EmailAddresses](#get-emailaddresses)

9. [EmailSharingDetails](#emailSharingDetails)
   - [Get EmailSharingDetails](#get-emailsharingdetails)

10. [Profile](#profile)
    - [Get Profiles](#get-profiles)

11. [EnrollCadences](#enrollCadences)
    - [EnrollCadences](#enrolcadenced)
    - [UnenrollCadences](#unenrollCadences)

12. [ScoringRules](#scoringrules)
    - [Get ScoringRule](#get-scoringrule)

13. [Tags](#tags)
    - [AddTagsToRecord](#addtagstorecord)
    - [RemoveTagsFromRecord](#removetagsfromrecord)
   
## Attachments

### Get Attachments

- Changes Note : Introduced record_status__s, attachment_source__s, file_id__s, field_states and zia_visions fields in Attachment class  

- PYTHON SDK 7.0-v4.0.0

    ```python
    attachments_list = response_object.get_data()
    for attachment in attachments_list:
    print('Attachment ID : ' + str(attachment.get_id()))
    ```
  
- PYTHON SDK 8.0-v1.0.0

    ```python
    attachments_list = response_object.get_data()
    for attachment in attachments_list:
        print("Attachment ID: " + attachment.get_id())
        print("Attachment File States: " + attachment.get_field_states())
        print("Attachment RecordStatusS: " + attachment.get_record_status__s())
        print("Attachment ZiaVisions: " + attachment.get_zia_visions())
        print("Attachment FileIds: " + attachment.get_file_id__s())
        print("Attachment AttachmentSourceS: " + attachment.get_attachment_source__s())
    ```
  
## ConversionOptions

### LeadConversionOptions

- Changes Note: method name updated from get_conversionoptions to get_conversion_options in ResponseWrapper

- PYTHON SDK 7.0-v4.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        conversion_option = response_handler.get_conversionoptions()
    ```
- PYTHON SDK 8.0-v1.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        conversion_option = response_handler.get_conversion_options()
    ```

## Fields

### Get Fields

- Changes Note : New fields[linking_details, connected_details, related_list] introduced in MultiSelectLookup and fields[display_label, linking_module, lookup_apiname, api_name, connectedlookup_apiname, id, connected_module] are removed.

- PYTHON SDK 7.0-v4.0.0

    ```python
    # get multi select lookup for field
    multi_select_lookup = field.get_multiselectlookup()
    if multi_select_lookup is not None:
        print("Field MultiSelectLookup DisplayLabel: " + multi_select_lookup.get_display_label())
        print("Field MultiSelectLookup LinkingModule: " + multi_select_lookup.get_linking_module())
        print("Field MultiSelectLookup LookupApiname: " + multi_select_lookup.get_lookup_apiname())
        print("Field MultiSelectLookup APIName: " + multi_select_lookup.get_api_name())
        print("Field MultiSelectLookup ConnectedlookupApiname: " + multi_select_lookup.get_connectedlookup_apiname())
        print("Field MultiSelectLookup ID: " + multi_select_lookup.get_id())
        print("Field MultiSelectLookup ConnectedModule: " + multi_select_lookup.get_connected_module())
    # get multi user lookup for field
    if multi_select_lookup is not None:
        multi_user_lookup = field.get_multiuserlookup()
        print("Field MultiUserLookup DisplayLabel" + multi_user_lookup.get_display_label())
        print("Field MultiUserLookup LinkingModule" + multi_user_lookup.get_linking_module())
        print("Field MultiUserLookup LookupApiname" + multi_user_lookup.get_lookup_apiname())
        print("Field MultiUserLookup APIName" + multi_user_lookup.get_api_name())
        print("Field MultiUserLookup ID" + multi_user_lookup.get_id())
        print("Field MultiUserLookup ConnectedModule" + multi_user_lookup.get_connected_module())
        print("Field MultiUserLookup ConnectedlookupApiname" + multi_user_lookup.get_connectedlookup_apiname())
    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    # get the multi select lookup for field
    multi_select_lookup = field.get_multiselectlookup()
    if multi_select_lookup is not None:
        linking_details = multi_select_lookup.get_linking_details()
        if linking_details is not None:
            module = linking_details.get_module()
            if module is not None:
                print("Field Multiselectlookup LinkingDetails Module Visibility: ",  module.get_visibility())
                print("Field Multiselectlookup LinkingDetails Module PluralLabel: ",  module.get_plural_label())
                print("Field Multiselectlookup LinkingDetails Module APIName: ",  module.get_api_name())
                print("Field Multiselectlookup LinkingDetails Module Id: ",  module.get_id())

            lookup_field = linking_details.get_lookup_field()
            if lookup_field is not None:
                print("Field MultiSelectLookup LinkingDetails LookupField APIName: ",  lookup_field.get_api_name())
                print("Field MultiSelectLookup LinkingDetails LookupField FieldLabel: ", lookup_field.get_field_label())
                print("Field MultiSelectLookup LinkingDetails LookupField Id: ",  lookup_field.get_id())
  
            connected_lookup_field = linking_details.get_connected_lookup_field()
            if connected_lookup_field is not None:
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField APIName: ", connected_lookup_field.get_api_name())
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField FieldLabel: ", connected_lookup_field.get_field_label())
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField Id: ", connected_lookup_field.get_id())

        connected_details = multi_select_lookup.get_connected_details()
        if connected_details is not None:
            connection_field = connected_details.get_field()
            if connection_field is not None:
                print("Field Multiselectlookup ConnectedDetails Field APIName: ", connection_field.get_api_name())
                print("Field Multiselectlookup ConnectedDetails Field FieldLabel: ", connection_field.get_field_label())
                print("Field Multiselectlookup ConnectedDetails Field id: ", connection_field.get_id())

            connected_module = connected_details.get_module()
            if connected_module is not None:
                print("Field MultiSelectLookup ConnectedDetails Module PluralLabel: ", connected_module.get_plural_label())
                print("Field MultiSelectLookup ConnectedDetails Module APIName: ", connected_module.get_api_name())
                print("Field MultiSelectLookup ConnectedDetails Module Id: ", connected_module.get_id())

            layouts = connected_details.get_layouts()
            if layouts is not None and len(layouts) > 0:
                for layout in layouts:
                    print("Field MultiSelectLookup ConnectedDetails Layouts APIName: ", layout.get_api_name())
                    print("Field MultiSelectLookup ConnectedDetails Layouts Id: ", layout.get_id())

        related_list = multi_select_lookup.get_related_list()
        if related_list is not None:
            print("Field MultiSelectLookup RelatedList DisplayLabel: ", related_list.get_display_label())
            print("Field MultiSelectLookup RelatedList APIName: ", related_list.get_api_name())
            print("Field MultiSelectLookup RelatedList Id: ", related_list.get_id())
  
  # get the multi user lookup for field
  if field.get_multiuserlookup is not None:
    multiuserlookup =  field.get_multiuserlookup()
    if multiuserlookup is not None:
        linkingDetails =  multiuserlookup.get_linking-details()
        if linking_details:
            module =  linking_details.get_module()
            if module is not None:
                print("Field Multiuserlookup LinkingDetails Module Visibility: ",  module.get_visibility())
                print("Field Multiuserlookup LinkingDetails Module PluralLabel: ",  module.get_plural_label())
                print("Field Multiuserlookup LinkingDetails Module APIName: ",  module.get_api_name())
                print("Field Multiuserlookup LinkingDetails Module Id: ",  module.get_id())
        
            lookup_field = linking_details.get_lookup_field()
            if lookup_field is not None:
                print("Field Multiuserlookup LinkingDetails LookupField APIName: ",  lookup_field.get_api_name())
                print("Field Multiuserlookup LinkingDetails LookupField FieldLabel: ",  lookup_field.get_field_label())
                print("Field Multiuserlookup LinkingDetails LookupField Id: ", lookup_field.get_id())

            connected_lookup_field = linking_details.get_connected_lookup_field()
            if connected_lookup_field is not None:
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField APIName: ",  connected_lookup_field.get_api_name())
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField FieldLabel: ",  connected_lookup_field.get_field_label())
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField Id: ", connected_lookup_field.get_id())

        print("Field Multiuserlookup RecordAccess: ", multiuserlookup.get_record_access())
  ```

## Layouts

### Get Layouts

- Changes Note : Updated get_defaultview method name to get_default_view and introduced new fields in MutliSelectLookup.

- PYTHON SDK 7.0-v4.0.0

    ```python
    layouts = response_object.get_layouts()
    for layout in layouts: 
        profiles = layout.get_profiles()
        if profiles is not None:
            for profile in profiles:
                default_view = profile.get_defaultview()
    
    # get multi select lookup for field
    multi_select_lookup = field.get_multiselectlookup()
    if multi_select_lookup is not None:
        print("Field MultiSelectLookup DisplayLabel: " + multi_select_lookup.get_display_label())
        print("Field MultiSelectLookup LinkingModule: " + multi_select_lookup.get_linking_module())
        print("Field MultiSelectLookup LookupApiname: " + multi_select_lookup.get_lookup_apiname())
        print("Field MultiSelectLookup APIName: " + multi_select_lookup.get_api_name())
        print("Field MultiSelectLookup ConnectedlookupApiname: " + multi_select_lookup.get_connectedlookup_apiname())
        print("Field MultiSelectLookup ID: " + multi_select_lookup.get_id())
        print("Field MultiSelectLookup ConnectedModule: " + multi_select_lookup.get_connected_module())
    # get multi user lookup for field
    if multi_select_lookup is not None:
        multi_user_lookup = field.get_multiuserlookup()
        print("Field MultiUserLookup DisplayLabel" + multi_user_lookup.get_display_label())
        print("Field MultiUserLookup LinkingModule" + multi_user_lookup.get_linking_module())
        print("Field MultiUserLookup LookupApiname" + multi_user_lookup.get_lookup_apiname())
        print("Field MultiUserLookup APIName" + multi_user_lookup.get_api_name())
        print("Field MultiUserLookup ID" + multi_user_lookup.get_id())
        print("Field MultiUserLookup ConnectedModule" + multi_user_lookup.get_connected_module())
        print("Field MultiUserLookup ConnectedlookupApiname" + multi_user_lookup.get_connectedlookup_apiname())
    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    layouts = response_object.get_layouts()
    for layout in layouts:
        profiles = layout.get_profiles()
        if profiles is not None:
             for profile in profiles:
                default_view = profile.get_default_view()
            
    # get the multi select lookup for field
    multi_select_lookup = field.get_multiselectlookup()
    if multi_select_lookup is not None:
        linking_details = multi_select_lookup.get_linking_details()
        if linking_details is not None:
            module = linking_details.get_module()
            if module is not None:
                print("Field Multiselectlookup LinkingDetails Module Visibility: ",  module.get_visibility())
                print("Field Multiselectlookup LinkingDetails Module PluralLabel: ",  module.get_plural_label())
                print("Field Multiselectlookup LinkingDetails Module APIName: ",  module.get_api_name())
                print("Field Multiselectlookup LinkingDetails Module Id: ",  module.get_id())

            lookup_field = linking_details.get_lookup_field()
            if lookup_field is not None:
                print("Field MultiSelectLookup LinkingDetails LookupField APIName: ",  lookup_field.get_api_name())
                print("Field MultiSelectLookup LinkingDetails LookupField FieldLabel: ", lookup_field.get_field_label())
                print("Field MultiSelectLookup LinkingDetails LookupField Id: ",  lookup_field.get_id())
  
            connected_lookup_field = linking_details.get_connected_lookup_field()
            if connected_lookup_field is not None:
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField APIName: ", connected_lookup_field.get_api_name())
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField FieldLabel: ", connected_lookup_field.get_field_label())
                print("Field MultiSelectLookup LinkingDetails ConnectedLookupField Id: ", connected_lookup_field.get_id())

        connected_details = multi_select_lookup.get_connected_details()
        if connected_details is not None:
            connection_field = connected_details.get_field()
            if connection_field is not None:
                print("Field Multiselectlookup ConnectedDetails Field APIName: ", connection_field.get_api_name())
                print("Field Multiselectlookup ConnectedDetails Field FieldLabel: ", connection_field.get_field_label())
                print("Field Multiselectlookup ConnectedDetails Field id: ", connection_field.get_id())

            connected_module = connected_details.get_module()
            if connected_module is not None:
                print("Field MultiSelectLookup ConnectedDetails Module PluralLabel: ", connected_module.get_plural_label())
                print("Field MultiSelectLookup ConnectedDetails Module APIName: ", connected_module.get_api_name())
                print("Field MultiSelectLookup ConnectedDetails Module Id: ", connected_module.get_id())

            layouts = connected_details.get_layouts()
            if layouts is not None and len(layouts) > 0:
                for layout in layouts:
                    print("Field MultiSelectLookup ConnectedDetails Layouts APIName: ", layout.get_api_name())
                    print("Field MultiSelectLookup ConnectedDetails Layouts Id: ", layout.get_id())

        related_list = multi_select_lookup.get_related_list()
        if related_list is not None:
            print("Field MultiSelectLookup RelatedList DisplayLabel: ", related_list.get_display_label())
            print("Field MultiSelectLookup RelatedList APIName: ", related_list.get_api_name())
            print("Field MultiSelectLookup RelatedList Id: ", related_list.get_id())
  
  # get the multi user lookup for field
  if field.get_multiuserlookup is not None:
    multiuserlookup =  field.get_multiuserlookup()
    if multiuserlookup is not None:
        linkingDetails =  multiuserlookup.get_linking-details()
        if linking_details:
            module =  linking_details.get_module()
            if module is not None:
                print("Field Multiuserlookup LinkingDetails Module Visibility: ",  module.get_visibility())
                print("Field Multiuserlookup LinkingDetails Module PluralLabel: ",  module.get_plural_label())
                print("Field Multiuserlookup LinkingDetails Module APIName: ",  module.get_api_name())
                print("Field Multiuserlookup LinkingDetails Module Id: ",  module.get_id())
        
            lookup_field = linking_details.get_lookup_field()
            if lookup_field is not None:
                print("Field Multiuserlookup LinkingDetails LookupField APIName: ",  lookup_field.get_api_name())
                print("Field Multiuserlookup LinkingDetails LookupField FieldLabel: ",  lookup_field.get_field_label())
                print("Field Multiuserlookup LinkingDetails LookupField Id: ", lookup_field.get_id())

            connected_lookup_field = linking_details.get_connected_lookup_field()
            if connected_lookup_field is not None:
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField APIName: ",  connected_lookup_field.get_api_name())
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField FieldLabel: ",  connected_lookup_field.get_field_label())
                print("Field Multiuserlookup LinkingDetails ConnectedLookupField Id: ", connected_lookup_field.get_id())

        print("Field Multiuserlookup RecordAccess: ", multiuserlookup.get_record_access())
    ```
    
## Notification

### Disable Notification

- Changes Note: Updated set_deleteevents method name to set_delete_events.

- PYTHON SDK 7.0-v4.0.0

    ```python
    notification = Notification()
    notification.set_channel_id("1006800211")
    events = ["Deals.edit"]
    notification.set_events(events)
    notification.set_deleteevents(Choice(True))    
    ```
- PYTHON SDK 8.0-v1.0.0

    ```python
    notification = Notification()
    notification.set_channel_id("1006800211")
    events = ["Deals.edit"]
    notification.set_events(events)
    notification.set_delete_events(Choice(True))     
    ```

## ZiaOrgEnrichment

### Create ZiaOrgEnrichment

- Changes Note: Updated set_ziaorgenrichment and get_ziaorgenrichment method names to set_zia_org_enrichment and get_zia_org_enrichment respectively.

- PYTHON SDK 7.0-v4.0.0
    ```python
    request = BodyWrapper()
    request.set_ziaorgenrichment(ziaorgenrichment)
    param_instance = ParameterMap()
    param_instance.add(CreateZiaOrgEnrichmentParam.module, "Vendors")
    response = zia_org_enrichment_operations.create_zia_org_enrichment(request, param_instance)
    if response is not None:
        response_object = response.get_object()
        if response_object is not None:
            if isinstance(response_object, ActionWrapper):
                action_responses = response_object.get_ziaorgenrichment()
    ```
- PYTHON SDK 8.0-v1.0.0
    ```python
    request = BodyWrapper()
    request.set_zia_org_enrichment(ziaorgenrichment)
    param_instance = ParameterMap()
    param_instance.add(CreateZiaOrgEnrichmentParam.module, "Vendors")
    response = zia_org_enrichment_operations.create_zia_org_enrichment(request, param_instance)
    if response is not None:
        response_object = response.get_object()
        if response_object is not None:
            if isinstance(response_object, ActionWrapper):
                action_responses = response_object.get_zia_org_enrichment()
    ```

### Get ZiaOrgEnrichment

- Changes Note: Updated get_ziaorgenrichment method name to get_zia_org_enrichment.

- PYTHON SDK 7.0-v4.0.0
    ```python
    zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
    response = zia_org_enrichment_operations.get_zia_org_enrichment(zia_org_enrichment_id)
    response_object = response.get_object()
    if response_object is not None: 
        if isinstance(response_object, ResponseWrapper):
            ziaorgenrichment = response_object.get_ziaorgenrichment()

    ```
- PYTHON SDK 8.0-v1.0.0
    
    ```python
    zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
    response = zia_org_enrichment_operations.get_zia_org_enrichment(zia_org_enrichment_id)
    response_object = response.get_object()
    if response_object is not None: 
        if isinstance(response_object, ResponseWrapper):
            ziaorgenrichment = response_object.get_zia_org_enrichment()

    ```
  
### Get ZiaOrgEnrichments

- Changes Note: Updated get_ziaorgenrichment method name to get_zia_org_enrichment.

- PYTHON SDK 7.0-v4.0.0
    ```python
    zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
    param_instance = ParameterMap()
    response = zia_org_enrichment_operations.get_zia_org_enrichments(param_instance)
    response_object = response.get_object()
    if response_object is not None: 
        if isinstance(response_object, ResponseWrapper):
            ziaorgenrichment = response_object.get_ziaorgenrichment()

    ```
- PYTHON SDK 8.0-v1.0.0
    ```python
    zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
    param_instance = ParameterMap()
    response = zia_org_enrichment_operations.get_zia_org_enrichments(param_instance)
    response_object = response.get_object()
    if response_object is not None: 
        if isinstance(response_object, ResponseWrapper):
            ziaorgenrichment = response_object.get_zia_org_enrichment()

   ```
  
## ZiaPeopleEnrichment

### Create ZiaPeopleEnrichment

- Changes Note : Updated set_ziapeopleenrichment and get_ziapeopleenrichment methods name to set_zia_people_enrichment and get_zia_people_enrichment respectively.

- PYTHON SDK 7.0-v4.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    request =  BodyWrapper()
    request.set_ziapeopleenrichment(ziapeopleenrichment)
		param_instance = ParameterMap()
		param_instance.add(CreateZiaPeopleEnrichmentParam.module, "TestSDK12")
	    response = zia_people_enrichment_operations.create_zia_people_enrichment(request, param_instance)
		if response is not None:
			response_object = response.get_object()
			if response_object is not None:
				if isinstance(response_object, ActionWrapper) :
					action_responses = response_object.get_ziapeopleenrichment()
    ```

- PYTHON SDK 8.0-v1.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    request =  BodyWrapper()
    request.set_zia_people_enrichment(ziapeopleenrichment)
		param_instance = ParameterMap()
		param_instance.add(CreateZiaPeopleEnrichmentParam.module, "TestSDK12")
	    response = zia_people_enrichment_operations.create_zia_people_enrichment(request, param_instance)
		if response is not None:
			response_object = response.get_object()
			if response_object is not None:
				if isinstance(response_object, ActionWrapper) :
					action_responses = response_object.get_zia_people_enrichment()
    ```
  
### Get ZiaPeopleEnrichment

- Changes Note : Updated get_ziapeopleenrichment method name to get_zia_people_enrichment.

- PYTHON SDK 7.0-v4.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    response = zia_people_enrichment_operations.get_zia_people_enrichment(zia_people_enrichment_id)
    responseObject = response.get_object()
        if responseObject is not None :
            if isinstance(responseObject, ResponseWrapper):
                ziapeopleenrichment = responseObject.get_ziapeopleenrichment()
      
    ```

- PYTHON SDK 8.0-v1.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    response = zia_people_enrichment_operations.get_zia_people_enrichment(zia_people_enrichment_id)
    responseObject = response.get_object()
        if responseObject is not None :
            if isinstance(responseObject, ResponseWrapper):
                ziapeopleenrichment = responseObject.get_zia_people_enrichment()
      
    ```

### Get ZiaPeopleEnrichments

- Changes Note : Updated get_ziapeopleenrichment method name to get_zia_people_enrichment.

- PYTHON SDK 7.0-v4.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    param_instance = ParameterMap()
    response = zia_people_enrichment_operations.get_zia_people_enrichments(param_instance)
    responseObject = response.get_object()
    if responseObject is not None :
        if isinstance(responseObject, ResponseWrapper):
            ziapeopleenrichment = responseObject.get_ziapeopleenrichment()
      
    ```

- PYTHON SDK 8.0-v1.0.0
    ```python
    zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
    param_instance = ParameterMap()
    response = zia_people_enrichment_operations.get_zia_people_enrichments(param_instance)
    responseObject = response.get_object()
    if responseObject is not None :
        if isinstance(responseObject, ResponseWrapper):
            ziapeopleenrichment = responseObject.get_zia_people_enrichment()
      
    ```
  
## FromAddresses

### Get EmailAddresses

- Changes Note: Introduced new param user_id in get_email_addresses method.

- PYTHON SDK 7.0-v4.0.0
    ```python
    class FromAddresses :
        @staticmethod
        def get_email_addresses():
            send_mail_operations = FromAddressesOperations()
        
    FromAddresses.getEmailAddresses()
    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    class FromAddresses:
        @staticmethod
        def get_email_addresses(user_id):
            send_mail_operations = FromAddressesOperations(user_id)
        
    user_id = 323132312312
    FromAddresses.getEmailAddresses(user_id)
    ```

## EmailSharingDetails

### Get EmailSharingDetails

- Changes Note : Updated get_emailssharingdetails method name to get_emails_sharing_details.

- PYTHON SDK 7.0-v4.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        response_wrapper = response_handler
        email_sharing_details = response_wrapper.get_emailssharingdetails()

    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        response_wrapper = response_handler
        email_sharing_details = response_wrapper.get_emails_sharing_details()

    ```

## Profile

### Get Profiles

- Changes Note : Updated get_defaultview method name to get_default_view

- PYTHON SDK 7.0-v4.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        response_wrapper = response_handler
        profiles = response_wrapper.get_profiles()
        for profile in profiles:
            default_view = profile.get_defaultview()

    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    response_handler = response.get_object()
    if isinstance(response_handler, ResponseWrapper):
        response_wrapper = response_handler
        profiles = response_wrapper.get_profiles()
        for profile in profiles:
            default_view = profile.get_default_view()

    ```

## EnrollCadences

### EnrollCadences

- Changes Note: Updated EnrolCadences to EnrollCadences and enrol_cadences method name to enroll_cadences.

- PYTHON SDK 7.0-v4.0.0

    ```python
    class EnrolCadences:
        @staticmethod
        def enrolCadences(module_api_name):
            response = cadences_execution_operations.enrol_cadences(module_api_name, request)

    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    class EnrollCadences:
        @staticmethod
        def enrolCadences(module_api_name):
            response = cadences_execution_operations.enroll_cadences(module_api_name, request)

    ```

### UnenrollCadences

- Changes Note: Updated UnenrolCadences to UnenrollCadences and unenrol_cadences method name to unenroll_cadences.

- PYTHON SDK 7.0-v4.0.0

    ```python
    class UnenrolCadences:
        @staticmethod
        def enrolCadences(module_api_name) :
            response = cadences_execution_operations.unenrol_cadences(module_api_name, request)

    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    class UnenrollCadences:
        @staticmethod
        def enrolCadences(module_api_name) :
            response = cadences_execution_operations.unenroll_cadences(module_api_name, request)

    ```

## ScoringRules

### Get ScoringRule

- Changes Note : module param removed in get_scoring_rule method

- PYTHON SDK 7.0-v4.0.0

    ```python
    @staticmethod
    def get_scoring_rule(module, id) :
        scoring_rules_operations = ScoringRulesOperations()
        param_instance = ParameterMap()
        response = scoring_rules_operations.get_scoring_rule(module, id, param_instance) 

    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    @staticmethod
    def get_scoring_rule(id) :
        scoring_rules_operations = ScoringRulesOperations()
        param_instance = ParameterMap()
        response = scoring_rules_operations.get_scoring_rule(id, param_instance) 

    ```

## Tags

### AddTagsToRecord

- Changes Note : location swap of record_id and module_api_name params

- PYTHON SDK 7.0-v4.0.0

    ```python
    tags_operations = TagsOperations()
    response = tags_operations.add_tags(record_id, module_api_name, request, param_instance)
    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    tags_operations = TagsOperations()
    response = tags_operations.add_tags(module_api_name, record_id, request, param_instance)
    ```

### RemoveTagsFromRecord

- Changes Note : location swap of record_id and module_api_name params

- PYTHON SDK 7.0-v4.0.0

    ```python
    tags_operations = TagsOperations()
    response = tags_operations.remove_tags(record_id, module_api_name, request)
    ```

- PYTHON SDK 8.0-v1.0.0

    ```python
    tags_operations = TagsOperations()
    response = tags_operations.remove_tags(module_api_name, record_id, request)
    ```


  
