# pyforeman.SyncApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repositories_repository_id_sync**](SyncApi.md#get_repositories_repository_id_sync) | **GET** /repositories/{repository_id}/sync | Get status of synchronisation for given repository


# **get_repositories_repository_id_sync**
> get_repositories_repository_id_sync(repository_id)

Get status of synchronisation for given repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SyncApi()
repository_id = 8.14 # float |

try:
    # Get status of synchronisation for given repository
    api_instance.get_repositories_repository_id_sync(repository_id)
except ApiException as e:
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
