# foreman.ProductsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_products_id**](ProductsApi.md#delete_products_id) | **DELETE** /products/{id} | Destroy a product
[**get_activation_keys_activation_key_id_products**](ProductsApi.md#get_activation_keys_activation_key_id_products) | **GET** /activation_keys/{activation_key_id}/products | List of subscription products in an activation key
[**get_organizations_organization_id_products**](ProductsApi.md#get_organizations_organization_id_products) | **GET** /organizations/{organization_id}/products | List of products in an organization
[**get_organizations_organization_id_sync_plans_sync_plan_id_products**](ProductsApi.md#get_organizations_organization_id_sync_plans_sync_plan_id_products) | **GET** /organizations/{organization_id}/sync_plans/{sync_plan_id}/products | List of Products for sync plan
[**get_products**](ProductsApi.md#get_products) | **GET** /products | List products
[**get_products_id**](ProductsApi.md#get_products_id) | **GET** /products/{id} | Show a product
[**get_subscriptions_subscription_id_products**](ProductsApi.md#get_subscriptions_subscription_id_products) | **GET** /subscriptions/{subscription_id}/products | List of subscription products in a subscription
[**get_sync_plans_sync_plan_id_products**](ProductsApi.md#get_sync_plans_sync_plan_id_products) | **GET** /sync_plans/{sync_plan_id}/products | List of Products for sync plan
[**post_products**](ProductsApi.md#post_products) | **POST** /products | Create a product
[**post_products_id_sync**](ProductsApi.md#post_products_id_sync) | **POST** /products/{id}/sync | Sync all repositories for a product
[**put_products_id**](ProductsApi.md#put_products_id) | **PUT** /products/{id} | Updates a product


# **delete_products_id**
> delete_products_id(id)

Destroy a product

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
    api_instance = foreman.ProductsApi(api_client)
    id = 3.4 # float | product numeric identifier

    try:
        # Destroy a product
        api_instance.delete_products_id(id)
    except Exception as e:
        print("Exception when calling ProductsApi->delete_products_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| product numeric identifier | 

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

# **get_activation_keys_activation_key_id_products**
> get_activation_keys_activation_key_id_products(activation_key_id, organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of subscription products in an activation key

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
    api_instance = foreman.ProductsApi(api_client)
    activation_key_id = 3.4 # float | 
    organization_id = 3.4 # float | Filter products by organization
    subscription_id = 3.4 # float | Filter products by subscription
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List of subscription products in an activation key
        api_instance.get_activation_keys_activation_key_id_products(activation_key_id, organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_activation_keys_activation_key_id_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_key_id** | **float**|  | 
 **organization_id** | **float**| Filter products by organization | 
 **subscription_id** | **float**| Filter products by subscription | 
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **get_organizations_organization_id_products**
> get_organizations_organization_id_products(organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of products in an organization

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
    api_instance = foreman.ProductsApi(api_client)
    organization_id = 3.4 # float | Filter products by organization
    subscription_id = 3.4 # float | Filter products by subscription
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List of products in an organization
        api_instance.get_organizations_organization_id_products(organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_organizations_organization_id_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Filter products by organization | 
 **subscription_id** | **float**| Filter products by subscription | 
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **get_organizations_organization_id_sync_plans_sync_plan_id_products**
> get_organizations_organization_id_sync_plans_sync_plan_id_products(organization_id, sync_plan_id, subscription_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of Products for sync plan

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
    api_instance = foreman.ProductsApi(api_client)
    organization_id = 3.4 # float | Filter products by organization
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    subscription_id = 3.4 # float | Filter products by subscription
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List of Products for sync plan
        api_instance.get_organizations_organization_id_sync_plans_sync_plan_id_products(organization_id, sync_plan_id, subscription_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_organizations_organization_id_sync_plans_sync_plan_id_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Filter products by organization | 
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **subscription_id** | **float**| Filter products by subscription | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **get_products**
> get_products(organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List products

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
    api_instance = foreman.ProductsApi(api_client)
    organization_id = 3.4 # float | Filter products by organization
    subscription_id = 3.4 # float | Filter products by subscription
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List products
        api_instance.get_products(organization_id, subscription_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Filter products by organization | 
 **subscription_id** | **float**| Filter products by subscription | 
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **get_products_id**
> get_products_id(id, organization_id=organization_id)

Show a product

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
    api_instance = foreman.ProductsApi(api_client)
    id = 3.4 # float | product numeric identifier
    organization_id = 3.4 # float | Organization ID (optional)

    try:
        # Show a product
        api_instance.get_products_id(id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ProductsApi->get_products_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| product numeric identifier | 
 **organization_id** | **float**| Organization ID | [optional] 

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

# **get_subscriptions_subscription_id_products**
> get_subscriptions_subscription_id_products(subscription_id, organization_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of subscription products in a subscription

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
    api_instance = foreman.ProductsApi(api_client)
    subscription_id = 3.4 # float | Filter products by subscription
    organization_id = 3.4 # float | Filter products by organization
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List of subscription products in a subscription
        api_instance.get_subscriptions_subscription_id_products(subscription_id, organization_id, sync_plan_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_subscriptions_subscription_id_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **float**| Filter products by subscription | 
 **organization_id** | **float**| Filter products by organization | 
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **get_sync_plans_sync_plan_id_products**
> get_sync_plans_sync_plan_id_products(sync_plan_id, organization_id, subscription_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of Products for sync plan

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
    api_instance = foreman.ProductsApi(api_client)
    sync_plan_id = 3.4 # float | Filter products by sync plan id
    organization_id = 3.4 # float | Filter products by organization
    subscription_id = 3.4 # float | Filter products by subscription
    name = 'name_example' # str | Filter products by name (optional)
    enabled = True # bool | Return enabled products only (optional)
    custom = True # bool | Return custom products only (optional)
    redhat_only = True # bool | Return Red Hat (non-custom) products only (optional)
    include_available_content = True # bool | Whether to include available content attribute in results (optional)
    available_for = 'available_for_example' # str | Interpret specified object to return only Products that can be associated with specified object.  Only 'sync_plan' is supported. (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List of Products for sync plan
        api_instance.get_sync_plans_sync_plan_id_products(sync_plan_id, organization_id, subscription_id, name=name, enabled=enabled, custom=custom, redhat_only=redhat_only, include_available_content=include_available_content, available_for=available_for, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ProductsApi->get_sync_plans_sync_plan_id_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_plan_id** | **float**| Filter products by sync plan id | 
 **organization_id** | **float**| Filter products by organization | 
 **subscription_id** | **float**| Filter products by subscription | 
 **name** | **str**| Filter products by name | [optional] 
 **enabled** | **bool**| Return enabled products only | [optional] 
 **custom** | **bool**| Return custom products only | [optional] 
 **redhat_only** | **bool**| Return Red Hat (non-custom) products only | [optional] 
 **include_available_content** | **bool**| Whether to include available content attribute in results | [optional] 
 **available_for** | **str**| Interpret specified object to return only Products that can be associated with specified object.  Only &#39;sync_plan&#39; is supported. | [optional] 
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

# **post_products**
> post_products(organization_id, name, description=description, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, sync_plan_id=sync_plan_id, label=label)

Create a product

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
    api_instance = foreman.ProductsApi(api_client)
    organization_id = 3.4 # float | ID of the organization
    name = 'name_example' # str | Product name
    description = 'description_example' # str | Product description (optional)
    gpg_key_id = 3.4 # float | Identifier of the GPG key (optional)
    ssl_ca_cert_id = 3.4 # float | Idenifier of the SSL CA Cert (optional)
    ssl_client_cert_id = 3.4 # float | Identifier of the SSL Client Cert (optional)
    ssl_client_key_id = 3.4 # float | Identifier of the SSL Client Key (optional)
    sync_plan_id = 3.4 # float | Plan numeric identifier (optional)
    label = 'label_example' # str |  (optional)

    try:
        # Create a product
        api_instance.post_products(organization_id, name, description=description, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, sync_plan_id=sync_plan_id, label=label)
    except Exception as e:
        print("Exception when calling ProductsApi->post_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization | 
 **name** | **str**| Product name | 
 **description** | **str**| Product description | [optional] 
 **gpg_key_id** | **float**| Identifier of the GPG key | [optional] 
 **ssl_ca_cert_id** | **float**| Idenifier of the SSL CA Cert | [optional] 
 **ssl_client_cert_id** | **float**| Identifier of the SSL Client Cert | [optional] 
 **ssl_client_key_id** | **float**| Identifier of the SSL Client Key | [optional] 
 **sync_plan_id** | **float**| Plan numeric identifier | [optional] 
 **label** | **str**|  | [optional] 

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

# **post_products_id_sync**
> post_products_id_sync(id)

Sync all repositories for a product

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
    api_instance = foreman.ProductsApi(api_client)
    id = 3.4 # float | product ID

    try:
        # Sync all repositories for a product
        api_instance.post_products_id_sync(id)
    except Exception as e:
        print("Exception when calling ProductsApi->post_products_id_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| product ID | 

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

# **put_products_id**
> put_products_id(id, description=description, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, sync_plan_id=sync_plan_id, name=name)

Updates a product

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
    api_instance = foreman.ProductsApi(api_client)
    id = 3.4 # float | product numeric identifier
    description = 'description_example' # str | Product description (optional)
    gpg_key_id = 3.4 # float | Identifier of the GPG key (optional)
    ssl_ca_cert_id = 3.4 # float | Idenifier of the SSL CA Cert (optional)
    ssl_client_cert_id = 3.4 # float | Identifier of the SSL Client Cert (optional)
    ssl_client_key_id = 3.4 # float | Identifier of the SSL Client Key (optional)
    sync_plan_id = 3.4 # float | Plan numeric identifier (optional)
    name = 'name_example' # str | Product name (optional)

    try:
        # Updates a product
        api_instance.put_products_id(id, description=description, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, sync_plan_id=sync_plan_id, name=name)
    except Exception as e:
        print("Exception when calling ProductsApi->put_products_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| product numeric identifier | 
 **description** | **str**| Product description | [optional] 
 **gpg_key_id** | **float**| Identifier of the GPG key | [optional] 
 **ssl_ca_cert_id** | **float**| Idenifier of the SSL CA Cert | [optional] 
 **ssl_client_cert_id** | **float**| Identifier of the SSL Client Cert | [optional] 
 **ssl_client_key_id** | **float**| Identifier of the SSL Client Key | [optional] 
 **sync_plan_id** | **float**| Plan numeric identifier | [optional] 
 **name** | **str**| Product name | [optional] 

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

