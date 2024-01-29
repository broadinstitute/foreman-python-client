# foreman.CommonParametersApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_common_parameters_id**](CommonParametersApi.md#delete_common_parameters_id) | **DELETE** /common_parameters/{id} | Delete a global parameter
[**get_common_parameters**](CommonParametersApi.md#get_common_parameters) | **GET** /common_parameters | List all global parameters
[**get_common_parameters_id**](CommonParametersApi.md#get_common_parameters_id) | **GET** /common_parameters/{id} | Show a global parameter
[**post_common_parameters**](CommonParametersApi.md#post_common_parameters) | **POST** /common_parameters | Create a global parameter
[**put_common_parameters_id**](CommonParametersApi.md#put_common_parameters_id) | **PUT** /common_parameters/{id} | Update a global parameter


# **delete_common_parameters_id**
> delete_common_parameters_id(id, location_id=location_id, organization_id=organization_id)

Delete a global parameter

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
    api_instance = foreman.CommonParametersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a global parameter
        api_instance.delete_common_parameters_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling CommonParametersApi->delete_common_parameters_id: %s\n" % e)
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

# **get_common_parameters**
> get_common_parameters(location_id=location_id, organization_id=organization_id, show_hidden=show_hidden, search=search, order=order, page=page, per_page=per_page)

List all global parameters

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
    api_instance = foreman.CommonParametersApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    show_hidden = True # bool | Display hidden values (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all global parameters
        api_instance.get_common_parameters(location_id=location_id, organization_id=organization_id, show_hidden=show_hidden, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling CommonParametersApi->get_common_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **show_hidden** | **bool**| Display hidden values | [optional] 
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

# **get_common_parameters_id**
> get_common_parameters_id(id, location_id=location_id, organization_id=organization_id, show_hidden=show_hidden)

Show a global parameter

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
    api_instance = foreman.CommonParametersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    show_hidden = True # bool | Display hidden values (optional)

    try:
        # Show a global parameter
        api_instance.get_common_parameters_id(id, location_id=location_id, organization_id=organization_id, show_hidden=show_hidden)
    except Exception as e:
        print("Exception when calling CommonParametersApi->get_common_parameters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **show_hidden** | **bool**| Display hidden values | [optional] 

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

# **post_common_parameters**
> post_common_parameters(common_parameter_name, common_parameter_value, common_parameter_parameter_type, location_id=location_id, organization_id=organization_id, common_parameter_hidden_value=common_parameter_hidden_value)

Create a global parameter

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
    api_instance = foreman.CommonParametersApi(api_client)
    common_parameter_name = 'common_parameter_name_example' # str | 
    common_parameter_value = 'common_parameter_value_example' # str | 
    common_parameter_parameter_type = 'common_parameter_parameter_type_example' # str | Type of value
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    common_parameter_hidden_value = True # bool |  (optional)

    try:
        # Create a global parameter
        api_instance.post_common_parameters(common_parameter_name, common_parameter_value, common_parameter_parameter_type, location_id=location_id, organization_id=organization_id, common_parameter_hidden_value=common_parameter_hidden_value)
    except Exception as e:
        print("Exception when calling CommonParametersApi->post_common_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_parameter_name** | **str**|  | 
 **common_parameter_value** | **str**|  | 
 **common_parameter_parameter_type** | **str**| Type of value | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **common_parameter_hidden_value** | **bool**|  | [optional] 

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

# **put_common_parameters_id**
> put_common_parameters_id(id, location_id=location_id, organization_id=organization_id, common_parameter_name=common_parameter_name, common_parameter_value=common_parameter_value, common_parameter_parameter_type=common_parameter_parameter_type, common_parameter_hidden_value=common_parameter_hidden_value)

Update a global parameter

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
    api_instance = foreman.CommonParametersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    common_parameter_name = 'common_parameter_name_example' # str |  (optional)
    common_parameter_value = 'common_parameter_value_example' # str |  (optional)
    common_parameter_parameter_type = 'common_parameter_parameter_type_example' # str | Type of value (optional)
    common_parameter_hidden_value = True # bool |  (optional)

    try:
        # Update a global parameter
        api_instance.put_common_parameters_id(id, location_id=location_id, organization_id=organization_id, common_parameter_name=common_parameter_name, common_parameter_value=common_parameter_value, common_parameter_parameter_type=common_parameter_parameter_type, common_parameter_hidden_value=common_parameter_hidden_value)
    except Exception as e:
        print("Exception when calling CommonParametersApi->put_common_parameters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **common_parameter_name** | **str**|  | [optional] 
 **common_parameter_value** | **str**|  | [optional] 
 **common_parameter_parameter_type** | **str**| Type of value | [optional] 
 **common_parameter_hidden_value** | **bool**|  | [optional] 

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

