# foreman.ContentViewFiltersApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content_view_filters_id**](ContentViewFiltersApi.md#delete_content_view_filters_id) | **DELETE** /content_view_filters/{id} | delete a filter
[**delete_content_views_content_view_id_filters_id**](ContentViewFiltersApi.md#delete_content_views_content_view_id_filters_id) | **DELETE** /content_views/{content_view_id}/filters/{id} | delete a filter
[**get_content_view_filters**](ContentViewFiltersApi.md#get_content_view_filters) | **GET** /content_view_filters | list filters
[**get_content_view_filters_id**](ContentViewFiltersApi.md#get_content_view_filters_id) | **GET** /content_view_filters/{id} | show filter info
[**get_content_views_content_view_id_filters**](ContentViewFiltersApi.md#get_content_views_content_view_id_filters) | **GET** /content_views/{content_view_id}/filters | list filters
[**get_content_views_content_view_id_filters_id**](ContentViewFiltersApi.md#get_content_views_content_view_id_filters_id) | **GET** /content_views/{content_view_id}/filters/{id} | show filter info
[**post_content_view_filters**](ContentViewFiltersApi.md#post_content_view_filters) | **POST** /content_view_filters | create a filter for a content view
[**post_content_views_content_view_id_filters**](ContentViewFiltersApi.md#post_content_views_content_view_id_filters) | **POST** /content_views/{content_view_id}/filters | create a filter for a content view
[**put_content_view_filters_id**](ContentViewFiltersApi.md#put_content_view_filters_id) | **PUT** /content_view_filters/{id} | update a filter
[**put_content_view_filters_id_add_filter_rules**](ContentViewFiltersApi.md#put_content_view_filters_id_add_filter_rules) | **PUT** /content_view_filters/{id}/add_filter_rules | bulk add filter rules
[**put_content_view_filters_id_remove_filter_rules**](ContentViewFiltersApi.md#put_content_view_filters_id_remove_filter_rules) | **PUT** /content_view_filters/{id}/remove_filter_rules | bulk delete filter rules
[**put_content_views_content_view_id_filters_id**](ContentViewFiltersApi.md#put_content_views_content_view_id_filters_id) | **PUT** /content_views/{content_view_id}/filters/{id} | update a filter
[**put_content_views_content_view_id_filters_id_add_filter_rules**](ContentViewFiltersApi.md#put_content_views_content_view_id_filters_id_add_filter_rules) | **PUT** /content_views/{content_view_id}/filters/{id}/add_filter_rules | bulk add filter rules
[**put_content_views_content_view_id_filters_id_remove_filter_rules**](ContentViewFiltersApi.md#put_content_views_content_view_id_filters_id_remove_filter_rules) | **PUT** /content_views/{content_view_id}/filters/{id}/remove_filter_rules | bulk delete filter rules


# **delete_content_view_filters_id**
> delete_content_view_filters_id(id, content_view_id)

delete a filter

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    id = 3.4 # float | filter identifier
    content_view_id = 3.4 # float | content view identifier

    try:
        # delete a filter
        api_instance.delete_content_view_filters_id(id, content_view_id)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->delete_content_view_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| filter identifier | 
 **content_view_id** | **float**| content view identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_views_content_view_id_filters_id**
> delete_content_views_content_view_id_filters_id(content_view_id, id)

delete a filter

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    id = 3.4 # float | filter identifier

    try:
        # delete a filter
        api_instance.delete_content_views_content_view_id_filters_id(content_view_id, id)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->delete_content_views_content_view_id_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **id** | **float**| filter identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_view_filters**
> get_content_view_filters(content_view_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, types=types)

list filters

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    name = 'name_example' # str | filter content view filters by name (optional)
    types = ['types_example'] # List[str] | types of filters (optional)

    try:
        # list filters
        api_instance.get_content_view_filters(content_view_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, types=types)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->get_content_view_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **name** | **str**| filter content view filters by name | [optional] 
 **types** | [**List[str]**](str.md)| types of filters | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_view_filters_id**
> get_content_view_filters_id(id, content_view_id)

show filter info

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    id = 3.4 # float | filter identifier
    content_view_id = 3.4 # float | content view identifier

    try:
        # show filter info
        api_instance.get_content_view_filters_id(id, content_view_id)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->get_content_view_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| filter identifier | 
 **content_view_id** | **float**| content view identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_views_content_view_id_filters**
> get_content_views_content_view_id_filters(content_view_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, types=types)

list filters

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    name = 'name_example' # str | filter content view filters by name (optional)
    types = ['types_example'] # List[str] | types of filters (optional)

    try:
        # list filters
        api_instance.get_content_views_content_view_id_filters(content_view_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, types=types)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->get_content_views_content_view_id_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **name** | **str**| filter content view filters by name | [optional] 
 **types** | [**List[str]**](str.md)| types of filters | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_views_content_view_id_filters_id**
> get_content_views_content_view_id_filters_id(content_view_id, id)

show filter info

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    id = 3.4 # float | filter identifier

    try:
        # show filter info
        api_instance.get_content_views_content_view_id_filters_id(content_view_id, id)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->get_content_views_content_view_id_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **id** | **float**| filter identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_view_filters**
> post_content_view_filters(content_view_id, name, type, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)

create a filter for a content view

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    name = 'name_example' # str | name of the filter
    type = 'type_example' # str | type of filter (e.g. deb, rpm, package_group, erratum, erratum_id, erratum_date, docker, modulemd)
    original_packages = True # bool | add all packages without errata to the included/excluded list. (package filter only) (optional)
    original_module_streams = True # bool | add all module streams without errata to the included/excluded list. (module stream filter only) (optional)
    inclusion = True # bool | specifies if content should be included or excluded, default: inclusion=false (optional)
    repository_ids = ['repository_ids_example'] # List[str] | list of repository ids (optional)
    description = 'description_example' # str | description of the filter (optional)

    try:
        # create a filter for a content view
        api_instance.post_content_view_filters(content_view_id, name, type, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->post_content_view_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **name** | **str**| name of the filter | 
 **type** | **str**| type of filter (e.g. deb, rpm, package_group, erratum, erratum_id, erratum_date, docker, modulemd) | 
 **original_packages** | **bool**| add all packages without errata to the included/excluded list. (package filter only) | [optional] 
 **original_module_streams** | **bool**| add all module streams without errata to the included/excluded list. (module stream filter only) | [optional] 
 **inclusion** | **bool**| specifies if content should be included or excluded, default: inclusion&#x3D;false | [optional] 
 **repository_ids** | [**List[str]**](str.md)| list of repository ids | [optional] 
 **description** | **str**| description of the filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_views_content_view_id_filters**
> post_content_views_content_view_id_filters(content_view_id, name, type, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)

create a filter for a content view

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    name = 'name_example' # str | name of the filter
    type = 'type_example' # str | type of filter (e.g. deb, rpm, package_group, erratum, erratum_id, erratum_date, docker, modulemd)
    original_packages = True # bool | add all packages without errata to the included/excluded list. (package filter only) (optional)
    original_module_streams = True # bool | add all module streams without errata to the included/excluded list. (module stream filter only) (optional)
    inclusion = True # bool | specifies if content should be included or excluded, default: inclusion=false (optional)
    repository_ids = ['repository_ids_example'] # List[str] | list of repository ids (optional)
    description = 'description_example' # str | description of the filter (optional)

    try:
        # create a filter for a content view
        api_instance.post_content_views_content_view_id_filters(content_view_id, name, type, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->post_content_views_content_view_id_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **name** | **str**| name of the filter | 
 **type** | **str**| type of filter (e.g. deb, rpm, package_group, erratum, erratum_id, erratum_date, docker, modulemd) | 
 **original_packages** | **bool**| add all packages without errata to the included/excluded list. (package filter only) | [optional] 
 **original_module_streams** | **bool**| add all module streams without errata to the included/excluded list. (module stream filter only) | [optional] 
 **inclusion** | **bool**| specifies if content should be included or excluded, default: inclusion&#x3D;false | [optional] 
 **repository_ids** | [**List[str]**](str.md)| list of repository ids | [optional] 
 **description** | **str**| description of the filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_view_filters_id**
> put_content_view_filters_id(id, content_view_id, name=name, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)

update a filter

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    id = 3.4 # float | filter identifier
    content_view_id = 3.4 # float | content view identifier
    name = 'name_example' # str | new name for the filter (optional)
    original_packages = True # bool | add all packages without errata to the included/excluded list. (package filter only) (optional)
    original_module_streams = True # bool | add all module streams without errata to the included/excluded list. (module stream filter only) (optional)
    inclusion = True # bool | specifies if content should be included or excluded, default: inclusion=false (optional)
    repository_ids = ['repository_ids_example'] # List[str] | list of repository ids (optional)
    description = 'description_example' # str | description of the filter (optional)

    try:
        # update a filter
        api_instance.put_content_view_filters_id(id, content_view_id, name=name, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_view_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| filter identifier | 
 **content_view_id** | **float**| content view identifier | 
 **name** | **str**| new name for the filter | [optional] 
 **original_packages** | **bool**| add all packages without errata to the included/excluded list. (package filter only) | [optional] 
 **original_module_streams** | **bool**| add all module streams without errata to the included/excluded list. (module stream filter only) | [optional] 
 **inclusion** | **bool**| specifies if content should be included or excluded, default: inclusion&#x3D;false | [optional] 
 **repository_ids** | [**List[str]**](str.md)| list of repository ids | [optional] 
 **description** | **str**| description of the filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_view_filters_id_add_filter_rules**
> put_content_view_filters_id_add_filter_rules(id, content_view_id, rules_params=rules_params)

bulk add filter rules

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    id = 3.4 # float | filter identifier
    content_view_id = 3.4 # float | content view identifier
    rules_params = ['rules_params_example'] # List[str] | Rules to be added (optional)

    try:
        # bulk add filter rules
        api_instance.put_content_view_filters_id_add_filter_rules(id, content_view_id, rules_params=rules_params)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_view_filters_id_add_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| filter identifier | 
 **content_view_id** | **float**| content view identifier | 
 **rules_params** | [**List[str]**](str.md)| Rules to be added | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_view_filters_id_remove_filter_rules**
> put_content_view_filters_id_remove_filter_rules(id, content_view_id, rule_ids)

bulk delete filter rules

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    id = 3.4 # float | filter identifier
    content_view_id = 3.4 # float | content view identifier
    rule_ids = ['rule_ids_example'] # List[str] | filter identifiers

    try:
        # bulk delete filter rules
        api_instance.put_content_view_filters_id_remove_filter_rules(id, content_view_id, rule_ids)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_view_filters_id_remove_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| filter identifier | 
 **content_view_id** | **float**| content view identifier | 
 **rule_ids** | [**List[str]**](str.md)| filter identifiers | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_content_view_id_filters_id**
> put_content_views_content_view_id_filters_id(content_view_id, id, name=name, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)

update a filter

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    id = 3.4 # float | filter identifier
    name = 'name_example' # str | new name for the filter (optional)
    original_packages = True # bool | add all packages without errata to the included/excluded list. (package filter only) (optional)
    original_module_streams = True # bool | add all module streams without errata to the included/excluded list. (module stream filter only) (optional)
    inclusion = True # bool | specifies if content should be included or excluded, default: inclusion=false (optional)
    repository_ids = ['repository_ids_example'] # List[str] | list of repository ids (optional)
    description = 'description_example' # str | description of the filter (optional)

    try:
        # update a filter
        api_instance.put_content_views_content_view_id_filters_id(content_view_id, id, name=name, original_packages=original_packages, original_module_streams=original_module_streams, inclusion=inclusion, repository_ids=repository_ids, description=description)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_views_content_view_id_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **id** | **float**| filter identifier | 
 **name** | **str**| new name for the filter | [optional] 
 **original_packages** | **bool**| add all packages without errata to the included/excluded list. (package filter only) | [optional] 
 **original_module_streams** | **bool**| add all module streams without errata to the included/excluded list. (module stream filter only) | [optional] 
 **inclusion** | **bool**| specifies if content should be included or excluded, default: inclusion&#x3D;false | [optional] 
 **repository_ids** | [**List[str]**](str.md)| list of repository ids | [optional] 
 **description** | **str**| description of the filter | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_content_view_id_filters_id_add_filter_rules**
> put_content_views_content_view_id_filters_id_add_filter_rules(content_view_id, id, rules_params=rules_params)

bulk add filter rules

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    id = 3.4 # float | filter identifier
    rules_params = ['rules_params_example'] # List[str] | Rules to be added (optional)

    try:
        # bulk add filter rules
        api_instance.put_content_views_content_view_id_filters_id_add_filter_rules(content_view_id, id, rules_params=rules_params)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_views_content_view_id_filters_id_add_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **id** | **float**| filter identifier | 
 **rules_params** | [**List[str]**](str.md)| Rules to be added | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_content_view_id_filters_id_remove_filter_rules**
> put_content_views_content_view_id_filters_id_remove_filter_rules(content_view_id, id, rule_ids)

bulk delete filter rules

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentViewFiltersApi(api_client)
    content_view_id = 3.4 # float | content view identifier
    id = 3.4 # float | filter identifier
    rule_ids = ['rule_ids_example'] # List[str] | filter identifiers

    try:
        # bulk delete filter rules
        api_instance.put_content_views_content_view_id_filters_id_remove_filter_rules(content_view_id, id, rule_ids)
    except Exception as e:
        print("Exception when calling ContentViewFiltersApi->put_content_views_content_view_id_filters_id_remove_filter_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| content view identifier | 
 **id** | **float**| filter identifier | 
 **rule_ids** | [**List[str]**](str.md)| filter identifiers | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

