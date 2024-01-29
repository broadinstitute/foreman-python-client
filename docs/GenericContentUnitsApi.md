# pyforeman.GenericContentUnitsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_units**](GenericContentUnitsApi.md#get_content_units) | **GET** /content_units | List content_units
[**get_content_units_compare**](GenericContentUnitsApi.md#get_content_units_compare) | **GET** /content_units/compare | List :resource
[**get_content_units_id**](GenericContentUnitsApi.md#get_content_units_id) | **GET** /content_units/{id} | Show a content unit
[**get_content_view_filters_content_view_filter_id_content_units**](GenericContentUnitsApi.md#get_content_view_filters_content_view_filter_id_content_units) | **GET** /content_view_filters/{content_view_filter_id}/content_units | List content_units
[**get_content_views_content_view_id_filters_filter_id_content_units**](GenericContentUnitsApi.md#get_content_views_content_view_id_filters_filter_id_content_units) | **GET** /content_views/{content_view_id}/filters/{filter_id}/content_units | List content_units
[**get_ostree_refs**](GenericContentUnitsApi.md#get_ostree_refs) | **GET** /ostree_refs | List ostree_refs
[**get_ostree_refs_id**](GenericContentUnitsApi.md#get_ostree_refs_id) | **GET** /ostree_refs/{id} | Show ostree ref
[**get_python_packages**](GenericContentUnitsApi.md#get_python_packages) | **GET** /python_packages | List python_packages
[**get_python_packages_id**](GenericContentUnitsApi.md#get_python_packages_id) | **GET** /python_packages/{id} | Show python package
[**get_repositories_repository_id_content_units**](GenericContentUnitsApi.md#get_repositories_repository_id_content_units) | **GET** /repositories/{repository_id}/content_units | List content_units
[**get_repositories_repository_id_content_units_id**](GenericContentUnitsApi.md#get_repositories_repository_id_content_units_id) | **GET** /repositories/{repository_id}/content_units/{id} | Show a content unit
[**get_repositories_repository_id_ostree_refs_id**](GenericContentUnitsApi.md#get_repositories_repository_id_ostree_refs_id) | **GET** /repositories/{repository_id}/ostree_refs/{id} | Show ostree ref
[**get_repositories_repository_id_python_packages_id**](GenericContentUnitsApi.md#get_repositories_repository_id_python_packages_id) | **GET** /repositories/{repository_id}/python_packages/{id} | Show python package


# **get_content_units**
> get_content_units(content_type, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content_units



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_type = 'content_type_example' # str | Possible values:
content_view_filter_id = 8.14 # float | content view filter identifier
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)
content_view_version_id = 8.14 # float | content view version identifier (optional)
content_view_filter_rule_id = 8.14 # float | content view filter rule identifier (optional)
environment_id = 8.14 # float | environment identifier (optional)
ids = ['ids_example'] # list[str] | ids to filter content by (optional)
include_filter_ids = true # bool | Includes associated content view filter ids in response (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content_units
    api_instance.get_content_units(content_type, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_content_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Possible values:  |
 **content_view_filter_id** | **float**| content view filter identifier |
 **repository_id** | **float**| repository identifier |
 **organization_id** | **float**| organization identifier | [optional]
 **content_view_version_id** | **float**| content view version identifier | [optional]
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional]
 **environment_id** | **float**| environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| ids to filter content by | [optional]
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional]
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

# **get_content_units_compare**
> get_content_units_compare(content_type, content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List :resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_type = 'content_type_example' # str | Possible values:
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view versions to compare (optional)
repository_id = 8.14 # float | Library repository id to restrict comparisons to (optional)
restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

try:
    # List :resource
    api_instance.get_content_units_compare(content_type, content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_content_units_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Possible values:  |
 **content_view_version_ids** | [**list[str]**](str.md)| content view versions to compare | [optional]
 **repository_id** | **float**| Library repository id to restrict comparisons to | [optional]
 **restrict_comparison** | **str**| Return same, different or all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_units_id**
> get_content_units_id(id, content_type, repository_id, organization_id=organization_id)

Show a content unit



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
id = 'id_example' # str | :a_resource identifier
content_type = 'content_type_example' # str | Possible values:
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a content unit
    api_instance.get_content_units_id(id, content_type, repository_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_content_units_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| :a_resource identifier |
 **content_type** | **str**| Possible values:  |
 **repository_id** | **float**| repository identifier |
 **organization_id** | **float**| organization identifier | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_view_filters_content_view_filter_id_content_units**
> get_content_view_filters_content_view_filter_id_content_units(content_view_filter_id, content_type, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content_units



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_view_filter_id = 8.14 # float | content view filter identifier
content_type = 'content_type_example' # str | Possible values:
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)
content_view_version_id = 8.14 # float | content view version identifier (optional)
content_view_filter_rule_id = 8.14 # float | content view filter rule identifier (optional)
environment_id = 8.14 # float | environment identifier (optional)
ids = ['ids_example'] # list[str] | ids to filter content by (optional)
include_filter_ids = true # bool | Includes associated content view filter ids in response (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content_units
    api_instance.get_content_view_filters_content_view_filter_id_content_units(content_view_filter_id, content_type, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_content_view_filters_content_view_filter_id_content_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| content view filter identifier |
 **content_type** | **str**| Possible values:  |
 **repository_id** | **float**| repository identifier |
 **organization_id** | **float**| organization identifier | [optional]
 **content_view_version_id** | **float**| content view version identifier | [optional]
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional]
 **environment_id** | **float**| environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| ids to filter content by | [optional]
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional]
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

# **get_content_views_content_view_id_filters_filter_id_content_units**
> get_content_views_content_view_id_filters_filter_id_content_units(content_view_id, filter_id, content_type, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content_units



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_view_id = 8.14 # float |
filter_id = 8.14 # float |
content_type = 'content_type_example' # str | Possible values:
content_view_filter_id = 8.14 # float | content view filter identifier
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)
content_view_version_id = 8.14 # float | content view version identifier (optional)
content_view_filter_rule_id = 8.14 # float | content view filter rule identifier (optional)
environment_id = 8.14 # float | environment identifier (optional)
ids = ['ids_example'] # list[str] | ids to filter content by (optional)
include_filter_ids = true # bool | Includes associated content view filter ids in response (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content_units
    api_instance.get_content_views_content_view_id_filters_filter_id_content_units(content_view_id, filter_id, content_type, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_content_views_content_view_id_filters_filter_id_content_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**|  |
 **filter_id** | **float**|  |
 **content_type** | **str**| Possible values:  |
 **content_view_filter_id** | **float**| content view filter identifier |
 **repository_id** | **float**| repository identifier |
 **organization_id** | **float**| organization identifier | [optional]
 **content_view_version_id** | **float**| content view version identifier | [optional]
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional]
 **environment_id** | **float**| environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| ids to filter content by | [optional]
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional]
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

# **get_ostree_refs**
> get_ostree_refs(content_type)

List ostree_refs



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_type = 'content_type_example' # str | Possible values:

try:
    # List ostree_refs
    api_instance.get_ostree_refs(content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_ostree_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ostree_refs_id**
> get_ostree_refs_id(id, content_type)

Show ostree ref



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
id = 8.14 # float |
content_type = 'content_type_example' # str | Possible values:

try:
    # Show ostree ref
    api_instance.get_ostree_refs_id(id, content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_ostree_refs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_packages**
> get_python_packages(content_type)

List python_packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
content_type = 'content_type_example' # str | Possible values:

try:
    # List python_packages
    api_instance.get_python_packages(content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_python_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_packages_id**
> get_python_packages_id(id, content_type)

Show python package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
id = 8.14 # float |
content_type = 'content_type_example' # str | Possible values:

try:
    # Show python package
    api_instance.get_python_packages_id(id, content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_python_packages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_repository_id_content_units**
> get_repositories_repository_id_content_units(repository_id, content_type, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content_units



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
repository_id = 8.14 # float | repository identifier
content_type = 'content_type_example' # str | Possible values:
content_view_filter_id = 8.14 # float | content view filter identifier
organization_id = 8.14 # float | organization identifier (optional)
content_view_version_id = 8.14 # float | content view version identifier (optional)
content_view_filter_rule_id = 8.14 # float | content view filter rule identifier (optional)
environment_id = 8.14 # float | environment identifier (optional)
ids = ['ids_example'] # list[str] | ids to filter content by (optional)
include_filter_ids = true # bool | Includes associated content view filter ids in response (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content_units
    api_instance.get_repositories_repository_id_content_units(repository_id, content_type, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_repositories_repository_id_content_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository identifier |
 **content_type** | **str**| Possible values:  |
 **content_view_filter_id** | **float**| content view filter identifier |
 **organization_id** | **float**| organization identifier | [optional]
 **content_view_version_id** | **float**| content view version identifier | [optional]
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional]
 **environment_id** | **float**| environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| ids to filter content by | [optional]
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional]
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

# **get_repositories_repository_id_content_units_id**
> get_repositories_repository_id_content_units_id(repository_id, id, content_type, organization_id=organization_id)

Show a content unit



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
repository_id = 8.14 # float | repository identifier
id = 'id_example' # str | :a_resource identifier
content_type = 'content_type_example' # str | Possible values:
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a content unit
    api_instance.get_repositories_repository_id_content_units_id(repository_id, id, content_type, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_repositories_repository_id_content_units_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository identifier |
 **id** | **str**| :a_resource identifier |
 **content_type** | **str**| Possible values:  |
 **organization_id** | **float**| organization identifier | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_repository_id_ostree_refs_id**
> get_repositories_repository_id_ostree_refs_id(repository_id, id, content_type)

Show ostree ref



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
repository_id = 8.14 # float |
id = 8.14 # float |
content_type = 'content_type_example' # str | Possible values:

try:
    # Show ostree ref
    api_instance.get_repositories_repository_id_ostree_refs_id(repository_id, id, content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_repositories_repository_id_ostree_refs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**|  |
 **id** | **float**|  |
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_repository_id_python_packages_id**
> get_repositories_repository_id_python_packages_id(repository_id, id, content_type)

Show python package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.GenericContentUnitsApi()
repository_id = 8.14 # float |
id = 8.14 # float |
content_type = 'content_type_example' # str | Possible values:

try:
    # Show python package
    api_instance.get_repositories_repository_id_python_packages_id(repository_id, id, content_type)
except ApiException as e:
    print("Exception when calling GenericContentUnitsApi->get_repositories_repository_id_python_packages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**|  |
 **id** | **float**|  |
 **content_type** | **str**| Possible values:  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
