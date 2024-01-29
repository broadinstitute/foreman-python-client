# foreman.ForeignInputSetsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_templates_template_id_foreign_input_sets_id**](ForeignInputSetsApi.md#delete_templates_template_id_foreign_input_sets_id) | **DELETE** /templates/{template_id}/foreign_input_sets/{id} | Delete a foreign input set
[**get_templates_template_id_foreign_input_sets**](ForeignInputSetsApi.md#get_templates_template_id_foreign_input_sets) | **GET** /templates/{template_id}/foreign_input_sets | List foreign input sets
[**get_templates_template_id_foreign_input_sets_id**](ForeignInputSetsApi.md#get_templates_template_id_foreign_input_sets_id) | **GET** /templates/{template_id}/foreign_input_sets/{id} | Show foreign input set details
[**post_templates_template_id_foreign_input_sets**](ForeignInputSetsApi.md#post_templates_template_id_foreign_input_sets) | **POST** /templates/{template_id}/foreign_input_sets | Create a foreign input set
[**put_templates_template_id_foreign_input_sets_id**](ForeignInputSetsApi.md#put_templates_template_id_foreign_input_sets_id) | **PUT** /templates/{template_id}/foreign_input_sets/{id} | Update a foreign input set


# **delete_templates_template_id_foreign_input_sets_id**
> delete_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id)

Delete a foreign input set

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
    api_instance = foreman.ForeignInputSetsApi(api_client)
    template_id = 'template_id_example' # str | 
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a foreign input set
        api_instance.delete_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ForeignInputSetsApi->delete_templates_template_id_foreign_input_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
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

# **get_templates_template_id_foreign_input_sets**
> get_templates_template_id_foreign_input_sets(template_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List foreign input sets

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
    api_instance = foreman.ForeignInputSetsApi(api_client)
    template_id = 'template_id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List foreign input sets
        api_instance.get_templates_template_id_foreign_input_sets(template_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ForeignInputSetsApi->get_templates_template_id_foreign_input_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
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

# **get_templates_template_id_foreign_input_sets_id**
> get_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id)

Show foreign input set details

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
    api_instance = foreman.ForeignInputSetsApi(api_client)
    template_id = 'template_id_example' # str | 
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show foreign input set details
        api_instance.get_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ForeignInputSetsApi->get_templates_template_id_foreign_input_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
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

# **post_templates_template_id_foreign_input_sets**
> post_templates_template_id_foreign_input_sets(template_id, foreign_input_set_target_template_id, location_id=location_id, organization_id=organization_id, foreign_input_set_include_all=foreign_input_set_include_all, foreign_input_set_include=foreign_input_set_include, foreign_input_set_exclude=foreign_input_set_exclude, foreign_input_set_description=foreign_input_set_description)

Create a foreign input set

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
    api_instance = foreman.ForeignInputSetsApi(api_client)
    template_id = 'template_id_example' # str | 
    foreign_input_set_target_template_id = 'foreign_input_set_target_template_id_example' # str | Target template ID
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    foreign_input_set_include_all = True # bool | Include all inputs from the foreign template (optional)
    foreign_input_set_include = 'foreign_input_set_include_example' # str | A comma separated list of input names to be included from the foreign template. (optional)
    foreign_input_set_exclude = 'foreign_input_set_exclude_example' # str | A comma separated list of input names to be included from the foreign template. (optional)
    foreign_input_set_description = 'foreign_input_set_description_example' # str | Input set description (optional)

    try:
        # Create a foreign input set
        api_instance.post_templates_template_id_foreign_input_sets(template_id, foreign_input_set_target_template_id, location_id=location_id, organization_id=organization_id, foreign_input_set_include_all=foreign_input_set_include_all, foreign_input_set_include=foreign_input_set_include, foreign_input_set_exclude=foreign_input_set_exclude, foreign_input_set_description=foreign_input_set_description)
    except Exception as e:
        print("Exception when calling ForeignInputSetsApi->post_templates_template_id_foreign_input_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **foreign_input_set_target_template_id** | **str**| Target template ID | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **foreign_input_set_include_all** | **bool**| Include all inputs from the foreign template | [optional] 
 **foreign_input_set_include** | **str**| A comma separated list of input names to be included from the foreign template. | [optional] 
 **foreign_input_set_exclude** | **str**| A comma separated list of input names to be included from the foreign template. | [optional] 
 **foreign_input_set_description** | **str**| Input set description | [optional] 

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

# **put_templates_template_id_foreign_input_sets_id**
> put_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id, foreign_input_set_target_template_id=foreign_input_set_target_template_id, foreign_input_set_include_all=foreign_input_set_include_all, foreign_input_set_include=foreign_input_set_include, foreign_input_set_exclude=foreign_input_set_exclude, foreign_input_set_description=foreign_input_set_description)

Update a foreign input set

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
    api_instance = foreman.ForeignInputSetsApi(api_client)
    template_id = 'template_id_example' # str | 
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    foreign_input_set_target_template_id = 'foreign_input_set_target_template_id_example' # str | Target template ID (optional)
    foreign_input_set_include_all = True # bool | Include all inputs from the foreign template (optional)
    foreign_input_set_include = 'foreign_input_set_include_example' # str | A comma separated list of input names to be included from the foreign template. (optional)
    foreign_input_set_exclude = 'foreign_input_set_exclude_example' # str | A comma separated list of input names to be included from the foreign template. (optional)
    foreign_input_set_description = 'foreign_input_set_description_example' # str | Input set description (optional)

    try:
        # Update a foreign input set
        api_instance.put_templates_template_id_foreign_input_sets_id(template_id, id, location_id=location_id, organization_id=organization_id, foreign_input_set_target_template_id=foreign_input_set_target_template_id, foreign_input_set_include_all=foreign_input_set_include_all, foreign_input_set_include=foreign_input_set_include, foreign_input_set_exclude=foreign_input_set_exclude, foreign_input_set_description=foreign_input_set_description)
    except Exception as e:
        print("Exception when calling ForeignInputSetsApi->put_templates_template_id_foreign_input_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **foreign_input_set_target_template_id** | **str**| Target template ID | [optional] 
 **foreign_input_set_include_all** | **bool**| Include all inputs from the foreign template | [optional] 
 **foreign_input_set_include** | **str**| A comma separated list of input names to be included from the foreign template. | [optional] 
 **foreign_input_set_exclude** | **str**| A comma separated list of input names to be included from the foreign template. | [optional] 
 **foreign_input_set_description** | **str**| Input set description | [optional] 

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

