# foreman.ContentViewFilterRulesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content_view_filters_content_view_filter_id_rules_id**](ContentViewFilterRulesApi.md#delete_content_view_filters_content_view_filter_id_rules_id) | **DELETE** /content_view_filters/{content_view_filter_id}/rules/{id} | Delete a filter rule
[**get_content_view_filters_content_view_filter_id_rules**](ContentViewFilterRulesApi.md#get_content_view_filters_content_view_filter_id_rules) | **GET** /content_view_filters/{content_view_filter_id}/rules | List filter rules
[**get_content_view_filters_content_view_filter_id_rules_id**](ContentViewFilterRulesApi.md#get_content_view_filters_content_view_filter_id_rules_id) | **GET** /content_view_filters/{content_view_filter_id}/rules/{id} | Show filter rule info
[**post_content_view_filters_content_view_filter_id_rules**](ContentViewFilterRulesApi.md#post_content_view_filters_content_view_filter_id_rules) | **POST** /content_view_filters/{content_view_filter_id}/rules | Create a filter rule. The parameters included should be based upon the filter type.
[**put_content_view_filters_content_view_filter_id_rules_id**](ContentViewFilterRulesApi.md#put_content_view_filters_content_view_filter_id_rules_id) | **PUT** /content_view_filters/{content_view_filter_id}/rules/{id} | Update a filter rule. The parameters included should be based upon the filter type.


# **delete_content_view_filters_content_view_filter_id_rules_id**
> delete_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id)

Delete a filter rule

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
    api_instance = foreman.ContentViewFilterRulesApi(api_client)
    content_view_filter_id = 3.4 # float | filter identifier
    id = 3.4 # float | rule identifier

    try:
        # Delete a filter rule
        api_instance.delete_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id)
    except Exception as e:
        print("Exception when calling ContentViewFilterRulesApi->delete_content_view_filters_content_view_filter_id_rules_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| filter identifier | 
 **id** | **float**| rule identifier | 

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

# **get_content_view_filters_content_view_filter_id_rules**
> get_content_view_filters_content_view_filter_id_rules(content_view_filter_id, name=name, errata_id=errata_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List filter rules

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
    api_instance = foreman.ContentViewFilterRulesApi(api_client)
    content_view_filter_id = 3.4 # float | filter identifier
    name = 'name_example' # str | name of the content view filter rule (optional)
    errata_id = 'errata_id_example' # str | errata_id of the content view filter rule (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List filter rules
        api_instance.get_content_view_filters_content_view_filter_id_rules(content_view_filter_id, name=name, errata_id=errata_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ContentViewFilterRulesApi->get_content_view_filters_content_view_filter_id_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| filter identifier | 
 **name** | **str**| name of the content view filter rule | [optional] 
 **errata_id** | **str**| errata_id of the content view filter rule | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_view_filters_content_view_filter_id_rules_id**
> get_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id)

Show filter rule info

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
    api_instance = foreman.ContentViewFilterRulesApi(api_client)
    content_view_filter_id = 3.4 # float | filter identifier
    id = 3.4 # float | rule identifier

    try:
        # Show filter rule info
        api_instance.get_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id)
    except Exception as e:
        print("Exception when calling ContentViewFilterRulesApi->get_content_view_filters_content_view_filter_id_rules_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| filter identifier | 
 **id** | **float**| rule identifier | 

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

# **post_content_view_filters_content_view_filter_id_rules**
> post_content_view_filters_content_view_filter_id_rules(content_view_filter_id, name=name, uuid=uuid, version=version, architecture=architecture, min_version=min_version, max_version=max_version, errata_id=errata_id, errata_ids=errata_ids, start_date=start_date, end_date=end_date, types=types, date_type=date_type, module_stream_ids=module_stream_ids)

Create a filter rule. The parameters included should be based upon the filter type.

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
    api_instance = foreman.ContentViewFilterRulesApi(api_client)
    content_view_filter_id = 3.4 # float | filter identifier
    name = ['name_example'] # List[str] | deb, package, package group, or docker tag names (optional)
    uuid = 'uuid_example' # str | package group: uuid (optional)
    version = 'version_example' # str | package: version (optional)
    architecture = 'architecture_example' # str | package: architecture (optional)
    min_version = 'min_version_example' # str | package: minimum version (optional)
    max_version = 'max_version_example' # str | package: maximum version (optional)
    errata_id = 'errata_id_example' # str | erratum: id (optional)
    errata_ids = ['errata_ids_example'] # List[str] | erratum: IDs or a select all object (optional)
    start_date = 'start_date_example' # str | erratum: start date (YYYY-MM-DD) (optional)
    end_date = 'end_date_example' # str | erratum: end date (YYYY-MM-DD) (optional)
    types = ['types_example'] # List[str] | erratum: types (enhancement, bugfix, security) (optional)
    date_type = 'date_type_example' # str | erratum: search using the 'Issued On' or 'Updated On' column of the errata. Values are 'issued'/'updated' (optional)
    module_stream_ids = ['module_stream_ids_example'] # List[str] | module stream ids (optional)

    try:
        # Create a filter rule. The parameters included should be based upon the filter type.
        api_instance.post_content_view_filters_content_view_filter_id_rules(content_view_filter_id, name=name, uuid=uuid, version=version, architecture=architecture, min_version=min_version, max_version=max_version, errata_id=errata_id, errata_ids=errata_ids, start_date=start_date, end_date=end_date, types=types, date_type=date_type, module_stream_ids=module_stream_ids)
    except Exception as e:
        print("Exception when calling ContentViewFilterRulesApi->post_content_view_filters_content_view_filter_id_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| filter identifier | 
 **name** | [**List[str]**](str.md)| deb, package, package group, or docker tag names | [optional] 
 **uuid** | **str**| package group: uuid | [optional] 
 **version** | **str**| package: version | [optional] 
 **architecture** | **str**| package: architecture | [optional] 
 **min_version** | **str**| package: minimum version | [optional] 
 **max_version** | **str**| package: maximum version | [optional] 
 **errata_id** | **str**| erratum: id | [optional] 
 **errata_ids** | [**List[str]**](str.md)| erratum: IDs or a select all object | [optional] 
 **start_date** | **str**| erratum: start date (YYYY-MM-DD) | [optional] 
 **end_date** | **str**| erratum: end date (YYYY-MM-DD) | [optional] 
 **types** | [**List[str]**](str.md)| erratum: types (enhancement, bugfix, security) | [optional] 
 **date_type** | **str**| erratum: search using the &#39;Issued On&#39; or &#39;Updated On&#39; column of the errata. Values are &#39;issued&#39;/&#39;updated&#39; | [optional] 
 **module_stream_ids** | [**List[str]**](str.md)| module stream ids | [optional] 

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

# **put_content_view_filters_content_view_filter_id_rules_id**
> put_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id, name=name, version=version, architecture=architecture, min_version=min_version, max_version=max_version, errata_id=errata_id, start_date=start_date, end_date=end_date, types=types)

Update a filter rule. The parameters included should be based upon the filter type.

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
    api_instance = foreman.ContentViewFilterRulesApi(api_client)
    content_view_filter_id = 3.4 # float | filter identifier
    id = 3.4 # float | rule identifier
    name = 'name_example' # str | package, package group, or docker tag: name (optional)
    version = 'version_example' # str | package: version (optional)
    architecture = 'architecture_example' # str | package: architecture (optional)
    min_version = 'min_version_example' # str | package: minimum version (optional)
    max_version = 'max_version_example' # str | package: maximum version (optional)
    errata_id = 'errata_id_example' # str | erratum: id (optional)
    start_date = 'start_date_example' # str | erratum: start date (YYYY-MM-DD) (optional)
    end_date = 'end_date_example' # str | erratum: end date (YYYY-MM-DD) (optional)
    types = ['types_example'] # List[str] | erratum: types (enhancement, bugfix, security) (optional)

    try:
        # Update a filter rule. The parameters included should be based upon the filter type.
        api_instance.put_content_view_filters_content_view_filter_id_rules_id(content_view_filter_id, id, name=name, version=version, architecture=architecture, min_version=min_version, max_version=max_version, errata_id=errata_id, start_date=start_date, end_date=end_date, types=types)
    except Exception as e:
        print("Exception when calling ContentViewFilterRulesApi->put_content_view_filters_content_view_filter_id_rules_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| filter identifier | 
 **id** | **float**| rule identifier | 
 **name** | **str**| package, package group, or docker tag: name | [optional] 
 **version** | **str**| package: version | [optional] 
 **architecture** | **str**| package: architecture | [optional] 
 **min_version** | **str**| package: minimum version | [optional] 
 **max_version** | **str**| package: maximum version | [optional] 
 **errata_id** | **str**| erratum: id | [optional] 
 **start_date** | **str**| erratum: start date (YYYY-MM-DD) | [optional] 
 **end_date** | **str**| erratum: end date (YYYY-MM-DD) | [optional] 
 **types** | [**List[str]**](str.md)| erratum: types (enhancement, bugfix, security) | [optional] 

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

