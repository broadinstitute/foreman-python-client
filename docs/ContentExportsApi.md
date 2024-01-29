# pyforeman.ContentExportsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_exports**](ContentExportsApi.md#get_content_exports) | **GET** /content_exports | List export histories
[**post_content_exports_library**](ContentExportsApi.md#post_content_exports_library) | **POST** /content_exports/library | Performs a full-export of the repositories in library.
[**post_content_exports_repository**](ContentExportsApi.md#post_content_exports_repository) | **POST** /content_exports/repository | Performs a full-export of the repository in library.
[**post_content_exports_version**](ContentExportsApi.md#post_content_exports_version) | **POST** /content_exports/version | Performs a full-export of a content view version.


# **get_content_exports**
> get_content_exports(content_view_version_id=content_view_version_id, content_view_id=content_view_id, destination_server=destination_server, organization_id=organization_id, id=id, type=type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List export histories



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportsApi()
content_view_version_id = 8.14 # float | Content view version identifier (optional)
content_view_id = 8.14 # float | Content view identifier (optional)
destination_server = 'destination_server_example' # str | Destination Server name (optional)
organization_id = 8.14 # float | Organization identifier (optional)
id = 8.14 # float | Content view version export history identifier (optional)
type = 'type_example' # str | Export Types (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List export histories
    api_instance.get_content_exports(content_view_version_id=content_view_version_id, content_view_id=content_view_id, destination_server=destination_server, organization_id=organization_id, id=id, type=type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling ContentExportsApi->get_content_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_version_id** | **float**| Content view version identifier | [optional]
 **content_view_id** | **float**| Content view identifier | [optional]
 **destination_server** | **str**| Destination Server name | [optional]
 **organization_id** | **float**| Organization identifier | [optional]
 **id** | **float**| Content view version export history identifier | [optional]
 **type** | **str**| Export Types | [optional]
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_exports_library**
> post_content_exports_library(organization_id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format)

Performs a full-export of the repositories in library.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportsApi()
organization_id = 8.14 # float | Organization identifier
fail_on_missing_content = true # bool | Fails if any of the repositories belonging to this organization are unexportable. False by default. (optional)
destination_server = 'destination_server_example' # str | Destination Server name (optional)
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)

try:
    # Performs a full-export of the repositories in library.
    api_instance.post_content_exports_library(organization_id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format)
except ApiException as e:
    print("Exception when calling ContentExportsApi->post_content_exports_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier |
 **fail_on_missing_content** | **bool**| Fails if any of the repositories belonging to this organization are unexportable. False by default. | [optional]
 **destination_server** | **str**| Destination Server name | [optional]
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_exports_repository**
> post_content_exports_repository(id, chunk_size_gb=chunk_size_gb, format=format)

Performs a full-export of the repository in library.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportsApi()
id = 8.14 # float | Repository identifier
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)

try:
    # Performs a full-export of the repository in library.
    api_instance.post_content_exports_repository(id, chunk_size_gb=chunk_size_gb, format=format)
except ApiException as e:
    print("Exception when calling ContentExportsApi->post_content_exports_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Repository identifier |
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_exports_version**
> post_content_exports_version(id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format)

Performs a full-export of a content view version.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportsApi()
id = 8.14 # float | Content view version identifier
fail_on_missing_content = true # bool | Fails if any of the repositories belonging to this version are unexportable. False by default. (optional)
destination_server = 'destination_server_example' # str | Destination Server name (optional)
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)

try:
    # Performs a full-export of a content view version.
    api_instance.post_content_exports_version(id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format)
except ApiException as e:
    print("Exception when calling ContentExportsApi->post_content_exports_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier |
 **fail_on_missing_content** | **bool**| Fails if any of the repositories belonging to this version are unexportable. False by default. | [optional]
 **destination_server** | **str**| Destination Server name | [optional]
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
