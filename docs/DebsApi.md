# pyforeman.DebsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_view_filters_content_view_filter_id_debs**](DebsApi.md#get_content_view_filters_content_view_filter_id_debs) | **GET** /content_view_filters/{content_view_filter_id}/debs | List deb packages
[**get_content_views_content_view_id_filters_filter_id_debs**](DebsApi.md#get_content_views_content_view_id_filters_filter_id_debs) | **GET** /content_views/{content_view_id}/filters/{filter_id}/debs | List deb packages
[**get_debs**](DebsApi.md#get_debs) | **GET** /debs | List deb packages
[**get_debs_compare**](DebsApi.md#get_debs_compare) | **GET** /debs/compare | List deb packages
[**get_debs_id**](DebsApi.md#get_debs_id) | **GET** /debs/{id} | Show a deb package
[**get_repositories_repository_id_debs**](DebsApi.md#get_repositories_repository_id_debs) | **GET** /repositories/{repository_id}/debs | List deb packages
[**get_repositories_repository_id_debs_id**](DebsApi.md#get_repositories_repository_id_debs_id) | **GET** /repositories/{repository_id}/debs/{id} | Show a deb package


# **get_content_view_filters_content_view_filter_id_debs**
> get_content_view_filters_content_view_filter_id_debs(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List deb packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
content_view_filter_id = 8.14 # float | Content View Filter identifier
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Deb package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable deb packages for (optional)
packages_restrict_applicable = true # bool | Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return deb packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return deb packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List deb packages
    api_instance.get_content_view_filters_content_view_filter_id_debs(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling DebsApi->get_content_view_filters_content_view_filter_id_debs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Deb package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable deb packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return deb packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return deb packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_content_views_content_view_id_filters_filter_id_debs**
> get_content_views_content_view_id_filters_filter_id_debs(content_view_id, filter_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List deb packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
content_view_id = 8.14 # float |
filter_id = 8.14 # float |
content_view_filter_id = 8.14 # float | Content View Filter identifier
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Deb package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable deb packages for (optional)
packages_restrict_applicable = true # bool | Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return deb packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return deb packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List deb packages
    api_instance.get_content_views_content_view_id_filters_filter_id_debs(content_view_id, filter_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling DebsApi->get_content_views_content_view_id_filters_filter_id_debs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**|  |
 **filter_id** | **float**|  |
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Deb package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable deb packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return deb packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return deb packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_debs**
> get_debs(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List deb packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
content_view_filter_id = 8.14 # float | Content View Filter identifier
repository_id = 8.14 # float | Repository identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Deb package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable deb packages for (optional)
packages_restrict_applicable = true # bool | Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return deb packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return deb packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List deb packages
    api_instance.get_debs(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling DebsApi->get_debs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **repository_id** | **float**| Repository identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Deb package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable deb packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return deb packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return deb packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_debs_compare**
> get_debs_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List deb packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view versions to compare (optional)
repository_id = 8.14 # float | Library repository id to restrict comparisons to (optional)
restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

try:
    # List deb packages
    api_instance.get_debs_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
except ApiException as e:
    print("Exception when calling DebsApi->get_debs_compare: %s\n" % e)
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

# **get_debs_id**
> get_debs_id(id, repository_id, organization_id=organization_id)

Show a deb package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
id = 'id_example' # str | :a_resource identifier
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a deb package
    api_instance.get_debs_id(id, repository_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling DebsApi->get_debs_id: %s\n" % e)
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

# **get_repositories_repository_id_debs**
> get_repositories_repository_id_debs(repository_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List deb packages



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
repository_id = 8.14 # float | Repository identifier
content_view_filter_id = 8.14 # float | Content View Filter identifier
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
ids = ['ids_example'] # list[str] | Deb package identifiers to filter content by (optional)
host_id = 8.14 # float | Host id to list applicable deb packages for (optional)
packages_restrict_applicable = true # bool | Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
packages_restrict_upgradable = true # bool | Return deb packages that are upgradable on one or more hosts (optional)
packages_restrict_latest = true # bool | Return only the latest version of each package (optional)
available_for = 'available_for_example' # str | Return deb packages that can be added to the specified object.  Only the value 'content_view_version' is supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List deb packages
    api_instance.get_repositories_repository_id_debs(repository_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, environment_id=environment_id, ids=ids, host_id=host_id, packages_restrict_applicable=packages_restrict_applicable, packages_restrict_upgradable=packages_restrict_upgradable, packages_restrict_latest=packages_restrict_latest, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling DebsApi->get_repositories_repository_id_debs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| Repository identifier |
 **content_view_filter_id** | **float**| Content View Filter identifier |
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **ids** | [**list[str]**](str.md)| Deb package identifiers to filter content by | [optional]
 **host_id** | **float**| Host id to list applicable deb packages for | [optional]
 **packages_restrict_applicable** | **bool**| Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **packages_restrict_upgradable** | **bool**| Return deb packages that are upgradable on one or more hosts | [optional]
 **packages_restrict_latest** | **bool**| Return only the latest version of each package | [optional]
 **available_for** | **str**| Return deb packages that can be added to the specified object.  Only the value &#39;content_view_version&#39; is supported. | [optional]
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

# **get_repositories_repository_id_debs_id**
> get_repositories_repository_id_debs_id(repository_id, id, organization_id=organization_id)

Show a deb package



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DebsApi()
repository_id = 8.14 # float | repository identifier
id = 'id_example' # str | :a_resource identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a deb package
    api_instance.get_repositories_repository_id_debs_id(repository_id, id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling DebsApi->get_repositories_repository_id_debs_id: %s\n" % e)
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
