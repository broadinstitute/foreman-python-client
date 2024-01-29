# foreman.SettingsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings | List all settings
[**get_settings_id**](SettingsApi.md#get_settings_id) | **GET** /settings/{id} | Show a setting
[**put_settings_id**](SettingsApi.md#put_settings_id) | **PUT** /settings/{id} | Update a setting


# **get_settings**
> get_settings(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all settings

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
    api_instance = foreman.SettingsApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all settings
        api_instance.get_settings(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_settings_id**
> SettingParams get_settings_id(id, location_id=location_id, organization_id=organization_id)

Show a setting

### Example


```python
import time
import os
import foreman
from foreman.models.setting_params import SettingParams
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
    api_instance = foreman.SettingsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a setting
        api_response = api_instance.get_settings_id(id, location_id=location_id, organization_id=organization_id)
        print("The response of SettingsApi->get_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

### Return type

[**SettingParams**](SettingParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_settings_id**
> SettingParams put_settings_id(id, location_id=location_id, organization_id=organization_id, setting_value=setting_value)

Update a setting

### Example


```python
import time
import os
import foreman
from foreman.models.setting_params import SettingParams
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
    api_instance = foreman.SettingsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    setting_value = 'setting_value_example' # str |  (optional)

    try:
        # Update a setting
        api_response = api_instance.put_settings_id(id, location_id=location_id, organization_id=organization_id, setting_value=setting_value)
        print("The response of SettingsApi->put_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->put_settings_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **setting_value** | **str**|  | [optional] 

### Return type

[**SettingParams**](SettingParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the updated setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

