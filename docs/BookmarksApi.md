# pyforeman.BookmarksApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bookmarks_id**](BookmarksApi.md#delete_bookmarks_id) | **DELETE** /bookmarks/{id} | Delete a bookmark
[**get_bookmarks**](BookmarksApi.md#get_bookmarks) | **GET** /bookmarks | List all bookmarks
[**get_bookmarks_id**](BookmarksApi.md#get_bookmarks_id) | **GET** /bookmarks/{id} | Show a bookmark
[**post_bookmarks**](BookmarksApi.md#post_bookmarks) | **POST** /bookmarks | Create a bookmark
[**put_bookmarks_id**](BookmarksApi.md#put_bookmarks_id) | **PUT** /bookmarks/{id} | Update a bookmark


# **delete_bookmarks_id**
> delete_bookmarks_id(id, location_id=location_id, organization_id=organization_id)

Delete a bookmark



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.BookmarksApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a bookmark
    api_instance.delete_bookmarks_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling BookmarksApi->delete_bookmarks_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmarks**
> get_bookmarks(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all bookmarks



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.BookmarksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all bookmarks
    api_instance.get_bookmarks(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling BookmarksApi->get_bookmarks: %s\n" % e)
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bookmarks_id**
> get_bookmarks_id(id, location_id=location_id, organization_id=organization_id)

Show a bookmark



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.BookmarksApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a bookmark
    api_instance.get_bookmarks_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling BookmarksApi->get_bookmarks_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bookmarks**
> post_bookmarks(bookmark_name, bookmark_controller, bookmark_query, location_id=location_id, organization_id=organization_id, bookmark_public=bookmark_public)

Create a bookmark



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.BookmarksApi()
bookmark_name = 'bookmark_name_example' # str |
bookmark_controller = 'bookmark_controller_example' # str |
bookmark_query = 'bookmark_query_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
bookmark_public = true # bool |  (optional)

try:
    # Create a bookmark
    api_instance.post_bookmarks(bookmark_name, bookmark_controller, bookmark_query, location_id=location_id, organization_id=organization_id, bookmark_public=bookmark_public)
except ApiException as e:
    print("Exception when calling BookmarksApi->post_bookmarks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmark_name** | **str**|  |
 **bookmark_controller** | **str**|  |
 **bookmark_query** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **bookmark_public** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bookmarks_id**
> put_bookmarks_id(id, location_id=location_id, organization_id=organization_id, bookmark_name=bookmark_name, bookmark_controller=bookmark_controller, bookmark_query=bookmark_query, bookmark_public=bookmark_public)

Update a bookmark



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.BookmarksApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
bookmark_name = 'bookmark_name_example' # str |  (optional)
bookmark_controller = 'bookmark_controller_example' # str |  (optional)
bookmark_query = 'bookmark_query_example' # str |  (optional)
bookmark_public = true # bool |  (optional)

try:
    # Update a bookmark
    api_instance.put_bookmarks_id(id, location_id=location_id, organization_id=organization_id, bookmark_name=bookmark_name, bookmark_controller=bookmark_controller, bookmark_query=bookmark_query, bookmark_public=bookmark_public)
except ApiException as e:
    print("Exception when calling BookmarksApi->put_bookmarks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **bookmark_name** | **str**|  | [optional]
 **bookmark_controller** | **str**|  | [optional]
 **bookmark_query** | **str**|  | [optional]
 **bookmark_public** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
