# foreman.HostErrataApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosts_host_id_errata**](HostErrataApi.md#get_hosts_host_id_errata) | **GET** /hosts/{host_id}/errata | List errata available for the content host
[**get_hosts_host_id_errata_id**](HostErrataApi.md#get_hosts_host_id_errata_id) | **GET** /hosts/{host_id}/errata/{id} | Retrieve a single errata for a host
[**put_hosts_host_id_errata_applicability**](HostErrataApi.md#put_hosts_host_id_errata_applicability) | **PUT** /hosts/{host_id}/errata/applicability | Force regenerate applicability.


# **get_hosts_host_id_errata**
> get_hosts_host_id_errata(host_id, content_view_id=content_view_id, environment_id=environment_id, include_applicable=include_applicable, type=type, severity=severity, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List errata available for the content host

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
    api_instance = foreman.HostErrataApi(api_client)
    host_id = 3.4 # float | UUID of the content host
    content_view_id = 3.4 # float | Calculate Applicable Errata based on a particular Content View (optional)
    environment_id = 3.4 # float | Calculate Applicable Errata based on a particular Environment (optional)
    include_applicable = True # bool | Return errata that are applicable to this host. Defaults to false) (optional)
    type = 'type_example' # str | Return only errata of a particular type (security, bugfix, enhancement) (optional)
    severity = 'severity_example' # str | Return only errata of a particular severity (None, Low, Moderate, Important, Critical) (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List errata available for the content host
        api_instance.get_hosts_host_id_errata(host_id, content_view_id=content_view_id, environment_id=environment_id, include_applicable=include_applicable, type=type, severity=severity, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling HostErrataApi->get_hosts_host_id_errata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| UUID of the content host | 
 **content_view_id** | **float**| Calculate Applicable Errata based on a particular Content View | [optional] 
 **environment_id** | **float**| Calculate Applicable Errata based on a particular Environment | [optional] 
 **include_applicable** | **bool**| Return errata that are applicable to this host. Defaults to false) | [optional] 
 **type** | **str**| Return only errata of a particular type (security, bugfix, enhancement) | [optional] 
 **severity** | **str**| Return only errata of a particular severity (None, Low, Moderate, Important, Critical) | [optional] 
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

# **get_hosts_host_id_errata_id**
> get_hosts_host_id_errata_id(host_id, id)

Retrieve a single errata for a host

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
    api_instance = foreman.HostErrataApi(api_client)
    host_id = 3.4 # float | Host ID
    id = 'id_example' # str | Errata id of the erratum (RHSA-2012:108)

    try:
        # Retrieve a single errata for a host
        api_instance.get_hosts_host_id_errata_id(host_id, id)
    except Exception as e:
        print("Exception when calling HostErrataApi->get_hosts_host_id_errata_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Host ID | 
 **id** | **str**| Errata id of the erratum (RHSA-2012:108) | 

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

# **put_hosts_host_id_errata_applicability**
> put_hosts_host_id_errata_applicability(host_id)

Force regenerate applicability.

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
    api_instance = foreman.HostErrataApi(api_client)
    host_id = 3.4 # float | Host ID

    try:
        # Force regenerate applicability.
        api_instance.put_hosts_host_id_errata_applicability(host_id)
    except Exception as e:
        print("Exception when calling HostErrataApi->put_hosts_host_id_errata_applicability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Host ID | 

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

