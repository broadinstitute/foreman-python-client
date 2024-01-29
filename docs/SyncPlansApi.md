# foreman.SyncPlansApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organizations_organization_id_sync_plans_id**](SyncPlansApi.md#delete_organizations_organization_id_sync_plans_id) | **DELETE** /organizations/{organization_id}/sync_plans/{id} | Destroy a sync plan
[**delete_sync_plans_id**](SyncPlansApi.md#delete_sync_plans_id) | **DELETE** /sync_plans/{id} | Destroy a sync plan
[**get_organizations_organization_id_sync_plans**](SyncPlansApi.md#get_organizations_organization_id_sync_plans) | **GET** /organizations/{organization_id}/sync_plans | 
[**get_organizations_organization_id_sync_plans_id**](SyncPlansApi.md#get_organizations_organization_id_sync_plans_id) | **GET** /organizations/{organization_id}/sync_plans/{id} | Show a sync plan
[**get_sync_plans**](SyncPlansApi.md#get_sync_plans) | **GET** /sync_plans | List sync plans
[**get_sync_plans_id**](SyncPlansApi.md#get_sync_plans_id) | **GET** /sync_plans/{id} | Show a sync plan
[**post_organizations_organization_id_sync_plans**](SyncPlansApi.md#post_organizations_organization_id_sync_plans) | **POST** /organizations/{organization_id}/sync_plans | Create a sync plan
[**put_organizations_organization_id_sync_plans_id**](SyncPlansApi.md#put_organizations_organization_id_sync_plans_id) | **PUT** /organizations/{organization_id}/sync_plans/{id} | Update a sync plan
[**put_organizations_organization_id_sync_plans_id_add_products**](SyncPlansApi.md#put_organizations_organization_id_sync_plans_id_add_products) | **PUT** /organizations/{organization_id}/sync_plans/{id}/add_products | Add products to sync plan
[**put_organizations_organization_id_sync_plans_id_remove_products**](SyncPlansApi.md#put_organizations_organization_id_sync_plans_id_remove_products) | **PUT** /organizations/{organization_id}/sync_plans/{id}/remove_products | Remove products from sync plan
[**put_organizations_organization_id_sync_plans_id_sync**](SyncPlansApi.md#put_organizations_organization_id_sync_plans_id_sync) | **PUT** /organizations/{organization_id}/sync_plans/{id}/sync | Initiate a sync of the products attached to the sync plan
[**put_sync_plans_id**](SyncPlansApi.md#put_sync_plans_id) | **PUT** /sync_plans/{id} | Update a sync plan
[**put_sync_plans_id_sync**](SyncPlansApi.md#put_sync_plans_id_sync) | **PUT** /sync_plans/{id}/sync | Initiate a sync of the products attached to the sync plan


# **delete_organizations_organization_id_sync_plans_id**
> delete_organizations_organization_id_sync_plans_id(organization_id, id)

Destroy a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    id = 3.4 # float | sync plan numeric identifier

    try:
        # Destroy a sync plan
        api_instance.delete_organizations_organization_id_sync_plans_id(organization_id, id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->delete_organizations_organization_id_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **id** | **float**| sync plan numeric identifier | 

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

# **delete_sync_plans_id**
> delete_sync_plans_id(id, organization_id)

Destroy a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    id = 3.4 # float | sync plan numeric identifier
    organization_id = 3.4 # float | Organization ID

    try:
        # Destroy a sync plan
        api_instance.delete_sync_plans_id(id, organization_id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->delete_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| sync plan numeric identifier | 
 **organization_id** | **float**| Organization ID | 

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

# **get_organizations_organization_id_sync_plans**
> get_organizations_organization_id_sync_plans(organization_id, name=name, sync_date=sync_date, interval=interval, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)



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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    name = 'name_example' # str | filter by name (optional)
    sync_date = 'sync_date_example' # str | filter by sync date (optional)
    interval = 'interval_example' # str | filter by interval (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        api_instance.get_organizations_organization_id_sync_plans(organization_id, name=name, sync_date=sync_date, interval=interval, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling SyncPlansApi->get_organizations_organization_id_sync_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **name** | **str**| filter by name | [optional] 
 **sync_date** | **str**| filter by sync date | [optional] 
 **interval** | **str**| filter by interval | [optional] 
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

# **get_organizations_organization_id_sync_plans_id**
> get_organizations_organization_id_sync_plans_id(organization_id, id)

Show a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    id = 3.4 # float | sync plan numeric identifier

    try:
        # Show a sync plan
        api_instance.get_organizations_organization_id_sync_plans_id(organization_id, id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->get_organizations_organization_id_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **id** | **float**| sync plan numeric identifier | 

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

# **get_sync_plans**
> get_sync_plans(organization_id, name=name, sync_date=sync_date, interval=interval, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List sync plans

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    name = 'name_example' # str | filter by name (optional)
    sync_date = 'sync_date_example' # str | filter by sync date (optional)
    interval = 'interval_example' # str | filter by interval (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List sync plans
        api_instance.get_sync_plans(organization_id, name=name, sync_date=sync_date, interval=interval, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling SyncPlansApi->get_sync_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **name** | **str**| filter by name | [optional] 
 **sync_date** | **str**| filter by sync date | [optional] 
 **interval** | **str**| filter by interval | [optional] 
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

# **get_sync_plans_id**
> get_sync_plans_id(id, organization_id)

Show a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    id = 3.4 # float | sync plan numeric identifier
    organization_id = 3.4 # float | Organization ID

    try:
        # Show a sync plan
        api_instance.get_sync_plans_id(id, organization_id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->get_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| sync plan numeric identifier | 
 **organization_id** | **float**| Organization ID | 

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

# **post_organizations_organization_id_sync_plans**
> post_organizations_organization_id_sync_plans(organization_id, name, interval, sync_date, enabled, description=description, cron_expression=cron_expression)

Create a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    name = 'name_example' # str | sync plan name
    interval = 'interval_example' # str | how often synchronization should run
    sync_date = 'sync_date_example' # str | start datetime of synchronization
    enabled = True # bool | enables or disables synchronization
    description = 'description_example' # str | sync plan description (optional)
    cron_expression = 'cron_expression_example' # str | Add custom cron logic for sync plan (optional)

    try:
        # Create a sync plan
        api_instance.post_organizations_organization_id_sync_plans(organization_id, name, interval, sync_date, enabled, description=description, cron_expression=cron_expression)
    except Exception as e:
        print("Exception when calling SyncPlansApi->post_organizations_organization_id_sync_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **name** | **str**| sync plan name | 
 **interval** | **str**| how often synchronization should run | 
 **sync_date** | **str**| start datetime of synchronization | 
 **enabled** | **bool**| enables or disables synchronization | 
 **description** | **str**| sync plan description | [optional] 
 **cron_expression** | **str**| Add custom cron logic for sync plan | [optional] 

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

# **put_organizations_organization_id_sync_plans_id**
> put_organizations_organization_id_sync_plans_id(organization_id, id, name=name, interval=interval, sync_date=sync_date, description=description, enabled=enabled, cron_expression=cron_expression)

Update a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    id = 3.4 # float | sync plan numeric identifier
    name = 'name_example' # str | sync plan name (optional)
    interval = 'interval_example' # str | how often synchronization should run (optional)
    sync_date = 'sync_date_example' # str | start datetime of synchronization (optional)
    description = 'description_example' # str | sync plan description (optional)
    enabled = True # bool | enables or disables synchronization (optional)
    cron_expression = 'cron_expression_example' # str | Add custom cron logic for sync plan (optional)

    try:
        # Update a sync plan
        api_instance.put_organizations_organization_id_sync_plans_id(organization_id, id, name=name, interval=interval, sync_date=sync_date, description=description, enabled=enabled, cron_expression=cron_expression)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_organizations_organization_id_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **id** | **float**| sync plan numeric identifier | 
 **name** | **str**| sync plan name | [optional] 
 **interval** | **str**| how often synchronization should run | [optional] 
 **sync_date** | **str**| start datetime of synchronization | [optional] 
 **description** | **str**| sync plan description | [optional] 
 **enabled** | **bool**| enables or disables synchronization | [optional] 
 **cron_expression** | **str**| Add custom cron logic for sync plan | [optional] 

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

# **put_organizations_organization_id_sync_plans_id_add_products**
> put_organizations_organization_id_sync_plans_id_add_products(organization_id, id, product_ids)

Add products to sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    id = 'id_example' # str | ID of the sync plan
    product_ids = ['product_ids_example'] # List[str] | List of product ids to add to the sync plan

    try:
        # Add products to sync plan
        api_instance.put_organizations_organization_id_sync_plans_id_add_products(organization_id, id, product_ids)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_organizations_organization_id_sync_plans_id_add_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **id** | **str**| ID of the sync plan | 
 **product_ids** | [**List[str]**](str.md)| List of product ids to add to the sync plan | 

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

# **put_organizations_organization_id_sync_plans_id_remove_products**
> put_organizations_organization_id_sync_plans_id_remove_products(organization_id, id, product_ids)

Remove products from sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    organization_id = 3.4 # float | Organization ID
    id = 'id_example' # str | ID of the sync plan
    product_ids = ['product_ids_example'] # List[str] | List of product ids to remove from the sync plan

    try:
        # Remove products from sync plan
        api_instance.put_organizations_organization_id_sync_plans_id_remove_products(organization_id, id, product_ids)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_organizations_organization_id_sync_plans_id_remove_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID | 
 **id** | **str**| ID of the sync plan | 
 **product_ids** | [**List[str]**](str.md)| List of product ids to remove from the sync plan | 

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

# **put_organizations_organization_id_sync_plans_id_sync**
> put_organizations_organization_id_sync_plans_id_sync(id, organization_id)

Initiate a sync of the products attached to the sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    id = 'id_example' # str | ID of the sync plan
    organization_id = 3.4 # float | 

    try:
        # Initiate a sync of the products attached to the sync plan
        api_instance.put_organizations_organization_id_sync_plans_id_sync(id, organization_id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_organizations_organization_id_sync_plans_id_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the sync plan | 
 **organization_id** | **float**|  | 

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

# **put_sync_plans_id**
> put_sync_plans_id(id, organization_id, name=name, interval=interval, sync_date=sync_date, description=description, enabled=enabled, cron_expression=cron_expression)

Update a sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    id = 3.4 # float | sync plan numeric identifier
    organization_id = 3.4 # float | Organization ID
    name = 'name_example' # str | sync plan name (optional)
    interval = 'interval_example' # str | how often synchronization should run (optional)
    sync_date = 'sync_date_example' # str | start datetime of synchronization (optional)
    description = 'description_example' # str | sync plan description (optional)
    enabled = True # bool | enables or disables synchronization (optional)
    cron_expression = 'cron_expression_example' # str | Add custom cron logic for sync plan (optional)

    try:
        # Update a sync plan
        api_instance.put_sync_plans_id(id, organization_id, name=name, interval=interval, sync_date=sync_date, description=description, enabled=enabled, cron_expression=cron_expression)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_sync_plans_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| sync plan numeric identifier | 
 **organization_id** | **float**| Organization ID | 
 **name** | **str**| sync plan name | [optional] 
 **interval** | **str**| how often synchronization should run | [optional] 
 **sync_date** | **str**| start datetime of synchronization | [optional] 
 **description** | **str**| sync plan description | [optional] 
 **enabled** | **bool**| enables or disables synchronization | [optional] 
 **cron_expression** | **str**| Add custom cron logic for sync plan | [optional] 

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

# **put_sync_plans_id_sync**
> put_sync_plans_id_sync(id)

Initiate a sync of the products attached to the sync plan

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
    api_instance = foreman.SyncPlansApi(api_client)
    id = 'id_example' # str | ID of the sync plan

    try:
        # Initiate a sync of the products attached to the sync plan
        api_instance.put_sync_plans_id_sync(id)
    except Exception as e:
        print("Exception when calling SyncPlansApi->put_sync_plans_id_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the sync plan | 

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

