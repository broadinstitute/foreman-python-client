# pyforeman.PackagesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_view_filters_content_view_filter_id_resource_id**](PackagesApi.md#get_content_view_filters_content_view_filter_id_resource_id) | **GET** /content_view_filters/{content_view_filter_id}/{resource_id} | List :resource_id
[**get_content_views_content_view_id_filters_filter_id_resource_id**](PackagesApi.md#get_content_views_content_view_id_filters_filter_id_resource_id) | **GET** /content_views/{content_view_id}/filters/{filter_id}/{resource_id} | List :resource_id
[**get_packages**](PackagesApi.md#get_packages) | **GET** /packages | List packages
[**get_packages_compare**](PackagesApi.md#get_packages_compare) | **GET** /packages/compare | List packages
[**get_packages_id**](PackagesApi.md#get_packages_id) | **GET** /packages/{id} | Show a package
[**get_repositories_repository_id_packages_id**](PackagesApi.md#get_repositories_repository_id_packages_id) | **GET** /repositories/{repository_id}/packages/{id} | Show a package
[**get_repositories_repository_id_resource_id**](PackagesApi.md#get_repositories_repository_id_resource_id) | **GET** /repositories/{repository_id}/{resource_id} | List :resource_id


# **get_content_view_filters_content_view_filter_id_resource_id**
> get_content_view_filters_content_view_filter_id_resource_id(content_view_filter_id, resource_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List :resource_id



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
content_view_filter_id = 8.14 # float | Content View Filter identifier
resource_id = 8.14 # float |
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable packages for (optional)
packages_restrict_applicable = true # bool | Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List :resource_id
    api_instance.get_content_view_filters_content_view_filter_id_resource_id(content_view_filter_id, resource_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling PackagesApi->get_content_view_filters_content_view_filter_id_resource_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **resource_id** | **float**|  |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_content_views_content_view_id_filters_filter_id_resource_id**
> get_content_views_content_view_id_filters_filter_id_resource_id(content_view_id, filter_id, resource_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List :resource_id



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
content_view_id = 8.14 # float |
filter_id = 8.14 # float |
resource_id = 8.14 # float |
content_view_filter_id = 8.14 # float | Content View Filter identifier
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable packages for (optional)
packages_restrict_applicable = true # bool | Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List :resource_id
    api_instance.get_content_views_content_view_id_filters_filter_id_resource_id(content_view_id, filter_id, resource_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling PackagesApi->get_content_views_content_view_id_filters_filter_id_resource_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**|  |
 **filter_id** | **float**|  |
 **resource_id** | **float**|  |
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_packages**
> get_packages(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
content_view_filter_id = 8.14 # float | Content View Filter identifier
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable packages for (optional)
packages_restrict_applicable = true # bool | Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List packages
    api_instance.get_packages(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling PackagesApi->get_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_packages_compare**
> get_packages_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view versions to compare (optional)
repository_id = 8.14 # float | Library repository id to restrict comparisons to (optional)
restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

try:
    # List packages
    api_instance.get_packages_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
except ApiException as e:
    print("Exception when calling PackagesApi->get_packages_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_packages_id**
> get_packages_id(id, repository_id, organization_id=organization_id)

Show a package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
id = 'id_example' # str | :a_resource identifier
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a package
    api_instance.get_packages_id(id, repository_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PackagesApi->get_packages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| :a_resource identifier |
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

# **get_repositories_repository_id_packages_id**
> get_repositories_repository_id_packages_id(repository_id, id, organization_id=organization_id)

Show a package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
repository_id = 8.14 # float | repository identifier
id = 'id_example' # str | :a_resource identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a package
    api_instance.get_repositories_repository_id_packages_id(repository_id, id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling PackagesApi->get_repositories_repository_id_packages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository identifier |
 **id** | **str**| :a_resource identifier |
 **organization_id** | **float**| organization identifier | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_repository_id_resource_id**
> get_repositories_repository_id_resource_id(repository_id, resource_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List :resource_id



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.PackagesApi()
repository_id = 8.14 # float | Repository identifier
resource_id = 8.14 # float |
content_view_filter_id = 8.14 # float | Content View Filter identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable packages for (optional)
packages_restrict_applicable = true # bool | Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List :resource_id
    api_instance.get_repositories_repository_id_resource_id(repository_id, resource_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling PackagesApi->get_repositories_repository_id_resource_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| Repository identifier |
 **resource_id** | **float**|  |
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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
