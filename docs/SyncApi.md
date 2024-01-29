# foreman.SyncApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repositories_repository_id_sync**](SyncApi.md#get_repositories_repository_id_sync) | **GET** /repositories/{repository_id}/sync | Get status of synchronisation for given repository


# **get_repositories_repository_id_sync**
> get_repositories_repository_id_sync(repository_id)

Get status of synchronisation for given repository

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
    api_instance = foreman.SyncApi(api_client)
    repository_id = 3.4 # float | 

    try:
        # Get status of synchronisation for given repository
        api_instance.get_repositories_repository_id_sync(repository_id)
    except Exception as e:
        print("Exception when calling SyncApi->get_repositories_repository_id_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**|  | 

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

