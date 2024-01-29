# foreman.ContentCredentialsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content_credentials_id**](ContentCredentialsApi.md#delete_content_credentials_id) | **DELETE** /content_credentials/{id} | Destroy a Content Credential
[**get_content_credentials**](ContentCredentialsApi.md#get_content_credentials) | **GET** /content_credentials | List Content Credentials
[**get_content_credentials_id**](ContentCredentialsApi.md#get_content_credentials_id) | **GET** /content_credentials/{id} | Show a Content Credential
[**get_content_credentials_id_content**](ContentCredentialsApi.md#get_content_credentials_id_content) | **GET** /content_credentials/{id}/content | Return the content of a Content Credential, used directly by yum
[**post_content_credentials**](ContentCredentialsApi.md#post_content_credentials) | **POST** /content_credentials | Create a Content Credential
[**post_content_credentials_id_content**](ContentCredentialsApi.md#post_content_credentials_id_content) | **POST** /content_credentials/{id}/content | Upload Content Credential contents
[**put_content_credentials_id**](ContentCredentialsApi.md#put_content_credentials_id) | **PUT** /content_credentials/{id} | Update a Content Credential


# **delete_content_credentials_id**
> delete_content_credentials_id(id)

Destroy a Content Credential

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    id = 3.4 # float | Content Credential ID

    try:
        # Destroy a Content Credential
        api_instance.delete_content_credentials_id(id)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->delete_content_credentials_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content Credential ID | 

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

# **get_content_credentials**
> get_content_credentials(organization_id, name=name, content_type=content_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List Content Credentials

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    organization_id = 3.4 # float | Organization identifier
    name = 'name_example' # str | Name of the Content Credential (optional)
    content_type = 'content_type_example' # str | Type of content (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List Content Credentials
        api_instance.get_content_credentials(organization_id, name=name, content_type=content_type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->get_content_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | 
 **name** | **str**| Name of the Content Credential | [optional] 
 **content_type** | **str**| Type of content | [optional] 
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

# **get_content_credentials_id**
> get_content_credentials_id(id)

Show a Content Credential

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    id = 3.4 # float | Content Credential numeric identifier

    try:
        # Show a Content Credential
        api_instance.get_content_credentials_id(id)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->get_content_credentials_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content Credential numeric identifier | 

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

# **get_content_credentials_id_content**
> get_content_credentials_id_content(id)

Return the content of a Content Credential, used directly by yum

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    id = 3.4 # float | 

    try:
        # Return the content of a Content Credential, used directly by yum
        api_instance.get_content_credentials_id_content(id)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->get_content_credentials_id_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

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

# **post_content_credentials**
> post_content_credentials(organization_id, name, content_type, content)

Create a Content Credential

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    organization_id = 3.4 # float | Organization identifier
    name = 'name_example' # str | Name of the Content Credential
    content_type = 'content_type_example' # str | Type of content: \\\"cert\\\", \\\"gpg_key\\\"
    content = 'content_example' # str | Public key block in DER encoding or certificate content

    try:
        # Create a Content Credential
        api_instance.post_content_credentials(organization_id, name, content_type, content)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->post_content_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | 
 **name** | **str**| Name of the Content Credential | 
 **content_type** | **str**| Type of content: \\\&quot;cert\\\&quot;, \\\&quot;gpg_key\\\&quot; | 
 **content** | **str**| Public key block in DER encoding or certificate content | 

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

# **post_content_credentials_id_content**
> post_content_credentials_id_content(id, content)

Upload Content Credential contents

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    id = 3.4 # float | Content Credential ID
    content = None # bytearray | File contents

    try:
        # Upload Content Credential contents
        api_instance.post_content_credentials_id_content(id, content)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->post_content_credentials_id_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content Credential ID | 
 **content** | **bytearray**| File contents | 

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

# **put_content_credentials_id**
> put_content_credentials_id(id, name=name, content_type=content_type, content=content)

Update a Content Credential

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
    api_instance = foreman.ContentCredentialsApi(api_client)
    id = 3.4 # float | Content Credential ID
    name = 'name_example' # str | Name of the Content Credential (optional)
    content_type = 'content_type_example' # str | Type of content: \\\"cert\\\", \\\"gpg_key\\\" (optional)
    content = 'content_example' # str | Public key block in DER encoding or certificate content (optional)

    try:
        # Update a Content Credential
        api_instance.put_content_credentials_id(id, name=name, content_type=content_type, content=content)
    except Exception as e:
        print("Exception when calling ContentCredentialsApi->put_content_credentials_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content Credential ID | 
 **name** | **str**| Name of the Content Credential | [optional] 
 **content_type** | **str**| Type of content: \\\&quot;cert\\\&quot;, \\\&quot;gpg_key\\\&quot; | [optional] 
 **content** | **str**| Public key block in DER encoding or certificate content | [optional] 

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

