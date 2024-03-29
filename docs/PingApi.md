# pyforeman.PingApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_ping**](PingApi.md#get_api_ping) | **GET** /api/ping | Shows status of Foreman system and it&#39;s subcomponents
[**get_api_statuses**](PingApi.md#get_api_statuses) | **GET** /api/statuses | Shows status and version information of Foreman system and it&#39;s subcomponents
[**get_katello_api_ping**](PingApi.md#get_katello_api_ping) | **GET** /katello/api/ping | Shows status of Katello system and it&#39;s subcomponents
[**get_katello_api_status**](PingApi.md#get_katello_api_status) | **GET** /katello/api/status | Shows version information


# **get_api_ping**
> get_api_ping(location_id=location_id, organization_id=organization_id)

Shows status of Foreman system and it's subcomponents

This service is available for unauthenticated users

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PingApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Shows status of Foreman system and it's subcomponents
    api_instance.get_api_ping(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PingApi->get_api_ping: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_statuses**
> get_api_statuses(location_id=location_id, organization_id=organization_id)

Shows status and version information of Foreman system and it's subcomponents

This service is only available for authenticated users

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PingApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Shows status and version information of Foreman system and it's subcomponents
    api_instance.get_api_statuses(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PingApi->get_api_statuses: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_katello_api_ping**
> get_katello_api_ping(location_id=location_id, organization_id=organization_id)

Shows status of Katello system and it's subcomponents

This service is only available for authenticated users

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PingApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Shows status of Katello system and it's subcomponents
    api_instance.get_katello_api_ping(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PingApi->get_katello_api_ping: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_katello_api_status**
> get_katello_api_status(location_id=location_id, organization_id=organization_id)

Shows version information

This service is available for unauthenticated users

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PingApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Shows version information
    api_instance.get_katello_api_status(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PingApi->get_katello_api_status: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
