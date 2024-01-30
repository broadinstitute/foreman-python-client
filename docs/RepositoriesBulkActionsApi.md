# pyforeman.RepositoriesBulkActionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_repositories_bulk_reclaim_space**](RepositoriesBulkActionsApi.md#post_repositories_bulk_reclaim_space) | **POST** /repositories/bulk/reclaim_space | Reclaim space from On Demand repositories
[**post_repositories_bulk_sync**](RepositoriesBulkActionsApi.md#post_repositories_bulk_sync) | **POST** /repositories/bulk/sync | Synchronize repository
[**put_repositories_bulk_destroy**](RepositoriesBulkActionsApi.md#put_repositories_bulk_destroy) | **PUT** /repositories/bulk/destroy | Destroy one or more repositories


# **post_repositories_bulk_reclaim_space**
> post_repositories_bulk_reclaim_space(ids)

Reclaim space from On Demand repositories



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesBulkActionsApi()
ids = ['ids_example'] # list[str] | List of repository ids

try:
    # Reclaim space from On Demand repositories
    api_instance.post_repositories_bulk_reclaim_space(ids)
except ApiException as e:
    print("Exception when calling RepositoriesBulkActionsApi->post_repositories_bulk_reclaim_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of repository ids |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_bulk_sync**
> post_repositories_bulk_sync(ids)

Synchronize repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesBulkActionsApi()
ids = ['ids_example'] # list[str] | List of repository ids

try:
    # Synchronize repository
    api_instance.post_repositories_bulk_sync(ids)
except ApiException as e:
    print("Exception when calling RepositoriesBulkActionsApi->post_repositories_bulk_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of repository ids |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_bulk_destroy**
> put_repositories_bulk_destroy(ids)

Destroy one or more repositories



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesBulkActionsApi()
ids = ['ids_example'] # list[str] | List of repository ids

try:
    # Destroy one or more repositories
    api_instance.put_repositories_bulk_destroy(ids)
except ApiException as e:
    print("Exception when calling RepositoriesBulkActionsApi->put_repositories_bulk_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of repository ids |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
