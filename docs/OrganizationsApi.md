# pyforeman.OrganizationsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organizations_id**](OrganizationsApi.md#delete_organizations_id) | **DELETE** /organizations/{id} | Delete an organization
[**get_organizations**](OrganizationsApi.md#get_organizations) | **GET** /organizations | List all organizations
[**get_organizations_id**](OrganizationsApi.md#get_organizations_id) | **GET** /organizations/{id} | Show organization
[**get_organizations_id_redhat_provider**](OrganizationsApi.md#get_organizations_id_redhat_provider) | **GET** /organizations/{id}/redhat_provider | List all :resource_id
[**get_organizations_id_releases**](OrganizationsApi.md#get_organizations_id_releases) | **GET** /organizations/{id}/releases | List available releases in the organization
[**get_organizations_label_download_debug_certificate**](OrganizationsApi.md#get_organizations_label_download_debug_certificate) | **GET** /organizations/{label}/download_debug_certificate | Download a debug certificate
[**post_organizations**](OrganizationsApi.md#post_organizations) | **POST** /organizations | Create organization
[**put_organizations_id**](OrganizationsApi.md#put_organizations_id) | **PUT** /organizations/{id} | Update organization
[**put_organizations_id_cdn_configuration**](OrganizationsApi.md#put_organizations_id_cdn_configuration) | **PUT** /organizations/{id}/cdn_configuration | Update the CDN configuration
[**put_organizations_id_repo_discover**](OrganizationsApi.md#put_organizations_id_repo_discover) | **PUT** /organizations/{id}/repo_discover | Discover Repositories
[**put_organizations_label_cancel_repo_discover**](OrganizationsApi.md#put_organizations_label_cancel_repo_discover) | **PUT** /organizations/{label}/cancel_repo_discover | Cancel repository discovery


# **delete_organizations_id**
> delete_organizations_id(id, location_id=location_id, organization_id=organization_id)

Delete an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 8.14 # float | Organization ID
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete an organization
    api_instance.delete_organizations_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Organization ID |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations**
> get_organizations(location_id=location_id, organization_id=organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List all organizations



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List all organizations
    api_instance.get_organizations(location_id=location_id, organization_id=organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id**
> get_organizations_id(id, location_id=location_id, organization_id=organization_id)

Show organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 8.14 # float | organization ID
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show organization
    api_instance.get_organizations_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| organization ID |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_redhat_provider**
> get_organizations_id_redhat_provider(id, location_id=location_id, organization_id=organization_id)

List all :resource_id



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List all :resource_id
    api_instance.get_organizations_id_redhat_provider(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_id_redhat_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_releases**
> get_organizations_id_releases(id, location_id=location_id, organization_id=organization_id)

List available releases in the organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 'id_example' # str | ID of the Organization
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available releases in the organization
    api_instance.get_organizations_id_releases(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_id_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_label_download_debug_certificate**
> get_organizations_label_download_debug_certificate(label, location_id=location_id, organization_id=organization_id)

Download a debug certificate



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
label = 'label_example' # str | Organization label
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Download a debug certificate
    api_instance.get_organizations_label_download_debug_certificate(label, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations_label_download_debug_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Organization label |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations**
> post_organizations(organization_name, location_id=location_id, organization_id=organization_id, organization_description=organization_description, organization_user_ids=organization_user_ids, organization_smart_proxy_ids=organization_smart_proxy_ids, organization_compute_resource_ids=organization_compute_resource_ids, organization_medium_ids=organization_medium_ids, organization_ptable_ids=organization_ptable_ids, organization_provisioning_template_ids=organization_provisioning_template_ids, organization_domain_ids=organization_domain_ids, organization_realm_ids=organization_realm_ids, organization_hostgroup_ids=organization_hostgroup_ids, organization_environment_ids=organization_environment_ids, organization_subnet_ids=organization_subnet_ids, organization_ignore_types=organization_ignore_types, organization_location_ids=organization_location_ids, organization_label=organization_label, simple_content_access=simple_content_access)

Create organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
organization_name = 'organization_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
organization_description = 'organization_description_example' # str |  (optional)
organization_user_ids = ['organization_user_ids_example'] # list[str] | User IDs (optional)
organization_smart_proxy_ids = ['organization_smart_proxy_ids_example'] # list[str] | Smart proxy IDs (optional)
organization_compute_resource_ids = ['organization_compute_resource_ids_example'] # list[str] | Compute resource IDs (optional)
organization_medium_ids = ['organization_medium_ids_example'] # list[str] | Medium IDs (optional)
organization_ptable_ids = ['organization_ptable_ids_example'] # list[str] | Partition template IDs (optional)
organization_provisioning_template_ids = ['organization_provisioning_template_ids_example'] # list[str] | Provisioning template IDs (optional)
organization_domain_ids = ['organization_domain_ids_example'] # list[str] | Domain IDs (optional)
organization_realm_ids = ['organization_realm_ids_example'] # list[str] | Realm IDs (optional)
organization_hostgroup_ids = ['organization_hostgroup_ids_example'] # list[str] | Host group IDs (optional)
organization_environment_ids = ['organization_environment_ids_example'] # list[str] | Environment IDs (optional)
organization_subnet_ids = ['organization_subnet_ids_example'] # list[str] | Subnet IDs (optional)
organization_ignore_types = ['organization_ignore_types_example'] # list[str] | List of resources types that will be automatically associated (optional)
organization_location_ids = ['organization_location_ids_example'] # list[str] | Associated location IDs (optional)
organization_label = 'organization_label_example' # str |  (optional)
simple_content_access = true # bool | Whether to turn on Simple Content Access for the organization. (optional)

try:
    # Create organization
    api_instance.post_organizations(organization_name, location_id=location_id, organization_id=organization_id, organization_description=organization_description, organization_user_ids=organization_user_ids, organization_smart_proxy_ids=organization_smart_proxy_ids, organization_compute_resource_ids=organization_compute_resource_ids, organization_medium_ids=organization_medium_ids, organization_ptable_ids=organization_ptable_ids, organization_provisioning_template_ids=organization_provisioning_template_ids, organization_domain_ids=organization_domain_ids, organization_realm_ids=organization_realm_ids, organization_hostgroup_ids=organization_hostgroup_ids, organization_environment_ids=organization_environment_ids, organization_subnet_ids=organization_subnet_ids, organization_ignore_types=organization_ignore_types, organization_location_ids=organization_location_ids, organization_label=organization_label, simple_content_access=simple_content_access)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **organization_description** | **str**|  | [optional]
 **organization_user_ids** | [**list[str]**](str.md)| User IDs | [optional]
 **organization_smart_proxy_ids** | [**list[str]**](str.md)| Smart proxy IDs | [optional]
 **organization_compute_resource_ids** | [**list[str]**](str.md)| Compute resource IDs | [optional]
 **organization_medium_ids** | [**list[str]**](str.md)| Medium IDs | [optional]
 **organization_ptable_ids** | [**list[str]**](str.md)| Partition template IDs | [optional]
 **organization_provisioning_template_ids** | [**list[str]**](str.md)| Provisioning template IDs | [optional]
 **organization_domain_ids** | [**list[str]**](str.md)| Domain IDs | [optional]
 **organization_realm_ids** | [**list[str]**](str.md)| Realm IDs | [optional]
 **organization_hostgroup_ids** | [**list[str]**](str.md)| Host group IDs | [optional]
 **organization_environment_ids** | [**list[str]**](str.md)| Environment IDs | [optional]
 **organization_subnet_ids** | [**list[str]**](str.md)| Subnet IDs | [optional]
 **organization_ignore_types** | [**list[str]**](str.md)| List of resources types that will be automatically associated | [optional]
 **organization_location_ids** | [**list[str]**](str.md)| Associated location IDs | [optional]
 **organization_label** | **str**|  | [optional]
 **simple_content_access** | **bool**| Whether to turn on Simple Content Access for the organization. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id**
> put_organizations_id(id, location_id=location_id, organization_id=organization_id, redhat_repository_url=redhat_repository_url, simple_content_access=simple_content_access, organization_name=organization_name, organization_description=organization_description, organization_user_ids=organization_user_ids, organization_smart_proxy_ids=organization_smart_proxy_ids, organization_compute_resource_ids=organization_compute_resource_ids, organization_medium_ids=organization_medium_ids, organization_ptable_ids=organization_ptable_ids, organization_provisioning_template_ids=organization_provisioning_template_ids, organization_domain_ids=organization_domain_ids, organization_realm_ids=organization_realm_ids, organization_hostgroup_ids=organization_hostgroup_ids, organization_environment_ids=organization_environment_ids, organization_subnet_ids=organization_subnet_ids, organization_ignore_types=organization_ignore_types, organization_location_ids=organization_location_ids)

Update organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 8.14 # float | organization ID
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
redhat_repository_url = 'redhat_repository_url_example' # str | Red Hat CDN URL (optional)
simple_content_access = true # bool | Whether Simple Content Access should be enabled for the organization. (optional)
organization_name = 'organization_name_example' # str |  (optional)
organization_description = 'organization_description_example' # str |  (optional)
organization_user_ids = ['organization_user_ids_example'] # list[str] | User IDs (optional)
organization_smart_proxy_ids = ['organization_smart_proxy_ids_example'] # list[str] | Smart proxy IDs (optional)
organization_compute_resource_ids = ['organization_compute_resource_ids_example'] # list[str] | Compute resource IDs (optional)
organization_medium_ids = ['organization_medium_ids_example'] # list[str] | Medium IDs (optional)
organization_ptable_ids = ['organization_ptable_ids_example'] # list[str] | Partition template IDs (optional)
organization_provisioning_template_ids = ['organization_provisioning_template_ids_example'] # list[str] | Provisioning template IDs (optional)
organization_domain_ids = ['organization_domain_ids_example'] # list[str] | Domain IDs (optional)
organization_realm_ids = ['organization_realm_ids_example'] # list[str] | Realm IDs (optional)
organization_hostgroup_ids = ['organization_hostgroup_ids_example'] # list[str] | Host group IDs (optional)
organization_environment_ids = ['organization_environment_ids_example'] # list[str] | Environment IDs (optional)
organization_subnet_ids = ['organization_subnet_ids_example'] # list[str] | Subnet IDs (optional)
organization_ignore_types = ['organization_ignore_types_example'] # list[str] | List of resources types that will be automatically associated (optional)
organization_location_ids = ['organization_location_ids_example'] # list[str] | Associated location IDs (optional)

try:
    # Update organization
    api_instance.put_organizations_id(id, location_id=location_id, organization_id=organization_id, redhat_repository_url=redhat_repository_url, simple_content_access=simple_content_access, organization_name=organization_name, organization_description=organization_description, organization_user_ids=organization_user_ids, organization_smart_proxy_ids=organization_smart_proxy_ids, organization_compute_resource_ids=organization_compute_resource_ids, organization_medium_ids=organization_medium_ids, organization_ptable_ids=organization_ptable_ids, organization_provisioning_template_ids=organization_provisioning_template_ids, organization_domain_ids=organization_domain_ids, organization_realm_ids=organization_realm_ids, organization_hostgroup_ids=organization_hostgroup_ids, organization_environment_ids=organization_environment_ids, organization_subnet_ids=organization_subnet_ids, organization_ignore_types=organization_ignore_types, organization_location_ids=organization_location_ids)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| organization ID |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **redhat_repository_url** | **str**| Red Hat CDN URL | [optional]
 **simple_content_access** | **bool**| Whether Simple Content Access should be enabled for the organization. | [optional]
 **organization_name** | **str**|  | [optional]
 **organization_description** | **str**|  | [optional]
 **organization_user_ids** | [**list[str]**](str.md)| User IDs | [optional]
 **organization_smart_proxy_ids** | [**list[str]**](str.md)| Smart proxy IDs | [optional]
 **organization_compute_resource_ids** | [**list[str]**](str.md)| Compute resource IDs | [optional]
 **organization_medium_ids** | [**list[str]**](str.md)| Medium IDs | [optional]
 **organization_ptable_ids** | [**list[str]**](str.md)| Partition template IDs | [optional]
 **organization_provisioning_template_ids** | [**list[str]**](str.md)| Provisioning template IDs | [optional]
 **organization_domain_ids** | [**list[str]**](str.md)| Domain IDs | [optional]
 **organization_realm_ids** | [**list[str]**](str.md)| Realm IDs | [optional]
 **organization_hostgroup_ids** | [**list[str]**](str.md)| Host group IDs | [optional]
 **organization_environment_ids** | [**list[str]**](str.md)| Environment IDs | [optional]
 **organization_subnet_ids** | [**list[str]**](str.md)| Subnet IDs | [optional]
 **organization_ignore_types** | [**list[str]**](str.md)| List of resources types that will be automatically associated | [optional]
 **organization_location_ids** | [**list[str]**](str.md)| Associated location IDs | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id_cdn_configuration**
> put_organizations_id_cdn_configuration(id, type, location_id=location_id, organization_id=organization_id, url=url, username=username, password=password, upstream_organization_label=upstream_organization_label, upstream_content_view_label=upstream_content_view_label, upstream_lifecycle_environment_label=upstream_lifecycle_environment_label, ssl_ca_credential_id=ssl_ca_credential_id, custom_cdn_auth_enabled=custom_cdn_auth_enabled)

Update the CDN configuration



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 'id_example' # str | ID of the Organization
type = 'type_example' # str | CDN configuration type. One of redhat_cdn, network_sync, export_sync, custom_cdn.
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
url = 'url_example' # str | Upstream foreman server to sync CDN content from. Relevant only for 'upstream_server' type. (optional)
username = 'username_example' # str | Username for authentication. Relevant only for 'upstream_server' type. (optional)
password = 'password_example' # str | Password for authentication. Relevant only for 'upstream_server' type. (optional)
upstream_organization_label = 'upstream_organization_label_example' # str | Upstream organization to sync CDN content from. Relevant only for 'upstream_server' type. (optional)
upstream_content_view_label = 'upstream_content_view_label_example' # str | Upstream Content View Label, default: Default_Organization_View. Relevant only for 'upstream_server' type. (optional)
upstream_lifecycle_environment_label = 'upstream_lifecycle_environment_label_example' # str | Upstream Lifecycle Environment, default: Library. Relevant only for 'upstream_server' type. (optional)
ssl_ca_credential_id = 8.14 # float | Content Credential to use for SSL CA. Relevant only for 'upstream_server' type. (optional)
custom_cdn_auth_enabled = true # bool | If product certificates should be used to authenticate to a custom CDN. (optional)

try:
    # Update the CDN configuration
    api_instance.put_organizations_id_cdn_configuration(id, type, location_id=location_id, organization_id=organization_id, url=url, username=username, password=password, upstream_organization_label=upstream_organization_label, upstream_content_view_label=upstream_content_view_label, upstream_lifecycle_environment_label=upstream_lifecycle_environment_label, ssl_ca_credential_id=ssl_ca_credential_id, custom_cdn_auth_enabled=custom_cdn_auth_enabled)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organizations_id_cdn_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Organization |
 **type** | **str**| CDN configuration type. One of redhat_cdn, network_sync, export_sync, custom_cdn. |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **url** | **str**| Upstream foreman server to sync CDN content from. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **username** | **str**| Username for authentication. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **password** | **str**| Password for authentication. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **upstream_organization_label** | **str**| Upstream organization to sync CDN content from. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **upstream_content_view_label** | **str**| Upstream Content View Label, default: Default_Organization_View. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **upstream_lifecycle_environment_label** | **str**| Upstream Lifecycle Environment, default: Library. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **ssl_ca_credential_id** | **float**| Content Credential to use for SSL CA. Relevant only for &#39;upstream_server&#39; type. | [optional]
 **custom_cdn_auth_enabled** | **bool**| If product certificates should be used to authenticate to a custom CDN. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id_repo_discover**
> put_organizations_id_repo_discover(id, location_id=location_id, organization_id=organization_id, url=url, content_type=content_type, upstream_username=upstream_username, upstream_password=upstream_password, search=search)

Discover Repositories



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
id = 8.14 # float | Organization ID
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
url = 'url_example' # str | Base URL to perform repo discovery on (optional)
content_type = 'content_type_example' # str | One of yum or docker (optional)
upstream_username = 'upstream_username_example' # str | Username to access URL (optional)
upstream_password = 'upstream_password_example' # str | Password to access URL (optional)
search = 'search_example' # str | Search pattern (defaults to '*') (optional)

try:
    # Discover Repositories
    api_instance.put_organizations_id_repo_discover(id, location_id=location_id, organization_id=organization_id, url=url, content_type=content_type, upstream_username=upstream_username, upstream_password=upstream_password, search=search)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organizations_id_repo_discover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Organization ID |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **url** | **str**| Base URL to perform repo discovery on | [optional]
 **content_type** | **str**| One of yum or docker | [optional]
 **upstream_username** | **str**| Username to access URL | [optional]
 **upstream_password** | **str**| Password to access URL | [optional]
 **search** | **str**| Search pattern (defaults to &#39;*&#39;) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_label_cancel_repo_discover**
> put_organizations_label_cancel_repo_discover(label, location_id=location_id, organization_id=organization_id, url=url)

Cancel repository discovery



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.OrganizationsApi()
label = 'label_example' # str | Organization label
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
url = 'url_example' # str | base url to perform repo discovery on (optional)

try:
    # Cancel repository discovery
    api_instance.put_organizations_label_cancel_repo_discover(label, location_id=location_id, organization_id=organization_id, url=url)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_organizations_label_cancel_repo_discover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Organization label |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **url** | **str**| base url to perform repo discovery on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
