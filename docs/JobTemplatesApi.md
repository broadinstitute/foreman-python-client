# foreman.JobTemplatesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_job_templates_id**](JobTemplatesApi.md#delete_job_templates_id) | **DELETE** /job_templates/{id} | Delete a job template
[**get_job_templates**](JobTemplatesApi.md#get_job_templates) | **GET** /job_templates | List job templates
[**get_job_templates_id**](JobTemplatesApi.md#get_job_templates_id) | **GET** /job_templates/{id} | Show job template details
[**get_job_templates_id_export**](JobTemplatesApi.md#get_job_templates_id_export) | **GET** /job_templates/{id}/export | Export a job template to ERB
[**get_job_templates_revision**](JobTemplatesApi.md#get_job_templates_revision) | **GET** /job_templates/revision | 
[**get_locations_location_id_job_templates**](JobTemplatesApi.md#get_locations_location_id_job_templates) | **GET** /locations/{location_id}/job_templates | List job templates per location
[**get_organizations_organization_id_job_templates**](JobTemplatesApi.md#get_organizations_organization_id_job_templates) | **GET** /organizations/{organization_id}/job_templates | List job templates per organization
[**post_job_templates**](JobTemplatesApi.md#post_job_templates) | **POST** /job_templates | Create a job template
[**post_job_templates_id_clone**](JobTemplatesApi.md#post_job_templates_id_clone) | **POST** /job_templates/{id}/clone | Clone a provision template
[**post_job_templates_import**](JobTemplatesApi.md#post_job_templates_import) | **POST** /job_templates/import | Import a job template from ERB
[**put_job_templates_id**](JobTemplatesApi.md#put_job_templates_id) | **PUT** /job_templates/{id} | Update a job template


# **delete_job_templates_id**
> delete_job_templates_id(id, location_id=location_id, organization_id=organization_id)

Delete a job template

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
    api_instance = foreman.JobTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a job template
        api_instance.delete_job_templates_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->delete_job_templates_id: %s\n" % e)
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

# **get_job_templates**
> get_job_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List job templates

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
    api_instance = foreman.JobTemplatesApi(api_client)
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List job templates
        api_instance.get_job_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_job_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_job_templates_id**
> get_job_templates_id(id, location_id=location_id, organization_id=organization_id)

Show job template details

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
    api_instance = foreman.JobTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show job template details
        api_instance.get_job_templates_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_job_templates_id: %s\n" % e)
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

# **get_job_templates_id_export**
> get_job_templates_id_export(id, location_id=location_id, organization_id=organization_id)

Export a job template to ERB

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
    api_instance = foreman.JobTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Export a job template to ERB
        api_instance.get_job_templates_id_export(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_job_templates_id_export: %s\n" % e)
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

# **get_job_templates_revision**
> get_job_templates_revision(location_id=location_id, organization_id=organization_id, version=version)



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
    api_instance = foreman.JobTemplatesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    version = 'version_example' # str | Template version (optional)

    try:
        api_instance.get_job_templates_revision(location_id=location_id, organization_id=organization_id, version=version)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_job_templates_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **version** | **str**| Template version | [optional] 

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

# **get_locations_location_id_job_templates**
> get_locations_location_id_job_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List job templates per location

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
    api_instance = foreman.JobTemplatesApi(api_client)
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List job templates per location
        api_instance.get_locations_location_id_job_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_locations_location_id_job_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_organizations_organization_id_job_templates**
> get_organizations_organization_id_job_templates(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)

List job templates per organization

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
    api_instance = foreman.JobTemplatesApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List job templates per organization
        api_instance.get_organizations_organization_id_job_templates(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->get_organizations_organization_id_job_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations | 
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

# **post_job_templates**
> post_job_templates(job_template_name, job_template_job_category, job_template_template, job_template_provider_type, location_id=location_id, organization_id=organization_id, job_template_description=job_template_description, job_template_description_format=job_template_description_format, job_template_snippet=job_template_snippet, job_template_audit_comment=job_template_audit_comment, job_template_locked=job_template_locked, job_template_effective_user_attributes_value=job_template_effective_user_attributes_value, job_template_effective_user_attributes_overridable=job_template_effective_user_attributes_overridable, job_template_effective_user_attributes_current_user=job_template_effective_user_attributes_current_user, job_template_location_ids=job_template_location_ids, job_template_organization_ids=job_template_organization_ids)

Create a job template

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
    api_instance = foreman.JobTemplatesApi(api_client)
    job_template_name = 'job_template_name_example' # str | Template name
    job_template_job_category = 'job_template_job_category_example' # str | Job category
    job_template_template = 'job_template_template_example' # str | 
    job_template_provider_type = 'job_template_provider_type_example' # str | Provider type
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    job_template_description = 'job_template_description_example' # str |  (optional)
    job_template_description_format = 'job_template_description_format_example' # str | This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}. (optional)
    job_template_snippet = True # bool |  (optional)
    job_template_audit_comment = 'job_template_audit_comment_example' # str |  (optional)
    job_template_locked = True # bool | Whether or not the template is locked for editing (optional)
    job_template_effective_user_attributes_value = 'job_template_effective_user_attributes_value_example' # str | What user should be used to run the script (using sudo-like mechanisms) (optional)
    job_template_effective_user_attributes_overridable = True # bool | Whether it should be allowed to override the effective user from the invocation form. (optional)
    job_template_effective_user_attributes_current_user = True # bool | Whether the current user login should be used as the effective user (optional)
    job_template_location_ids = ['job_template_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    job_template_organization_ids = ['job_template_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create a job template
        api_instance.post_job_templates(job_template_name, job_template_job_category, job_template_template, job_template_provider_type, location_id=location_id, organization_id=organization_id, job_template_description=job_template_description, job_template_description_format=job_template_description_format, job_template_snippet=job_template_snippet, job_template_audit_comment=job_template_audit_comment, job_template_locked=job_template_locked, job_template_effective_user_attributes_value=job_template_effective_user_attributes_value, job_template_effective_user_attributes_overridable=job_template_effective_user_attributes_overridable, job_template_effective_user_attributes_current_user=job_template_effective_user_attributes_current_user, job_template_location_ids=job_template_location_ids, job_template_organization_ids=job_template_organization_ids)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->post_job_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_template_name** | **str**| Template name | 
 **job_template_job_category** | **str**| Job category | 
 **job_template_template** | **str**|  | 
 **job_template_provider_type** | **str**| Provider type | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **job_template_description** | **str**|  | [optional] 
 **job_template_description_format** | **str**| This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}. | [optional] 
 **job_template_snippet** | **bool**|  | [optional] 
 **job_template_audit_comment** | **str**|  | [optional] 
 **job_template_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **job_template_effective_user_attributes_value** | **str**| What user should be used to run the script (using sudo-like mechanisms) | [optional] 
 **job_template_effective_user_attributes_overridable** | **bool**| Whether it should be allowed to override the effective user from the invocation form. | [optional] 
 **job_template_effective_user_attributes_current_user** | **bool**| Whether the current user login should be used as the effective user | [optional] 
 **job_template_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **job_template_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **post_job_templates_id_clone**
> post_job_templates_id_clone(id, job_template_name, location_id=location_id, organization_id=organization_id)

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
    api_instance = foreman.JobTemplatesApi(api_client)
    id = 'id_example' # str | 
    job_template_name = 'job_template_name_example' # str | Template name
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Clone a provision template
        api_instance.post_job_templates_id_clone(id, job_template_name, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->post_job_templates_id_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **job_template_name** | **str**| Template name | 
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

# **post_job_templates_import**
> post_job_templates_import(template, location_id=location_id, organization_id=organization_id, overwrite=overwrite)

Import a job template from ERB

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
    api_instance = foreman.JobTemplatesApi(api_client)
    template = 'template_example' # str | Template ERB
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    overwrite = True # bool | Overwrite template if it already exists (optional)

    try:
        # Import a job template from ERB
        api_instance.post_job_templates_import(template, location_id=location_id, organization_id=organization_id, overwrite=overwrite)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->post_job_templates_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| Template ERB | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **overwrite** | **bool**| Overwrite template if it already exists | [optional] 

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

# **put_job_templates_id**
> put_job_templates_id(id, location_id=location_id, organization_id=organization_id, job_template_name=job_template_name, job_template_description=job_template_description, job_template_job_category=job_template_job_category, job_template_description_format=job_template_description_format, job_template_template=job_template_template, job_template_provider_type=job_template_provider_type, job_template_snippet=job_template_snippet, job_template_audit_comment=job_template_audit_comment, job_template_locked=job_template_locked, job_template_effective_user_attributes_value=job_template_effective_user_attributes_value, job_template_effective_user_attributes_overridable=job_template_effective_user_attributes_overridable, job_template_effective_user_attributes_current_user=job_template_effective_user_attributes_current_user, job_template_location_ids=job_template_location_ids, job_template_organization_ids=job_template_organization_ids)

Update a job template

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
    api_instance = foreman.JobTemplatesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    job_template_name = 'job_template_name_example' # str | Template name (optional)
    job_template_description = 'job_template_description_example' # str |  (optional)
    job_template_job_category = 'job_template_job_category_example' # str | Job category (optional)
    job_template_description_format = 'job_template_description_format_example' # str | This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}. (optional)
    job_template_template = 'job_template_template_example' # str |  (optional)
    job_template_provider_type = 'job_template_provider_type_example' # str | Provider type (optional)
    job_template_snippet = True # bool |  (optional)
    job_template_audit_comment = 'job_template_audit_comment_example' # str |  (optional)
    job_template_locked = True # bool | Whether or not the template is locked for editing (optional)
    job_template_effective_user_attributes_value = 'job_template_effective_user_attributes_value_example' # str | What user should be used to run the script (using sudo-like mechanisms) (optional)
    job_template_effective_user_attributes_overridable = True # bool | Whether it should be allowed to override the effective user from the invocation form. (optional)
    job_template_effective_user_attributes_current_user = True # bool | Whether the current user login should be used as the effective user (optional)
    job_template_location_ids = ['job_template_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    job_template_organization_ids = ['job_template_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update a job template
        api_instance.put_job_templates_id(id, location_id=location_id, organization_id=organization_id, job_template_name=job_template_name, job_template_description=job_template_description, job_template_job_category=job_template_job_category, job_template_description_format=job_template_description_format, job_template_template=job_template_template, job_template_provider_type=job_template_provider_type, job_template_snippet=job_template_snippet, job_template_audit_comment=job_template_audit_comment, job_template_locked=job_template_locked, job_template_effective_user_attributes_value=job_template_effective_user_attributes_value, job_template_effective_user_attributes_overridable=job_template_effective_user_attributes_overridable, job_template_effective_user_attributes_current_user=job_template_effective_user_attributes_current_user, job_template_location_ids=job_template_location_ids, job_template_organization_ids=job_template_organization_ids)
    except Exception as e:
        print("Exception when calling JobTemplatesApi->put_job_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **job_template_name** | **str**| Template name | [optional] 
 **job_template_description** | **str**|  | [optional] 
 **job_template_job_category** | **str**| Job category | [optional] 
 **job_template_description_format** | **str**| This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}. | [optional] 
 **job_template_template** | **str**|  | [optional] 
 **job_template_provider_type** | **str**| Provider type | [optional] 
 **job_template_snippet** | **bool**|  | [optional] 
 **job_template_audit_comment** | **str**|  | [optional] 
 **job_template_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **job_template_effective_user_attributes_value** | **str**| What user should be used to run the script (using sudo-like mechanisms) | [optional] 
 **job_template_effective_user_attributes_overridable** | **bool**| Whether it should be allowed to override the effective user from the invocation form. | [optional] 
 **job_template_effective_user_attributes_current_user** | **bool**| Whether the current user login should be used as the effective user | [optional] 
 **job_template_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **job_template_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

