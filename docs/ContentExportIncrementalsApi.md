# pyforeman.ContentExportIncrementalsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_content_export_incrementals_library**](ContentExportIncrementalsApi.md#post_content_export_incrementals_library) | **POST** /content_export_incrementals/library | Performs an incremental-export of the repositories in library.
[**post_content_export_incrementals_repository**](ContentExportIncrementalsApi.md#post_content_export_incrementals_repository) | **POST** /content_export_incrementals/repository | Performs a incremental-export of the repository in library.
[**post_content_export_incrementals_version**](ContentExportIncrementalsApi.md#post_content_export_incrementals_version) | **POST** /content_export_incrementals/version | Performs an incremental-export of a content view version.


# **post_content_export_incrementals_library**
> post_content_export_incrementals_library(organization_id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)

Performs an incremental-export of the repositories in library.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportIncrementalsApi()
organization_id = 8.14 # float | Organization identifier
fail_on_missing_content = true # bool | Fails if any of the repositories belonging to this organization are unexportable. False by default. (optional)
destination_server = 'destination_server_example' # str | Destination Server name (optional)
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)
from_history_id = 8.14 # float | Export history identifier used for incremental export. If not provided the most recent export history will be used. (optional)

try:
    # Performs an incremental-export of the repositories in library.
    api_instance.post_content_export_incrementals_library(organization_id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)
except ApiException as e:
    print("Exception when calling ContentExportIncrementalsApi->post_content_export_incrementals_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier |
 **fail_on_missing_content** | **bool**| Fails if any of the repositories belonging to this organization are unexportable. False by default. | [optional]
 **destination_server** | **str**| Destination Server name | [optional]
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]
 **from_history_id** | **float**| Export history identifier used for incremental export. If not provided the most recent export history will be used. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_export_incrementals_repository**
> post_content_export_incrementals_repository(id, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)

Performs a incremental-export of the repository in library.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportIncrementalsApi()
id = 8.14 # float | Repository identifier
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)
from_history_id = 8.14 # float | Export history identifier used for incremental export. If not provided the most recent export history will be used. (optional)

try:
    # Performs a incremental-export of the repository in library.
    api_instance.post_content_export_incrementals_repository(id, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)
except ApiException as e:
    print("Exception when calling ContentExportIncrementalsApi->post_content_export_incrementals_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Repository identifier |
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]
 **from_history_id** | **float**| Export history identifier used for incremental export. If not provided the most recent export history will be used. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_export_incrementals_version**
> post_content_export_incrementals_version(id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)

Performs an incremental-export of a content view version.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentExportIncrementalsApi()
id = 8.14 # float | Content view version identifier
fail_on_missing_content = true # bool | Fails if any of the repositories belonging to this version are unexportable. False by default. (optional)
destination_server = 'destination_server_example' # str | Destination Server name (optional)
chunk_size_gb = 8.14 # float | Split the exported content into archives no greater than the specified size in gigabytes. (optional)
format = 'format_example' # str | Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. (optional)
from_history_id = 8.14 # float | Export history identifier used for incremental export. If not provided the most recent export history will be used. (optional)

try:
    # Performs an incremental-export of a content view version.
    api_instance.post_content_export_incrementals_version(id, fail_on_missing_content=fail_on_missing_content, destination_server=destination_server, chunk_size_gb=chunk_size_gb, format=format, from_history_id=from_history_id)
except ApiException as e:
    print("Exception when calling ContentExportIncrementalsApi->post_content_export_incrementals_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier |
 **fail_on_missing_content** | **bool**| Fails if any of the repositories belonging to this version are unexportable. False by default. | [optional]
 **destination_server** | **str**| Destination Server name | [optional]
 **chunk_size_gb** | **float**| Split the exported content into archives no greater than the specified size in gigabytes. | [optional]
 **format** | **str**| Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version  and exported content needs to be one of yum, file, ansible_collection, docker repositories. | [optional]
 **from_history_id** | **float**| Export history identifier used for incremental export. If not provided the most recent export history will be used. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
