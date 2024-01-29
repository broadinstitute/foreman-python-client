# pyforeman.ErrataApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_errata**](ErrataApi.md#get_errata) | **GET** /errata | List errata
[**get_errata_compare**](ErrataApi.md#get_errata_compare) | **GET** /errata/compare | List errata
[**get_errata_id**](ErrataApi.md#get_errata_id) | **GET** /errata/{id} | Show an erratum
[**get_repositories_repository_id_errata_id**](ErrataApi.md#get_repositories_repository_id_errata_id) | **GET** /repositories/{repository_id}/errata/{id} | Show an erratum


# **get_errata**
> get_errata(organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_id=content_view_filter_id, repository_id=repository_id, environment_id=environment_id, cve=cve, host_id=host_id, errata_restrict_applicable=errata_restrict_applicable, errata_restrict_installable=errata_restrict_installable, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List errata



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ErrataApi()
organization_id = 8.14 # float | Organization identifier (optional)
content_view_version_id = 8.14 # float | Content View Version identifier (optional)
content_view_filter_id = 8.14 # float | Content View Filter identifier (optional)
repository_id = 8.14 # float | Repository identifier (optional)
environment_id = 8.14 # float | Environment identifier (optional)
cve = 'cve_example' # str | CVE identifier (optional)
host_id = 8.14 # float | Host id to list applicable errata for (optional)
errata_restrict_applicable = true # bool | Return errata that are applicable to one or more hosts (defaults to true if host_id is specified) (optional)
errata_restrict_installable = true # bool | Return errata that are upgradable on one or more hosts (optional)
available_for = 'available_for_example' # str | Return errata that can be added to the specified object.  The values 'content_view_version' and 'content_view_filter are supported. (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List errata
    api_instance.get_errata(organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_id=content_view_filter_id, repository_id=repository_id, environment_id=environment_id, cve=cve, host_id=host_id, errata_restrict_applicable=errata_restrict_applicable, errata_restrict_installable=errata_restrict_installable, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling ErrataApi->get_errata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | [optional]
 **content_view_version_id** | **float**| Content View Version identifier | [optional]
 **content_view_filter_id** | **float**| Content View Filter identifier | [optional]
 **repository_id** | **float**| Repository identifier | [optional]
 **environment_id** | **float**| Environment identifier | [optional]
 **cve** | **str**| CVE identifier | [optional]
 **host_id** | **float**| Host id to list applicable errata for | [optional]
 **errata_restrict_applicable** | **bool**| Return errata that are applicable to one or more hosts (defaults to true if host_id is specified) | [optional]
 **errata_restrict_installable** | **bool**| Return errata that are upgradable on one or more hosts | [optional]
 **available_for** | **str**| Return errata that can be added to the specified object.  The values &#39;content_view_version&#39; and &#39;content_view_filter are supported. | [optional]
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

# **get_errata_compare**
> get_errata_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List errata



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ErrataApi()
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view versions to compare (optional)
repository_id = 8.14 # float | Library repository id to restrict comparisons to (optional)
restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

try:
    # List errata
    api_instance.get_errata_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
except ApiException as e:
    print("Exception when calling ErrataApi->get_errata_compare: %s\n" % e)
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

# **get_errata_id**
> get_errata_id(id, repository_id, organization_id=organization_id)

Show an erratum



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ErrataApi()
id = 'id_example' # str | :a_resource identifier
repository_id = 8.14 # float | repository identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show an erratum
    api_instance.get_errata_id(id, repository_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ErrataApi->get_errata_id: %s\n" % e)
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

# **get_repositories_repository_id_errata_id**
> get_repositories_repository_id_errata_id(repository_id, id, organization_id=organization_id)

Show an erratum



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ErrataApi()
repository_id = 8.14 # float | repository identifier
id = 'id_example' # str | :a_resource identifier
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show an erratum
    api_instance.get_repositories_repository_id_errata_id(repository_id, id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ErrataApi->get_repositories_repository_id_errata_id: %s\n" % e)
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
