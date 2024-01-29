# foreman.ImagesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compute_resources_compute_resource_id_images_id**](ImagesApi.md#delete_compute_resources_compute_resource_id_images_id) | **DELETE** /compute_resources/{compute_resource_id}/images/{id} | Delete an image
[**get_architectures_architecture_id_images**](ImagesApi.md#get_architectures_architecture_id_images) | **GET** /architectures/{architecture_id}/images | List all images for architecture
[**get_architectures_architecture_id_images_id**](ImagesApi.md#get_architectures_architecture_id_images_id) | **GET** /architectures/{architecture_id}/images/{id} | Show an image
[**get_compute_resources_compute_resource_id_images**](ImagesApi.md#get_compute_resources_compute_resource_id_images) | **GET** /compute_resources/{compute_resource_id}/images | List all images for a compute resource
[**get_compute_resources_compute_resource_id_images_id**](ImagesApi.md#get_compute_resources_compute_resource_id_images_id) | **GET** /compute_resources/{compute_resource_id}/images/{id} | Show an image
[**get_operatingsystems_operatingsystem_id_images**](ImagesApi.md#get_operatingsystems_operatingsystem_id_images) | **GET** /operatingsystems/{operatingsystem_id}/images | List all images for operating system
[**get_operatingsystems_operatingsystem_id_images_id**](ImagesApi.md#get_operatingsystems_operatingsystem_id_images_id) | **GET** /operatingsystems/{operatingsystem_id}/images/{id} | Show an image
[**post_compute_resources_compute_resource_id_images**](ImagesApi.md#post_compute_resources_compute_resource_id_images) | **POST** /compute_resources/{compute_resource_id}/images | Create an image
[**put_compute_resources_compute_resource_id_images_id**](ImagesApi.md#put_compute_resources_compute_resource_id_images_id) | **PUT** /compute_resources/{compute_resource_id}/images/{id} | Update an image


# **delete_compute_resources_compute_resource_id_images_id**
> delete_compute_resources_compute_resource_id_images_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id)

Delete an image

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
    api_instance = foreman.ImagesApi(api_client)
    compute_resource_id = 'compute_resource_id_example' # str | 
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete an image
        api_instance.delete_compute_resources_compute_resource_id_images_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_compute_resources_compute_resource_id_images_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**|  | 
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_architectures_architecture_id_images**
> get_architectures_architecture_id_images(architecture_id, compute_resource_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all images for architecture

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
    api_instance = foreman.ImagesApi(api_client)
    architecture_id = 'architecture_id_example' # str | ID of architecture
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all images for architecture
        api_instance.get_architectures_architecture_id_images(architecture_id, compute_resource_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ImagesApi->get_architectures_architecture_id_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architecture_id** | **str**| ID of architecture | 
 **compute_resource_id** | **str**| ID of compute resource | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_architectures_architecture_id_images_id**
> get_architectures_architecture_id_images_id(id, architecture_id, compute_resource_id, operatingsystem_id, location_id=location_id, organization_id=organization_id)

Show an image

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
    api_instance = foreman.ImagesApi(api_client)
    id = 'id_example' # str | 
    architecture_id = 'architecture_id_example' # str | ID of architecture
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show an image
        api_instance.get_architectures_architecture_id_images_id(id, architecture_id, compute_resource_id, operatingsystem_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ImagesApi->get_architectures_architecture_id_images_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **architecture_id** | **str**| ID of architecture | 
 **compute_resource_id** | **str**| ID of compute resource | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_compute_resources_compute_resource_id_images**
> get_compute_resources_compute_resource_id_images(compute_resource_id, architecture_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all images for a compute resource

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
    api_instance = foreman.ImagesApi(api_client)
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    architecture_id = 'architecture_id_example' # str | ID of architecture
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all images for a compute resource
        api_instance.get_compute_resources_compute_resource_id_images(compute_resource_id, architecture_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ImagesApi->get_compute_resources_compute_resource_id_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**| ID of compute resource | 
 **architecture_id** | **str**| ID of architecture | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_compute_resources_compute_resource_id_images_id**
> get_compute_resources_compute_resource_id_images_id(id, compute_resource_id, architecture_id, operatingsystem_id, location_id=location_id, organization_id=organization_id)

Show an image

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
    api_instance = foreman.ImagesApi(api_client)
    id = 'id_example' # str | 
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    architecture_id = 'architecture_id_example' # str | ID of architecture
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show an image
        api_instance.get_compute_resources_compute_resource_id_images_id(id, compute_resource_id, architecture_id, operatingsystem_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ImagesApi->get_compute_resources_compute_resource_id_images_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **compute_resource_id** | **str**| ID of compute resource | 
 **architecture_id** | **str**| ID of architecture | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_operatingsystems_operatingsystem_id_images**
> get_operatingsystems_operatingsystem_id_images(operatingsystem_id, compute_resource_id, architecture_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all images for operating system

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
    api_instance = foreman.ImagesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    architecture_id = 'architecture_id_example' # str | ID of architecture
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all images for operating system
        api_instance.get_operatingsystems_operatingsystem_id_images(operatingsystem_id, compute_resource_id, architecture_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling ImagesApi->get_operatingsystems_operatingsystem_id_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **compute_resource_id** | **str**| ID of compute resource | 
 **architecture_id** | **str**| ID of architecture | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_operatingsystems_operatingsystem_id_images_id**
> get_operatingsystems_operatingsystem_id_images_id(id, operatingsystem_id, compute_resource_id, architecture_id, location_id=location_id, organization_id=organization_id)

Show an image

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
    api_instance = foreman.ImagesApi(api_client)
    id = 'id_example' # str | 
    operatingsystem_id = 3.4 # float | ID of operating system
    compute_resource_id = 'compute_resource_id_example' # str | ID of compute resource
    architecture_id = 'architecture_id_example' # str | ID of architecture
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show an image
        api_instance.get_operatingsystems_operatingsystem_id_images_id(id, operatingsystem_id, compute_resource_id, architecture_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ImagesApi->get_operatingsystems_operatingsystem_id_images_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **compute_resource_id** | **str**| ID of compute resource | 
 **architecture_id** | **str**| ID of architecture | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **post_compute_resources_compute_resource_id_images**
> post_compute_resources_compute_resource_id_images(compute_resource_id, image_name, image_username, image_uuid, location_id=location_id, organization_id=organization_id, image_password=image_password, image_compute_resource_id=image_compute_resource_id, image_architecture_id=image_architecture_id, image_operatingsystem_id=image_operatingsystem_id, image_user_data=image_user_data)

Create an image

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
    api_instance = foreman.ImagesApi(api_client)
    compute_resource_id = 'compute_resource_id_example' # str | 
    image_name = 'image_name_example' # str | 
    image_username = 'image_username_example' # str | 
    image_uuid = 'image_uuid_example' # str | Template ID in the compute resource
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    image_password = 'image_password_example' # str |  (optional)
    image_compute_resource_id = 'image_compute_resource_id_example' # str | ID of compute resource (optional)
    image_architecture_id = 'image_architecture_id_example' # str | ID of architecture (optional)
    image_operatingsystem_id = 3.4 # float | ID of operating system (optional)
    image_user_data = True # bool | Whether or not the image supports user data (optional)

    try:
        # Create an image
        api_instance.post_compute_resources_compute_resource_id_images(compute_resource_id, image_name, image_username, image_uuid, location_id=location_id, organization_id=organization_id, image_password=image_password, image_compute_resource_id=image_compute_resource_id, image_architecture_id=image_architecture_id, image_operatingsystem_id=image_operatingsystem_id, image_user_data=image_user_data)
    except Exception as e:
        print("Exception when calling ImagesApi->post_compute_resources_compute_resource_id_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**|  | 
 **image_name** | **str**|  | 
 **image_username** | **str**|  | 
 **image_uuid** | **str**| Template ID in the compute resource | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **image_password** | **str**|  | [optional] 
 **image_compute_resource_id** | **str**| ID of compute resource | [optional] 
 **image_architecture_id** | **str**| ID of architecture | [optional] 
 **image_operatingsystem_id** | **float**| ID of operating system | [optional] 
 **image_user_data** | **bool**| Whether or not the image supports user data | [optional] 

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

# **put_compute_resources_compute_resource_id_images_id**
> put_compute_resources_compute_resource_id_images_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id, image_name=image_name, image_username=image_username, image_uuid=image_uuid, image_password=image_password, image_compute_resource_id=image_compute_resource_id, image_architecture_id=image_architecture_id, image_operatingsystem_id=image_operatingsystem_id, image_user_data=image_user_data)

Update an image

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
    api_instance = foreman.ImagesApi(api_client)
    compute_resource_id = 'compute_resource_id_example' # str | 
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    image_name = 'image_name_example' # str |  (optional)
    image_username = 'image_username_example' # str |  (optional)
    image_uuid = 'image_uuid_example' # str | Template ID in the compute resource (optional)
    image_password = 'image_password_example' # str |  (optional)
    image_compute_resource_id = 'image_compute_resource_id_example' # str | ID of compute resource (optional)
    image_architecture_id = 'image_architecture_id_example' # str | ID of architecture (optional)
    image_operatingsystem_id = 3.4 # float | ID of operating system (optional)
    image_user_data = True # bool | Whether or not the image supports user data (optional)

    try:
        # Update an image
        api_instance.put_compute_resources_compute_resource_id_images_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id, image_name=image_name, image_username=image_username, image_uuid=image_uuid, image_password=image_password, image_compute_resource_id=image_compute_resource_id, image_architecture_id=image_architecture_id, image_operatingsystem_id=image_operatingsystem_id, image_user_data=image_user_data)
    except Exception as e:
        print("Exception when calling ImagesApi->put_compute_resources_compute_resource_id_images_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**|  | 
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **image_name** | **str**|  | [optional] 
 **image_username** | **str**|  | [optional] 
 **image_uuid** | **str**| Template ID in the compute resource | [optional] 
 **image_password** | **str**|  | [optional] 
 **image_compute_resource_id** | **str**| ID of compute resource | [optional] 
 **image_architecture_id** | **str**| ID of architecture | [optional] 
 **image_operatingsystem_id** | **float**| ID of operating system | [optional] 
 **image_user_data** | **bool**| Whether or not the image supports user data | [optional] 

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

