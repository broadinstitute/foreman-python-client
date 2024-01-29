# pyforeman.ContentUploadsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_repositories_repository_id_content_uploads_id**](ContentUploadsApi.md#delete_repositories_repository_id_content_uploads_id) | **DELETE** /repositories/{repository_id}/content_uploads/{id} | Delete an upload request
[**post_repositories_repository_id_content_uploads**](ContentUploadsApi.md#post_repositories_repository_id_content_uploads) | **POST** /repositories/{repository_id}/content_uploads | Create an upload request
[**put_repositories_repository_id_content_uploads_id**](ContentUploadsApi.md#put_repositories_repository_id_content_uploads_id) | **PUT** /repositories/{repository_id}/content_uploads/{id} | Upload a chunk of the file&#39;s content


# **delete_repositories_repository_id_content_uploads_id**
> delete_repositories_repository_id_content_uploads_id(repository_id, id)

Delete an upload request



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentUploadsApi()
repository_id = 8.14 # float | Repository id
id = 'id_example' # str | Upload request id

try:
    # Delete an upload request
    api_instance.delete_repositories_repository_id_content_uploads_id(repository_id, id)
except ApiException as e:
    print("Exception when calling ContentUploadsApi->delete_repositories_repository_id_content_uploads_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| Repository id |
 **id** | **str**| Upload request id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_repository_id_content_uploads**
> post_repositories_repository_id_content_uploads(repository_id, size, checksum=checksum, content_type=content_type)

Create an upload request



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentUploadsApi()
repository_id = 8.14 # float | repository id
size = 8.14 # float | Size of file to upload
checksum = 'checksum_example' # str | Checksum of file to upload (optional)
content_type = 'content_type_example' # str | content type ('deb', 'docker_manifest', 'file', 'ostree_ref', 'rpm', 'srpm') (optional)

try:
    # Create an upload request
    api_instance.post_repositories_repository_id_content_uploads(repository_id, size, checksum=checksum, content_type=content_type)
except ApiException as e:
    print("Exception when calling ContentUploadsApi->post_repositories_repository_id_content_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository id |
 **size** | **float**| Size of file to upload |
 **checksum** | **str**| Checksum of file to upload | [optional]
 **content_type** | **str**| content type (&#39;deb&#39;, &#39;docker_manifest&#39;, &#39;file&#39;, &#39;ostree_ref&#39;, &#39;rpm&#39;, &#39;srpm&#39;) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_repository_id_content_uploads_id**
> put_repositories_repository_id_content_uploads_id(repository_id, id, size, offset, content)

Upload a chunk of the file's content



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentUploadsApi()
repository_id = 8.14 # float | Repository id
id = 'id_example' # str | Upload request id
size = 8.14 # float | Size of file to upload
offset = 8.14 # float | The offset in the file where the content starts
content = '/path/to/file.txt' # file | The actual file contents

try:
    # Upload a chunk of the file's content
    api_instance.put_repositories_repository_id_content_uploads_id(repository_id, id, size, offset, content)
except ApiException as e:
    print("Exception when calling ContentUploadsApi->put_repositories_repository_id_content_uploads_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| Repository id |
 **id** | **str**| Upload request id |
 **size** | **float**| Size of file to upload |
 **offset** | **float**| The offset in the file where the content starts |
 **content** | **file**| The actual file contents |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
