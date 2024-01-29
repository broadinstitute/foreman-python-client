# pyforeman.RegistrationCommandsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_registration_commands**](RegistrationCommandsApi.md#post_registration_commands) | **POST** /registration_commands | Generate global registration command


# **post_registration_commands**
> post_registration_commands(location_id=location_id, organization_id=organization_id, registration_command_organization_id=registration_command_organization_id, registration_command_location_id=registration_command_location_id, registration_command_hostgroup_id=registration_command_hostgroup_id, registration_command_operatingsystem_id=registration_command_operatingsystem_id, registration_command_smart_proxy_id=registration_command_smart_proxy_id, registration_command_setup_insights=registration_command_setup_insights, registration_command_setup_remote_execution=registration_command_setup_remote_execution, registration_command_jwt_expiration=registration_command_jwt_expiration, registration_command_insecure=registration_command_insecure, registration_command_packages=registration_command_packages, registration_command_update_packages=registration_command_update_packages, registration_command_repo=registration_command_repo, registration_command_repo_gpg_key_url=registration_command_repo_gpg_key_url, registration_command_remote_execution_interface=registration_command_remote_execution_interface, registration_command_setup_remote_execution_pull=registration_command_setup_remote_execution_pull, registration_command_activation_key=registration_command_activation_key, registration_command_activation_keys=registration_command_activation_keys, registration_command_lifecycle_environment_id=registration_command_lifecycle_environment_id, registration_command_force=registration_command_force, registration_command_ignore_subman_errors=registration_command_ignore_subman_errors)

Generate global registration command



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RegistrationCommandsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
registration_command_organization_id = 8.14 # float | ID of the Organization to register the host in (optional)
registration_command_location_id = 8.14 # float | ID of the Location to register the host in (optional)
registration_command_hostgroup_id = 8.14 # float | ID of the Host group to register the host in (optional)
registration_command_operatingsystem_id = 8.14 # float | ID of the Operating System to register the host in. Operating system must have a `host_init_config` template assigned (optional)
registration_command_smart_proxy_id = 8.14 # float | ID of the Smart Proxy. This Proxy must have enabled both the 'Templates' and 'Registration' features (optional)
registration_command_setup_insights = true # bool | Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems (optional)
registration_command_setup_remote_execution = true # bool | Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host (optional)
registration_command_jwt_expiration = 8.14 # float | Expiration of the authorization token (in hours) (optional)
registration_command_insecure = true # bool | Enable insecure argument for the initial curl (optional)
registration_command_packages = 'registration_command_packages_example' # str | Packages to install on the host when registered. Can be set by `host_packages` parameter, example: `pkg1 pkg2` (optional)
registration_command_update_packages = true # bool | Update all packages on the host (optional)
registration_command_repo = 'registration_command_repo_example' # str | Repository URL / details, for example for Debian OS family: 'deb http://deb.example.com/ buster 1.0', for Red Hat and SUSE OS family: 'http://yum.theforeman.org/client/latest/el8/x86_64/' (optional)
registration_command_repo_gpg_key_url = 'registration_command_repo_gpg_key_url_example' # str | URL of the GPG key for the repository (optional)
registration_command_remote_execution_interface = 'registration_command_remote_execution_interface_example' # str | Identifier of the Host interface for Remote execution (optional)
registration_command_setup_remote_execution_pull = true # bool | Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host (optional)
registration_command_activation_key = 'registration_command_activation_key_example' # str | Activation key for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. For multiple keys use `activation_keys` param instead. (optional)
registration_command_activation_keys = ['registration_command_activation_keys_example'] # list[str] | Activation keys for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. Required only if host group has no activation keys. (optional)
registration_command_lifecycle_environment_id = 8.14 # float | Lifecycle environment for the host. (optional)
registration_command_force = true # bool | Clear any previous registration and run subscription-manager with --force. (optional)
registration_command_ignore_subman_errors = true # bool | Ignore subscription-manager errors for `subscription-manager register` command (optional)

try:
    # Generate global registration command
    api_instance.post_registration_commands(location_id=location_id, organization_id=organization_id, registration_command_organization_id=registration_command_organization_id, registration_command_location_id=registration_command_location_id, registration_command_hostgroup_id=registration_command_hostgroup_id, registration_command_operatingsystem_id=registration_command_operatingsystem_id, registration_command_smart_proxy_id=registration_command_smart_proxy_id, registration_command_setup_insights=registration_command_setup_insights, registration_command_setup_remote_execution=registration_command_setup_remote_execution, registration_command_jwt_expiration=registration_command_jwt_expiration, registration_command_insecure=registration_command_insecure, registration_command_packages=registration_command_packages, registration_command_update_packages=registration_command_update_packages, registration_command_repo=registration_command_repo, registration_command_repo_gpg_key_url=registration_command_repo_gpg_key_url, registration_command_remote_execution_interface=registration_command_remote_execution_interface, registration_command_setup_remote_execution_pull=registration_command_setup_remote_execution_pull, registration_command_activation_key=registration_command_activation_key, registration_command_activation_keys=registration_command_activation_keys, registration_command_lifecycle_environment_id=registration_command_lifecycle_environment_id, registration_command_force=registration_command_force, registration_command_ignore_subman_errors=registration_command_ignore_subman_errors)
except ApiException as e:
    print("Exception when calling RegistrationCommandsApi->post_registration_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **registration_command_organization_id** | **float**| ID of the Organization to register the host in | [optional]
 **registration_command_location_id** | **float**| ID of the Location to register the host in | [optional]
 **registration_command_hostgroup_id** | **float**| ID of the Host group to register the host in | [optional]
 **registration_command_operatingsystem_id** | **float**| ID of the Operating System to register the host in. Operating system must have a &#x60;host_init_config&#x60; template assigned | [optional]
 **registration_command_smart_proxy_id** | **float**| ID of the Smart Proxy. This Proxy must have enabled both the &#39;Templates&#39; and &#39;Registration&#39; features | [optional]
 **registration_command_setup_insights** | **bool**| Set &#39;host_registration_insights&#39; parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems | [optional]
 **registration_command_setup_remote_execution** | **bool**| Set &#39;host_registration_remote_execution&#39; parameter for the host. If it is set to true, SSH keys will be installed on the host | [optional]
 **registration_command_jwt_expiration** | **float**| Expiration of the authorization token (in hours) | [optional]
 **registration_command_insecure** | **bool**| Enable insecure argument for the initial curl | [optional]
 **registration_command_packages** | **str**| Packages to install on the host when registered. Can be set by &#x60;host_packages&#x60; parameter, example: &#x60;pkg1 pkg2&#x60; | [optional]
 **registration_command_update_packages** | **bool**| Update all packages on the host | [optional]
 **registration_command_repo** | **str**| Repository URL / details, for example for Debian OS family: &#39;deb http://deb.example.com/ buster 1.0&#39;, for Red Hat and SUSE OS family: &#39;http://yum.theforeman.org/client/latest/el8/x86_64/&#39; | [optional]
 **registration_command_repo_gpg_key_url** | **str**| URL of the GPG key for the repository | [optional]
 **registration_command_remote_execution_interface** | **str**| Identifier of the Host interface for Remote execution | [optional]
 **registration_command_setup_remote_execution_pull** | **bool**| Set &#39;host_registration_remote_execution_pull&#39; parameter for the host. If it is set to true, pull provider client will be deployed on the host | [optional]
 **registration_command_activation_key** | **str**| Activation key for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. For multiple keys use &#x60;activation_keys&#x60; param instead. | [optional]
 **registration_command_activation_keys** | [**list[str]**](str.md)| Activation keys for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. Required only if host group has no activation keys. | [optional]
 **registration_command_lifecycle_environment_id** | **float**| Lifecycle environment for the host. | [optional]
 **registration_command_force** | **bool**| Clear any previous registration and run subscription-manager with --force. | [optional]
 **registration_command_ignore_subman_errors** | **bool**| Ignore subscription-manager errors for &#x60;subscription-manager register&#x60; command | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
