# foreman.TablePreferencesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_user_id_table_preferences_name**](TablePreferencesApi.md#delete_users_user_id_table_preferences_name) | **DELETE** /users/{user_id}/table_preferences/{name} | Delete a table preference for a given table
[**get_users_user_id_table_preferences**](TablePreferencesApi.md#get_users_user_id_table_preferences) | **GET** /users/{user_id}/table_preferences | List of table preferences for a user
[**get_users_user_id_table_preferences_name**](TablePreferencesApi.md#get_users_user_id_table_preferences_name) | **GET** /users/{user_id}/table_preferences/{name} | Table preference details of a given table
[**post_users_user_id_table_preferences**](TablePreferencesApi.md#post_users_user_id_table_preferences) | **POST** /users/{user_id}/table_preferences | Creates a table preference for a given table
[**put_users_user_id_table_preferences_name**](TablePreferencesApi.md#put_users_user_id_table_preferences_name) | **PUT** /users/{user_id}/table_preferences/{name} | Updates a table preference for a given table


# **delete_users_user_id_table_preferences_name**
> delete_users_user_id_table_preferences_name(user_id, name, location_id=location_id, organization_id=organization_id)

Delete a table preference for a given table

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
    api_instance = foreman.TablePreferencesApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    name = 'name_example' # str | Name of the table
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a table preference for a given table
        api_instance.delete_users_user_id_table_preferences_name(user_id, name, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling TablePreferencesApi->delete_users_user_id_table_preferences_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
 **name** | **str**| Name of the table | 
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

# **get_users_user_id_table_preferences**
> get_users_user_id_table_preferences(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of table preferences for a user

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
    api_instance = foreman.TablePreferencesApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List of table preferences for a user
        api_instance.get_users_user_id_table_preferences(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling TablePreferencesApi->get_users_user_id_table_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
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

# **get_users_user_id_table_preferences_name**
> get_users_user_id_table_preferences_name(user_id, name, location_id=location_id, organization_id=organization_id)

Table preference details of a given table

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
    api_instance = foreman.TablePreferencesApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    name = 'name_example' # str | Name of the table
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Table preference details of a given table
        api_instance.get_users_user_id_table_preferences_name(user_id, name, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling TablePreferencesApi->get_users_user_id_table_preferences_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
 **name** | **str**| Name of the table | 
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

# **post_users_user_id_table_preferences**
> post_users_user_id_table_preferences(user_id, name, columns, location_id=location_id, organization_id=organization_id)

Creates a table preference for a given table

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
    api_instance = foreman.TablePreferencesApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    name = 'name_example' # str | Name of the table
    columns = ['columns_example'] # List[str] | List of user selected columns
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Creates a table preference for a given table
        api_instance.post_users_user_id_table_preferences(user_id, name, columns, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling TablePreferencesApi->post_users_user_id_table_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
 **name** | **str**| Name of the table | 
 **columns** | [**List[str]**](str.md)| List of user selected columns | 
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

# **put_users_user_id_table_preferences_name**
> put_users_user_id_table_preferences_name(user_id, name, columns, location_id=location_id, organization_id=organization_id)

Updates a table preference for a given table

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
    api_instance = foreman.TablePreferencesApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    name = 'name_example' # str | Name of the table
    columns = ['columns_example'] # List[str] | List of user selected columns
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Updates a table preference for a given table
        api_instance.put_users_user_id_table_preferences_name(user_id, name, columns, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling TablePreferencesApi->put_users_user_id_table_preferences_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
 **name** | **str**| Name of the table | 
 **columns** | [**List[str]**](str.md)| List of user selected columns | 
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

