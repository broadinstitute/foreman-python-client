# foreman.RepositorySetsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_products_product_id_repository_sets**](RepositorySetsApi.md#get_products_product_id_repository_sets) | **GET** /products/{product_id}/repository_sets | List repository sets for a product.
[**get_products_product_id_repository_sets_id**](RepositorySetsApi.md#get_products_product_id_repository_sets_id) | **GET** /products/{product_id}/repository_sets/{id} | Get info about a repository set
[**get_products_product_id_repository_sets_id_available_repositories**](RepositorySetsApi.md#get_products_product_id_repository_sets_id_available_repositories) | **GET** /products/{product_id}/repository_sets/{id}/available_repositories | Get list of available repositories for the repository set
[**get_repository_sets**](RepositorySetsApi.md#get_repository_sets) | **GET** /repository_sets | List repository sets.
[**get_repository_sets_id**](RepositorySetsApi.md#get_repository_sets_id) | **GET** /repository_sets/{id} | Get info about a repository set
[**get_repository_sets_id_available_repositories**](RepositorySetsApi.md#get_repository_sets_id_available_repositories) | **GET** /repository_sets/{id}/available_repositories | Get list of available repositories for the repository set
[**put_products_product_id_repository_sets_id_disable**](RepositorySetsApi.md#put_products_product_id_repository_sets_id_disable) | **PUT** /products/{product_id}/repository_sets/{id}/disable | Disable a repository from the set
[**put_products_product_id_repository_sets_id_enable**](RepositorySetsApi.md#put_products_product_id_repository_sets_id_enable) | **PUT** /products/{product_id}/repository_sets/{id}/enable | Enable a repository from the set
[**put_repository_sets_id_disable**](RepositorySetsApi.md#put_repository_sets_id_disable) | **PUT** /repository_sets/{id}/disable | Disable a repository from the set
[**put_repository_sets_id_enable**](RepositorySetsApi.md#put_repository_sets_id_enable) | **PUT** /repository_sets/{id}/enable | Enable a repository from the set


# **get_products_product_id_repository_sets**
> get_products_product_id_repository_sets(product_id, name=name, enabled=enabled, with_active_subscription=with_active_subscription, organization_id=organization_id, with_custom=with_custom, activation_key_id=activation_key_id, host_id=host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, status=status, repository_type=repository_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List repository sets for a product.

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
    api_instance = foreman.RepositorySetsApi(api_client)
    product_id = 3.4 # float | ID of a product to list repository sets from
    name = 'name_example' # str | Repository set name to search on (optional)
    enabled = True # bool | If true, only return repository sets that have been enabled. Defaults to false (optional)
    with_active_subscription = True # bool | If true, only return repository sets that are associated with an active subscriptions (optional)
    organization_id = 3.4 # float | organization identifier (optional)
    with_custom = True # bool | If true, return custom repository sets along with redhat repos. Will be ignored if repository_type is supplied. (optional)
    activation_key_id = 3.4 # float | activation key identifier (optional)
    host_id = 3.4 # float | Id of the host (optional)
    content_access_mode_all = True # bool | Get all content available, not just that provided by subscriptions. (optional)
    content_access_mode_env = True # bool | Limit content to just that available in the host's or activation key's content view version and lifecycle environment. (optional)
    status = 'status_example' # str | Limit content to enabled / disabled / overridden (optional)
    repository_type = 'repository_type_example' # str | Limit content to Red Hat / custom (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List repository sets for a product.
        api_instance.get_products_product_id_repository_sets(product_id, name=name, enabled=enabled, with_active_subscription=with_active_subscription, organization_id=organization_id, with_custom=with_custom, activation_key_id=activation_key_id, host_id=host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, status=status, repository_type=repository_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_products_product_id_repository_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| ID of a product to list repository sets from | 
 **name** | **str**| Repository set name to search on | [optional] 
 **enabled** | **bool**| If true, only return repository sets that have been enabled. Defaults to false | [optional] 
 **with_active_subscription** | **bool**| If true, only return repository sets that are associated with an active subscriptions | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 
 **with_custom** | **bool**| If true, return custom repository sets along with redhat repos. Will be ignored if repository_type is supplied. | [optional] 
 **activation_key_id** | **float**| activation key identifier | [optional] 
 **host_id** | **float**| Id of the host | [optional] 
 **content_access_mode_all** | **bool**| Get all content available, not just that provided by subscriptions. | [optional] 
 **content_access_mode_env** | **bool**| Limit content to just that available in the host&#39;s or activation key&#39;s content view version and lifecycle environment. | [optional] 
 **status** | **str**| Limit content to enabled / disabled / overridden | [optional] 
 **repository_type** | **str**| Limit content to Red Hat / custom | [optional] 
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

# **get_products_product_id_repository_sets_id**
> get_products_product_id_repository_sets_id(id, product_id, organization_id=organization_id)

Get info about a repository set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set
    product_id = 3.4 # float | ID of a product to list repository sets from
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Get info about a repository set
        api_instance.get_products_product_id_repository_sets_id(id, product_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_products_product_id_repository_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set | 
 **product_id** | **float**| ID of a product to list repository sets from | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **get_products_product_id_repository_sets_id_available_repositories**
> get_products_product_id_repository_sets_id_available_repositories(id, product_id, organization_id=organization_id)

Get list of available repositories for the repository set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set
    product_id = 3.4 # float | ID of a product to list repository sets from
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Get list of available repositories for the repository set
        api_instance.get_products_product_id_repository_sets_id_available_repositories(id, product_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_products_product_id_repository_sets_id_available_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set | 
 **product_id** | **float**| ID of a product to list repository sets from | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **get_repository_sets**
> get_repository_sets(product_id, name=name, enabled=enabled, with_active_subscription=with_active_subscription, organization_id=organization_id, with_custom=with_custom, activation_key_id=activation_key_id, host_id=host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, status=status, repository_type=repository_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List repository sets.

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
    api_instance = foreman.RepositorySetsApi(api_client)
    product_id = 3.4 # float | ID of a product to list repository sets from
    name = 'name_example' # str | Repository set name to search on (optional)
    enabled = True # bool | If true, only return repository sets that have been enabled. Defaults to false (optional)
    with_active_subscription = True # bool | If true, only return repository sets that are associated with an active subscriptions (optional)
    organization_id = 3.4 # float | organization identifier (optional)
    with_custom = True # bool | If true, return custom repository sets along with redhat repos. Will be ignored if repository_type is supplied. (optional)
    activation_key_id = 3.4 # float | activation key identifier (optional)
    host_id = 3.4 # float | Id of the host (optional)
    content_access_mode_all = True # bool | Get all content available, not just that provided by subscriptions. (optional)
    content_access_mode_env = True # bool | Limit content to just that available in the host's or activation key's content view version and lifecycle environment. (optional)
    status = 'status_example' # str | Limit content to enabled / disabled / overridden (optional)
    repository_type = 'repository_type_example' # str | Limit content to Red Hat / custom (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List repository sets.
        api_instance.get_repository_sets(product_id, name=name, enabled=enabled, with_active_subscription=with_active_subscription, organization_id=organization_id, with_custom=with_custom, activation_key_id=activation_key_id, host_id=host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, status=status, repository_type=repository_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_repository_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| ID of a product to list repository sets from | 
 **name** | **str**| Repository set name to search on | [optional] 
 **enabled** | **bool**| If true, only return repository sets that have been enabled. Defaults to false | [optional] 
 **with_active_subscription** | **bool**| If true, only return repository sets that are associated with an active subscriptions | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 
 **with_custom** | **bool**| If true, return custom repository sets along with redhat repos. Will be ignored if repository_type is supplied. | [optional] 
 **activation_key_id** | **float**| activation key identifier | [optional] 
 **host_id** | **float**| Id of the host | [optional] 
 **content_access_mode_all** | **bool**| Get all content available, not just that provided by subscriptions. | [optional] 
 **content_access_mode_env** | **bool**| Limit content to just that available in the host&#39;s or activation key&#39;s content view version and lifecycle environment. | [optional] 
 **status** | **str**| Limit content to enabled / disabled / overridden | [optional] 
 **repository_type** | **str**| Limit content to Red Hat / custom | [optional] 
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

# **get_repository_sets_id**
> get_repository_sets_id(id, product_id, organization_id=organization_id)

Get info about a repository set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set
    product_id = 3.4 # float | ID of a product to list repository sets from
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Get info about a repository set
        api_instance.get_repository_sets_id(id, product_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_repository_sets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set | 
 **product_id** | **float**| ID of a product to list repository sets from | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **get_repository_sets_id_available_repositories**
> get_repository_sets_id_available_repositories(id, product_id, organization_id=organization_id)

Get list of available repositories for the repository set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set
    product_id = 3.4 # float | ID of a product to list repository sets from
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Get list of available repositories for the repository set
        api_instance.get_repository_sets_id_available_repositories(id, product_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->get_repository_sets_id_available_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set | 
 **product_id** | **float**| ID of a product to list repository sets from | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **put_products_product_id_repository_sets_id_disable**
> put_products_product_id_repository_sets_id_disable(id, product_id, repository_id=repository_id, basearch=basearch, releasever=releasever, organization_id=organization_id)

Disable a repository from the set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set to disable
    product_id = 3.4 # float | ID of the product containing the repository set
    repository_id = 3.4 # float | ID of the repository within the set to disable (optional)
    basearch = 'basearch_example' # str | Basearch to disable (optional)
    releasever = 'releasever_example' # str | Releasever to disable (optional)
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Disable a repository from the set
        api_instance.put_products_product_id_repository_sets_id_disable(id, product_id, repository_id=repository_id, basearch=basearch, releasever=releasever, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->put_products_product_id_repository_sets_id_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set to disable | 
 **product_id** | **float**| ID of the product containing the repository set | 
 **repository_id** | **float**| ID of the repository within the set to disable | [optional] 
 **basearch** | **str**| Basearch to disable | [optional] 
 **releasever** | **str**| Releasever to disable | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **put_products_product_id_repository_sets_id_enable**
> put_products_product_id_repository_sets_id_enable(id, product_id, basearch=basearch, releasever=releasever, organization_id=organization_id)

Enable a repository from the set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set to enable
    product_id = 3.4 # float | ID of the product containing the repository set
    basearch = 'basearch_example' # str | Basearch to enable (optional)
    releasever = 'releasever_example' # str | Releasever to enable (optional)
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Enable a repository from the set
        api_instance.put_products_product_id_repository_sets_id_enable(id, product_id, basearch=basearch, releasever=releasever, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->put_products_product_id_repository_sets_id_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set to enable | 
 **product_id** | **float**| ID of the product containing the repository set | 
 **basearch** | **str**| Basearch to enable | [optional] 
 **releasever** | **str**| Releasever to enable | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **put_repository_sets_id_disable**
> put_repository_sets_id_disable(id, product_id, repository_id=repository_id, basearch=basearch, releasever=releasever, organization_id=organization_id)

Disable a repository from the set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set to disable
    product_id = 3.4 # float | ID of the product containing the repository set
    repository_id = 3.4 # float | ID of the repository within the set to disable (optional)
    basearch = 'basearch_example' # str | Basearch to disable (optional)
    releasever = 'releasever_example' # str | Releasever to disable (optional)
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Disable a repository from the set
        api_instance.put_repository_sets_id_disable(id, product_id, repository_id=repository_id, basearch=basearch, releasever=releasever, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->put_repository_sets_id_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set to disable | 
 **product_id** | **float**| ID of the product containing the repository set | 
 **repository_id** | **float**| ID of the repository within the set to disable | [optional] 
 **basearch** | **str**| Basearch to disable | [optional] 
 **releasever** | **str**| Releasever to disable | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **put_repository_sets_id_enable**
> put_repository_sets_id_enable(id, product_id, basearch=basearch, releasever=releasever, organization_id=organization_id)

Enable a repository from the set

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
    api_instance = foreman.RepositorySetsApi(api_client)
    id = 3.4 # float | ID of the repository set to enable
    product_id = 3.4 # float | ID of the product containing the repository set
    basearch = 'basearch_example' # str | Basearch to enable (optional)
    releasever = 'releasever_example' # str | Releasever to enable (optional)
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Enable a repository from the set
        api_instance.put_repository_sets_id_enable(id, product_id, basearch=basearch, releasever=releasever, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RepositorySetsApi->put_repository_sets_id_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the repository set to enable | 
 **product_id** | **float**| ID of the product containing the repository set | 
 **basearch** | **str**| Basearch to enable | [optional] 
 **releasever** | **str**| Releasever to enable | [optional] 
 **organization_id** | **float**| organization identifier | [optional] 

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

