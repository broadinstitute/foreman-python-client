# foreman.RegistrationApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_register**](RegistrationApi.md#get_register) | **GET** /register | Render Global registration template
[**post_register**](RegistrationApi.md#post_register) | **POST** /register | Find or create a host and render the &#39;Host initial configuration&#39; template


# **get_register**
> get_register(organization_id=organization_id, location_id=location_id, hostgroup_id=hostgroup_id, operatingsystem_id=operatingsystem_id, setup_insights=setup_insights, setup_remote_execution=setup_remote_execution, packages=packages, update_packages=update_packages, repo=repo, repo_gpg_key_url=repo_gpg_key_url, remote_execution_interface=remote_execution_interface, setup_remote_execution_pull=setup_remote_execution_pull)

Render Global registration template

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.RegistrationApi(api_client)
    organization_id = 3.4 # float | ID of the Organization to register the host in (optional)
    location_id = 3.4 # float | ID of the Location to register the host in (optional)
    hostgroup_id = 3.4 # float | ID of the Host group to register the host in (optional)
    operatingsystem_id = 3.4 # float | ID of the Operating System to register the host in (optional)
    setup_insights = True # bool | Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems (optional)
    setup_remote_execution = True # bool | Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host (optional)
    packages = 'packages_example' # str | Packages to install on the host when registered. Can be set by `host_packages` parameter, example: `pkg1 pkg2` (optional)
    update_packages = True # bool | Update all packages on the host (optional)
    repo = 'repo_example' # str | Repository URL / details, for example for Debian OS family: 'deb http://deb.example.com/ buster 1.0', for Red Hat OS family: 'http://yum.theforeman.org/client/latest/el8/x86_64/' (optional)
    repo_gpg_key_url = 'repo_gpg_key_url_example' # str | URL of the GPG key for the repository (optional)
    remote_execution_interface = 'remote_execution_interface_example' # str | Identifier of the Host interface for Remote execution (optional)
    setup_remote_execution_pull = True # bool | Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host (optional)

    try:
        # Render Global registration template
        api_instance.get_register(organization_id=organization_id, location_id=location_id, hostgroup_id=hostgroup_id, operatingsystem_id=operatingsystem_id, setup_insights=setup_insights, setup_remote_execution=setup_remote_execution, packages=packages, update_packages=update_packages, repo=repo, repo_gpg_key_url=repo_gpg_key_url, remote_execution_interface=remote_execution_interface, setup_remote_execution_pull=setup_remote_execution_pull)
    except Exception as e:
        print("Exception when calling RegistrationApi->get_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the Organization to register the host in | [optional] 
 **location_id** | **float**| ID of the Location to register the host in | [optional] 
 **hostgroup_id** | **float**| ID of the Host group to register the host in | [optional] 
 **operatingsystem_id** | **float**| ID of the Operating System to register the host in | [optional] 
 **setup_insights** | **bool**| Set &#39;host_registration_insights&#39; parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems | [optional] 
 **setup_remote_execution** | **bool**| Set &#39;host_registration_remote_execution&#39; parameter for the host. If it is set to true, SSH keys will be installed on the host | [optional] 
 **packages** | **str**| Packages to install on the host when registered. Can be set by &#x60;host_packages&#x60; parameter, example: &#x60;pkg1 pkg2&#x60; | [optional] 
 **update_packages** | **bool**| Update all packages on the host | [optional] 
 **repo** | **str**| Repository URL / details, for example for Debian OS family: &#39;deb http://deb.example.com/ buster 1.0&#39;, for Red Hat OS family: &#39;http://yum.theforeman.org/client/latest/el8/x86_64/&#39; | [optional] 
 **repo_gpg_key_url** | **str**| URL of the GPG key for the repository | [optional] 
 **remote_execution_interface** | **str**| Identifier of the Host interface for Remote execution | [optional] 
 **setup_remote_execution_pull** | **bool**| Set &#39;host_registration_remote_execution_pull&#39; parameter for the host. If it is set to true, pull provider client will be deployed on the host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_register**
> post_register(location_id=location_id, organization_id=organization_id, host_name=host_name, host_location_id=host_location_id, host_organization_id=host_organization_id, host_ip=host_ip, host_ip6=host_ip6, host_mac=host_mac, host_domain_id=host_domain_id, host_operatingsystem_id=host_operatingsystem_id, host_subnet_id=host_subnet_id, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_managed=host_managed, host_comment=host_comment, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes, setup_insights=setup_insights, setup_remote_execution=setup_remote_execution, remote_execution_interface=remote_execution_interface, setup_remote_execution_pull=setup_remote_execution_pull)

Find or create a host and render the 'Host initial configuration' template

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.RegistrationApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    host_name = 'host_name_example' # str |  (optional)
    host_location_id = 3.4 # float |  (optional)
    host_organization_id = 3.4 # float |  (optional)
    host_ip = 'host_ip_example' # str | IPv4 address, not required if using a subnet with DHCP proxy (optional)
    host_ip6 = 'host_ip6_example' # str | IPv6 address, not required if using a subnet with DHCP proxy (optional)
    host_mac = 'host_mac_example' # str | required for managed host that is bare metal, not required if it's a virtual machine (optional)
    host_domain_id = 3.4 # float | required if host is managed and value is not inherited from host group (optional)
    host_operatingsystem_id = 3.4 # float | required if host is managed and value is not inherited from host group (optional)
    host_subnet_id = 3.4 # float | required if host is managed and value is not inherited from host group (optional)
    host_model_id = 3.4 # float |  (optional)
    host_hostgroup_id = 3.4 # float |  (optional)
    host_host_parameters_attributes = ['host_host_parameters_attributes_example'] # List[str] | Host's parameters (array or indexed hash) (optional)
    host_build = True # bool |  (optional)
    host_enabled = True # bool | Include this host within Foreman reporting (optional)
    host_managed = True # bool | True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not (optional)
    host_comment = 'host_comment_example' # str | Additional information about this host (optional)
    host_interfaces_attributes = ['host_interfaces_attributes_example'] # List[str] | Host's network interfaces (optional)
    host_content_facet_attributes_content_view_id = 3.4 # float |  (optional)
    host_content_facet_attributes_lifecycle_environment_id = 3.4 # float |  (optional)
    host_content_facet_attributes_content_source_id = 3.4 # float |  (optional)
    host_content_facet_attributes_kickstart_repository_id = 3.4 # float | Repository Id associated with the kickstart repo used for provisioning (optional)
    host_subscription_facet_attributes_release_version = 'host_subscription_facet_attributes_release_version_example' # str | Release version for this Host to use (7Server, 7.1, etc) (optional)
    host_subscription_facet_attributes_autoheal = True # bool | Sets whether the Host will autoheal subscriptions upon checkin (optional)
    host_subscription_facet_attributes_purpose_usage = 'host_subscription_facet_attributes_purpose_usage_example' # str | Sets the system purpose usage (optional)
    host_subscription_facet_attributes_purpose_role = 'host_subscription_facet_attributes_purpose_role_example' # str | Sets the system purpose usage (optional)
    host_subscription_facet_attributes_purpose_addons = ['host_subscription_facet_attributes_purpose_addons_example'] # List[str] | Sets the system add-ons (optional)
    host_subscription_facet_attributes_service_level = 'host_subscription_facet_attributes_service_level_example' # str | Service level to be used for autoheal (optional)
    host_subscription_facet_attributes_hypervisor_guest_uuids = ['host_subscription_facet_attributes_hypervisor_guest_uuids_example'] # List[str] | List of hypervisor guest uuids (optional)
    host_subscription_facet_attributes_installed_products_attributes = ['host_subscription_facet_attributes_installed_products_attributes_example'] # List[str] | List of products installed on the host (optional)
    setup_insights = True # bool | Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems (optional)
    setup_remote_execution = True # bool | Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host (optional)
    remote_execution_interface = 'remote_execution_interface_example' # str | Identifier of the Host interface for Remote execution (optional)
    setup_remote_execution_pull = True # bool | Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host (optional)

    try:
        # Find or create a host and render the 'Host initial configuration' template
        api_instance.post_register(location_id=location_id, organization_id=organization_id, host_name=host_name, host_location_id=host_location_id, host_organization_id=host_organization_id, host_ip=host_ip, host_ip6=host_ip6, host_mac=host_mac, host_domain_id=host_domain_id, host_operatingsystem_id=host_operatingsystem_id, host_subnet_id=host_subnet_id, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_managed=host_managed, host_comment=host_comment, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes, setup_insights=setup_insights, setup_remote_execution=setup_remote_execution, remote_execution_interface=remote_execution_interface, setup_remote_execution_pull=setup_remote_execution_pull)
    except Exception as e:
        print("Exception when calling RegistrationApi->post_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **host_name** | **str**|  | [optional] 
 **host_location_id** | **float**|  | [optional] 
 **host_organization_id** | **float**|  | [optional] 
 **host_ip** | **str**| IPv4 address, not required if using a subnet with DHCP proxy | [optional] 
 **host_ip6** | **str**| IPv6 address, not required if using a subnet with DHCP proxy | [optional] 
 **host_mac** | **str**| required for managed host that is bare metal, not required if it&#39;s a virtual machine | [optional] 
 **host_domain_id** | **float**| required if host is managed and value is not inherited from host group | [optional] 
 **host_operatingsystem_id** | **float**| required if host is managed and value is not inherited from host group | [optional] 
 **host_subnet_id** | **float**| required if host is managed and value is not inherited from host group | [optional] 
 **host_model_id** | **float**|  | [optional] 
 **host_hostgroup_id** | **float**|  | [optional] 
 **host_host_parameters_attributes** | [**List[str]**](str.md)| Host&#39;s parameters (array or indexed hash) | [optional] 
 **host_build** | **bool**|  | [optional] 
 **host_enabled** | **bool**| Include this host within Foreman reporting | [optional] 
 **host_managed** | **bool**| True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not | [optional] 
 **host_comment** | **str**| Additional information about this host | [optional] 
 **host_interfaces_attributes** | [**List[str]**](str.md)| Host&#39;s network interfaces | [optional] 
 **host_content_facet_attributes_content_view_id** | **float**|  | [optional] 
 **host_content_facet_attributes_lifecycle_environment_id** | **float**|  | [optional] 
 **host_content_facet_attributes_content_source_id** | **float**|  | [optional] 
 **host_content_facet_attributes_kickstart_repository_id** | **float**| Repository Id associated with the kickstart repo used for provisioning | [optional] 
 **host_subscription_facet_attributes_release_version** | **str**| Release version for this Host to use (7Server, 7.1, etc) | [optional] 
 **host_subscription_facet_attributes_autoheal** | **bool**| Sets whether the Host will autoheal subscriptions upon checkin | [optional] 
 **host_subscription_facet_attributes_purpose_usage** | **str**| Sets the system purpose usage | [optional] 
 **host_subscription_facet_attributes_purpose_role** | **str**| Sets the system purpose usage | [optional] 
 **host_subscription_facet_attributes_purpose_addons** | [**List[str]**](str.md)| Sets the system add-ons | [optional] 
 **host_subscription_facet_attributes_service_level** | **str**| Service level to be used for autoheal | [optional] 
 **host_subscription_facet_attributes_hypervisor_guest_uuids** | [**List[str]**](str.md)| List of hypervisor guest uuids | [optional] 
 **host_subscription_facet_attributes_installed_products_attributes** | [**List[str]**](str.md)| List of products installed on the host | [optional] 
 **setup_insights** | **bool**| Set &#39;host_registration_insights&#39; parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems | [optional] 
 **setup_remote_execution** | **bool**| Set &#39;host_registration_remote_execution&#39; parameter for the host. If it is set to true, SSH keys will be installed on the host | [optional] 
 **remote_execution_interface** | **str**| Identifier of the Host interface for Remote execution | [optional] 
 **setup_remote_execution_pull** | **bool**| Set &#39;host_registration_remote_execution_pull&#39; parameter for the host. If it is set to true, pull provider client will be deployed on the host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

