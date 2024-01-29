# foreman.ContentViewHistoriesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_views_id_history**](ContentViewHistoriesApi.md#get_content_views_id_history) | **GET** /content_views/{id}/history | Show a content view&#39;s history


# **get_content_views_id_history**
> get_content_views_id_history(id)

Show a content view's history

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
    api_instance = foreman.ContentViewHistoriesApi(api_client)
    id = 3.4 # float | content view numeric identifier

    try:
        # Show a content view's history
        api_instance.get_content_views_id_history(id)
    except Exception as e:
        print("Exception when calling ContentViewHistoriesApi->get_content_views_id_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier | 

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

