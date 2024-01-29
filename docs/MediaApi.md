# foreman.MediaApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_id**](MediaApi.md#delete_media_id) | **DELETE** /media/{id} | Delete a medium
[**get_locations_location_id_media**](MediaApi.md#get_locations_location_id_media) | **GET** /locations/{location_id}/media | List all media per location
[**get_media**](MediaApi.md#get_media) | **GET** /media | List all installation media
[**get_media_id**](MediaApi.md#get_media_id) | **GET** /media/{id} | Show a medium
[**get_operatingsystems_operatingsystem_id_media**](MediaApi.md#get_operatingsystems_operatingsystem_id_media) | **GET** /operatingsystems/{operatingsystem_id}/media | List all media for an operating system
[**get_organizations_organization_id_media**](MediaApi.md#get_organizations_organization_id_media) | **GET** /organizations/{organization_id}/media | List all media per organization
[**post_media**](MediaApi.md#post_media) | **POST** /media | Create a medium
[**put_media_id**](MediaApi.md#put_media_id) | **PUT** /media/{id} | Update a medium


# **delete_media_id**
> delete_media_id(id, location_id=location_id, organization_id=organization_id)

Delete a medium

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
    api_instance = foreman.MediaApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a medium
        api_instance.delete_media_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_locations_location_id_media**
> get_locations_location_id_media(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all media per location

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
    api_instance = foreman.MediaApi(api_client)
    location_id = 3.4 # float | Scope by locations
    operatingsystem_id = 3.4 # float | ID of operating system
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all media per location
        api_instance.get_locations_location_id_media(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling MediaApi->get_locations_location_id_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_media**
> get_media(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all installation media

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
    api_instance = foreman.MediaApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all installation media
        api_instance.get_media(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_media_id**
> get_media_id(id, location_id=location_id, organization_id=organization_id)

Show a medium

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
    api_instance = foreman.MediaApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a medium
        api_instance.get_media_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **get_operatingsystems_operatingsystem_id_media**
> get_operatingsystems_operatingsystem_id_media(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all media for an operating system

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
    api_instance = foreman.MediaApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all media for an operating system
        api_instance.get_operatingsystems_operatingsystem_id_media(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling MediaApi->get_operatingsystems_operatingsystem_id_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_organizations_organization_id_media**
> get_organizations_organization_id_media(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)

List all media per organization

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
    api_instance = foreman.MediaApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all media per organization
        api_instance.get_organizations_organization_id_media(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling MediaApi->get_organizations_organization_id_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
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

# **post_media**
> post_media(medium_name, medium_path, location_id=location_id, organization_id=organization_id, medium_os_family=medium_os_family, medium_operatingsystem_ids=medium_operatingsystem_ids, medium_location_ids=medium_location_ids, medium_organization_ids=medium_organization_ids)

Create a medium

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
    api_instance = foreman.MediaApi(api_client)
    medium_name = 'medium_name_example' # str | Name of media
    medium_path = 'medium_path_example' # str | The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).  for example http://mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host's actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.  Solaris and Debian media may also use $release. 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    medium_os_family = 'medium_os_family_example' # str | Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver (optional)
    medium_operatingsystem_ids = ['medium_operatingsystem_ids_example'] # List[str] |  (optional)
    medium_location_ids = ['medium_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    medium_organization_ids = ['medium_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create a medium
        api_instance.post_media(medium_name, medium_path, location_id=location_id, organization_id=organization_id, medium_os_family=medium_os_family, medium_operatingsystem_ids=medium_operatingsystem_ids, medium_location_ids=medium_location_ids, medium_organization_ids=medium_organization_ids)
    except Exception as e:
        print("Exception when calling MediaApi->post_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_name** | **str**| Name of media | 
 **medium_path** | **str**| The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).  for example http://mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host&#39;s actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.  Solaris and Debian media may also use $release.  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **medium_os_family** | **str**| Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver | [optional] 
 **medium_operatingsystem_ids** | [**List[str]**](str.md)|  | [optional] 
 **medium_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **medium_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **put_media_id**
> put_media_id(id, location_id=location_id, organization_id=organization_id, medium_name=medium_name, medium_path=medium_path, medium_os_family=medium_os_family, medium_operatingsystem_ids=medium_operatingsystem_ids, medium_location_ids=medium_location_ids, medium_organization_ids=medium_organization_ids)

Update a medium

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
    api_instance = foreman.MediaApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    medium_name = 'medium_name_example' # str | Name of media (optional)
    medium_path = 'medium_path_example' # str | The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).  for example http://mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host's actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.  Solaris and Debian media may also use $release.  (optional)
    medium_os_family = 'medium_os_family_example' # str | Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver (optional)
    medium_operatingsystem_ids = ['medium_operatingsystem_ids_example'] # List[str] |  (optional)
    medium_location_ids = ['medium_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    medium_organization_ids = ['medium_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update a medium
        api_instance.put_media_id(id, location_id=location_id, organization_id=organization_id, medium_name=medium_name, medium_path=medium_path, medium_os_family=medium_os_family, medium_operatingsystem_ids=medium_operatingsystem_ids, medium_location_ids=medium_location_ids, medium_organization_ids=medium_organization_ids)
    except Exception as e:
        print("Exception when calling MediaApi->put_media_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **medium_name** | **str**| Name of media | [optional] 
 **medium_path** | **str**| The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).  for example http://mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host&#39;s actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.  Solaris and Debian media may also use $release.  | [optional] 
 **medium_os_family** | **str**| Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver | [optional] 
 **medium_operatingsystem_ids** | [**List[str]**](str.md)|  | [optional] 
 **medium_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **medium_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

