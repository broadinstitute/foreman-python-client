# foreman.ProvisioningTemplatesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_provisioning_templates_id**](ProvisioningTemplatesApi.md#delete_provisioning_templates_id) | **DELETE** /provisioning_templates/{id} | Delete a provisioning template
[**get_locations_location_id_provisioning_templates**](ProvisioningTemplatesApi.md#get_locations_location_id_provisioning_templates) | **GET** /locations/{location_id}/provisioning_templates | List provisioning templates per location
[**get_operatingsystems_operatingsystem_id_provisioning_templates**](ProvisioningTemplatesApi.md#get_operatingsystems_operatingsystem_id_provisioning_templates) | **GET** /operatingsystems/{operatingsystem_id}/provisioning_templates | List provisioning templates per operating system
[**get_organizations_organization_id_provisioning_templates**](ProvisioningTemplatesApi.md#get_organizations_organization_id_provisioning_templates) | **GET** /organizations/{organization_id}/provisioning_templates | List provisioning templates per organization
[**get_provisioning_templates**](ProvisioningTemplatesApi.md#get_provisioning_templates) | **GET** /provisioning_templates | List provisioning templates
[**get_provisioning_templates_id**](ProvisioningTemplatesApi.md#get_provisioning_templates_id) | **GET** /provisioning_templates/{id} | Show provisioning template details
[**get_provisioning_templates_id_export**](ProvisioningTemplatesApi.md#get_provisioning_templates_id_export) | **GET** /provisioning_templates/{id}/export | Export a provisioning template to ERB
[**get_provisioning_templates_revision**](ProvisioningTemplatesApi.md#get_provisioning_templates_revision) | **GET** /provisioning_templates/revision | 
[**post_provisioning_templates**](ProvisioningTemplatesApi.md#post_provisioning_templates) | **POST** /provisioning_templates | Create a provisioning template
[**post_provisioning_templates_build_pxe_default**](ProvisioningTemplatesApi.md#post_provisioning_templates_build_pxe_default) | **POST** /provisioning_templates/build_pxe_default | Update the default PXE menu on all configured TFTP servers
[**post_provisioning_templates_id_clone**](ProvisioningTemplatesApi.md#post_provisioning_templates_id_clone) | **POST** /provisioning_templates/{id}/clone | Clone a provision template
[**post_provisioning_templates_import**](ProvisioningTemplatesApi.md#post_provisioning_templates_import) | **POST** /provisioning_templates/import | Import a provisioning template
[**put_provisioning_templates_id**](ProvisioningTemplatesApi.md#put_provisioning_templates_id) | **PUT** /provisioning_templates/{id} | Update a provisioning template


# **delete_provisioning_templates_id**
> delete_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id)

Delete a provisioning template

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a provisioning template
        api_instance.delete_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->delete_provisioning_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_locations_location_id_provisioning_templates**
> get_locations_location_id_provisioning_templates(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List provisioning templates per location

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    location_id = 3.4 # float | Scope by locations
    operatingsystem_id = 3.4 # float | ID of operating system
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List provisioning templates per location
        api_instance.get_locations_location_id_provisioning_templates(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_locations_location_id_provisioning_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **organization_id** | **float**| Scope by organizations | 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_operatingsystems_operatingsystem_id_provisioning_templates**
> get_operatingsystems_operatingsystem_id_provisioning_templates(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List provisioning templates per operating system

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List provisioning templates per operating system
        api_instance.get_operatingsystems_operatingsystem_id_provisioning_templates(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_operatingsystems_operatingsystem_id_provisioning_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_organizations_organization_id_provisioning_templates**
> get_organizations_organization_id_provisioning_templates(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)

List provisioning templates per organization

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List provisioning templates per organization
        api_instance.get_organizations_organization_id_provisioning_templates(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_organizations_organization_id_provisioning_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_provisioning_templates**
> get_provisioning_templates(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List provisioning templates

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List provisioning templates
        api_instance.get_provisioning_templates(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_provisioning_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_provisioning_templates_id**
> get_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id)

Show provisioning template details

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show provisioning template details
        api_instance.get_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_provisioning_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_provisioning_templates_id_export**
> get_provisioning_templates_id_export(id, location_id=location_id, organization_id=organization_id)

Export a provisioning template to ERB

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Export a provisioning template to ERB
        api_instance.get_provisioning_templates_id_export(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_provisioning_templates_id_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_provisioning_templates_revision**
> get_provisioning_templates_revision(location_id=location_id, organization_id=organization_id, version=version)



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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    version = 'version_example' # str | template version (optional)

    try:
        api_instance.get_provisioning_templates_revision(location_id=location_id, organization_id=organization_id, version=version)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->get_provisioning_templates_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **version** | **str**| template version | [optional] 

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

# **post_provisioning_templates**
> post_provisioning_templates(provisioning_template_name, provisioning_template_template, location_id=location_id, organization_id=organization_id, provisioning_template_description=provisioning_template_description, provisioning_template_snippet=provisioning_template_snippet, provisioning_template_audit_comment=provisioning_template_audit_comment, provisioning_template_template_kind_id=provisioning_template_template_kind_id, provisioning_template_template_combinations_attributes=provisioning_template_template_combinations_attributes, provisioning_template_operatingsystem_ids=provisioning_template_operatingsystem_ids, provisioning_template_locked=provisioning_template_locked, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids)

Create a provisioning template

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    provisioning_template_name = 'provisioning_template_name_example' # str | template name
    provisioning_template_template = 'provisioning_template_template_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    provisioning_template_description = 'provisioning_template_description_example' # str |  (optional)
    provisioning_template_snippet = True # bool |  (optional)
    provisioning_template_audit_comment = 'provisioning_template_audit_comment_example' # str |  (optional)
    provisioning_template_template_kind_id = 3.4 # float | not relevant for snippet (optional)
    provisioning_template_template_combinations_attributes = ['provisioning_template_template_combinations_attributes_example'] # List[str] | Array of template combinations (hostgroup_id, environment_id) (optional)
    provisioning_template_operatingsystem_ids = ['provisioning_template_operatingsystem_ids_example'] # List[str] | Array of operating system IDs to associate with the template (optional)
    provisioning_template_locked = True # bool | Whether or not the template is locked for editing (optional)
    provisioning_template_location_ids = ['provisioning_template_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    provisioning_template_organization_ids = ['provisioning_template_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create a provisioning template
        api_instance.post_provisioning_templates(provisioning_template_name, provisioning_template_template, location_id=location_id, organization_id=organization_id, provisioning_template_description=provisioning_template_description, provisioning_template_snippet=provisioning_template_snippet, provisioning_template_audit_comment=provisioning_template_audit_comment, provisioning_template_template_kind_id=provisioning_template_template_kind_id, provisioning_template_template_combinations_attributes=provisioning_template_template_combinations_attributes, provisioning_template_operatingsystem_ids=provisioning_template_operatingsystem_ids, provisioning_template_locked=provisioning_template_locked, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->post_provisioning_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_name** | **str**| template name | 
 **provisioning_template_template** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **provisioning_template_description** | **str**|  | [optional] 
 **provisioning_template_snippet** | **bool**|  | [optional] 
 **provisioning_template_audit_comment** | **str**|  | [optional] 
 **provisioning_template_template_kind_id** | **float**| not relevant for snippet | [optional] 
 **provisioning_template_template_combinations_attributes** | [**List[str]**](str.md)| Array of template combinations (hostgroup_id, environment_id) | [optional] 
 **provisioning_template_operatingsystem_ids** | [**List[str]**](str.md)| Array of operating system IDs to associate with the template | [optional] 
 **provisioning_template_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **provisioning_template_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **provisioning_template_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **post_provisioning_templates_build_pxe_default**
> post_provisioning_templates_build_pxe_default(location_id=location_id, organization_id=organization_id)

Update the default PXE menu on all configured TFTP servers

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Update the default PXE menu on all configured TFTP servers
        api_instance.post_provisioning_templates_build_pxe_default(location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->post_provisioning_templates_build_pxe_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **post_provisioning_templates_id_clone**
> post_provisioning_templates_id_clone(id, provisioning_template_name, location_id=location_id, organization_id=organization_id)

Clone a provision template

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    id = 'id_example' # str | 
    provisioning_template_name = 'provisioning_template_name_example' # str | template name
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Clone a provision template
        api_instance.post_provisioning_templates_id_clone(id, provisioning_template_name, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->post_provisioning_templates_id_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **provisioning_template_name** | **str**| template name | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **post_provisioning_templates_import**
> post_provisioning_templates_import(location_id=location_id, organization_id=organization_id, provisioning_template_name=provisioning_template_name, provisioning_template_template=provisioning_template_template, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)

Import a provisioning template

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    provisioning_template_name = 'provisioning_template_name_example' # str | template name (optional)
    provisioning_template_template = 'provisioning_template_template_example' # str | template contents including metadata (optional)
    provisioning_template_location_ids = ['provisioning_template_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    provisioning_template_organization_ids = ['provisioning_template_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)
    options_force = True # bool | use if you want update locked templates (optional)
    options_associate = 'options_associate_example' # str | determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata (optional)
    options_lock = True # bool | lock imported templates (false by default) (optional)
    options_default = True # bool | makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) (optional)

    try:
        # Import a provisioning template
        api_instance.post_provisioning_templates_import(location_id=location_id, organization_id=organization_id, provisioning_template_name=provisioning_template_name, provisioning_template_template=provisioning_template_template, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->post_provisioning_templates_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **provisioning_template_name** | **str**| template name | [optional] 
 **provisioning_template_template** | **str**| template contents including metadata | [optional] 
 **provisioning_template_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **provisioning_template_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 
 **options_force** | **bool**| use if you want update locked templates | [optional] 
 **options_associate** | **str**| determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata | [optional] 
 **options_lock** | **bool**| lock imported templates (false by default) | [optional] 
 **options_default** | **bool**| makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) | [optional] 

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

# **put_provisioning_templates_id**
> put_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id, provisioning_template_name=provisioning_template_name, provisioning_template_description=provisioning_template_description, provisioning_template_template=provisioning_template_template, provisioning_template_snippet=provisioning_template_snippet, provisioning_template_audit_comment=provisioning_template_audit_comment, provisioning_template_template_kind_id=provisioning_template_template_kind_id, provisioning_template_template_combinations_attributes=provisioning_template_template_combinations_attributes, provisioning_template_operatingsystem_ids=provisioning_template_operatingsystem_ids, provisioning_template_locked=provisioning_template_locked, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids)

Update a provisioning template

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
    api_instance = foreman.ProvisioningTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    provisioning_template_name = 'provisioning_template_name_example' # str | template name (optional)
    provisioning_template_description = 'provisioning_template_description_example' # str |  (optional)
    provisioning_template_template = 'provisioning_template_template_example' # str |  (optional)
    provisioning_template_snippet = True # bool |  (optional)
    provisioning_template_audit_comment = 'provisioning_template_audit_comment_example' # str |  (optional)
    provisioning_template_template_kind_id = 3.4 # float | not relevant for snippet (optional)
    provisioning_template_template_combinations_attributes = ['provisioning_template_template_combinations_attributes_example'] # List[str] | Array of template combinations (hostgroup_id, environment_id) (optional)
    provisioning_template_operatingsystem_ids = ['provisioning_template_operatingsystem_ids_example'] # List[str] | Array of operating system IDs to associate with the template (optional)
    provisioning_template_locked = True # bool | Whether or not the template is locked for editing (optional)
    provisioning_template_location_ids = ['provisioning_template_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    provisioning_template_organization_ids = ['provisioning_template_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update a provisioning template
        api_instance.put_provisioning_templates_id(id, location_id=location_id, organization_id=organization_id, provisioning_template_name=provisioning_template_name, provisioning_template_description=provisioning_template_description, provisioning_template_template=provisioning_template_template, provisioning_template_snippet=provisioning_template_snippet, provisioning_template_audit_comment=provisioning_template_audit_comment, provisioning_template_template_kind_id=provisioning_template_template_kind_id, provisioning_template_template_combinations_attributes=provisioning_template_template_combinations_attributes, provisioning_template_operatingsystem_ids=provisioning_template_operatingsystem_ids, provisioning_template_locked=provisioning_template_locked, provisioning_template_location_ids=provisioning_template_location_ids, provisioning_template_organization_ids=provisioning_template_organization_ids)
    except Exception as e:
        print("Exception when calling ProvisioningTemplatesApi->put_provisioning_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **provisioning_template_name** | **str**| template name | [optional] 
 **provisioning_template_description** | **str**|  | [optional] 
 **provisioning_template_template** | **str**|  | [optional] 
 **provisioning_template_snippet** | **bool**|  | [optional] 
 **provisioning_template_audit_comment** | **str**|  | [optional] 
 **provisioning_template_template_kind_id** | **float**| not relevant for snippet | [optional] 
 **provisioning_template_template_combinations_attributes** | [**List[str]**](str.md)| Array of template combinations (hostgroup_id, environment_id) | [optional] 
 **provisioning_template_operatingsystem_ids** | [**List[str]**](str.md)| Array of operating system IDs to associate with the template | [optional] 
 **provisioning_template_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **provisioning_template_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **provisioning_template_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

