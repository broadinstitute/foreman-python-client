# pyforeman.AlternateContentSourcesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alternate_content_sources_id**](AlternateContentSourcesApi.md#delete_alternate_content_sources_id) | **DELETE** /alternate_content_sources/{id} | Destroy an alternate content source.
[**get_alternate_content_sources**](AlternateContentSourcesApi.md#get_alternate_content_sources) | **GET** /alternate_content_sources | List alternate content sources.
[**get_alternate_content_sources_id**](AlternateContentSourcesApi.md#get_alternate_content_sources_id) | **GET** /alternate_content_sources/{id} | Show an alternate content source.
[**post_alternate_content_sources**](AlternateContentSourcesApi.md#post_alternate_content_sources) | **POST** /alternate_content_sources | Create an alternate content source to download content from during repository syncing.  Note: alternate content sources are global and affect ALL sync actions on their smart proxies regardless of organization.
[**post_alternate_content_sources_id_refresh**](AlternateContentSourcesApi.md#post_alternate_content_sources_id_refresh) | **POST** /alternate_content_sources/{id}/refresh | Refresh an alternate content source. Refreshing, like repository syncing, is required before using an alternate content source.
[**put_alternate_content_sources_id**](AlternateContentSourcesApi.md#put_alternate_content_sources_id) | **PUT** /alternate_content_sources/{id} | Update an alternate content source.


# **delete_alternate_content_sources_id**
> delete_alternate_content_sources_id(id)

Destroy an alternate content source.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
id = 8.14 # float | Alternate content source ID

try:
    # Destroy an alternate content source.
    api_instance.delete_alternate_content_sources_id(id)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->delete_alternate_content_sources_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Alternate content source ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alternate_content_sources**
> get_alternate_content_sources(name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List alternate content sources.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
name = 'name_example' # str | Name of the alternate content source (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List alternate content sources.
    api_instance.get_alternate_content_sources(name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->get_alternate_content_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the alternate content source | [optional]
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

# **get_alternate_content_sources_id**
> get_alternate_content_sources_id(id)

Show an alternate content source.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
id = 8.14 # float | Alternate content source ID

try:
    # Show an alternate content source.
    api_instance.get_alternate_content_sources_id(id)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->get_alternate_content_sources_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Alternate content source ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alternate_content_sources**
> post_alternate_content_sources(content_type=content_type, alternate_content_source_type=alternate_content_source_type, name=name, description=description, base_url=base_url, subpaths=subpaths, smart_proxy_ids=smart_proxy_ids, smart_proxy_names=smart_proxy_names, upstream_username=upstream_username, upstream_password=upstream_password, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, verify_ssl=verify_ssl, use_http_proxies=use_http_proxies, product_ids=product_ids)

Create an alternate content source to download content from during repository syncing.  Note: alternate content sources are global and affect ALL sync actions on their smart proxies regardless of organization.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
content_type = 'content_type_example' # str | The content type for the Alternate Content Source (optional)
alternate_content_source_type = 'alternate_content_source_type_example' # str | The Alternate Content Source type (optional)
name = 'name_example' # str | Name of the alternate content source (optional)
description = 'description_example' # str | Description for the alternate content source (optional)
base_url = 'base_url_example' # str | Base URL for finding alternate content (optional)
subpaths = ['subpaths_example'] # list[str] | Path suffixes for finding alternate content (optional)
smart_proxy_ids = ['smart_proxy_ids_example'] # list[str] | Ids of smart proxies to associate (optional)
smart_proxy_names = ['smart_proxy_names_example'] # list[str] | Names of smart proxies to associate (optional)
upstream_username = 'upstream_username_example' # str | Basic authentication username (optional)
upstream_password = 'upstream_password_example' # str | Basic authentication password (optional)
ssl_ca_cert_id = 8.14 # float | Identifier of the content credential containing the SSL CA Cert (optional)
ssl_client_cert_id = 8.14 # float | Identifier of the content credential containing the SSL Client Cert (optional)
ssl_client_key_id = 8.14 # float | Identifier of the content credential containing the SSL Client Key (optional)
verify_ssl = true # bool | If SSL should be verified for the upstream URL (optional)
use_http_proxies = true # bool | If the smart proxies' assigned HTTP proxies should be used (optional)
product_ids = ['product_ids_example'] # list[str] | IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type. (optional)

try:
    # Create an alternate content source to download content from during repository syncing.  Note: alternate content sources are global and affect ALL sync actions on their smart proxies regardless of organization.
    api_instance.post_alternate_content_sources(content_type=content_type, alternate_content_source_type=alternate_content_source_type, name=name, description=description, base_url=base_url, subpaths=subpaths, smart_proxy_ids=smart_proxy_ids, smart_proxy_names=smart_proxy_names, upstream_username=upstream_username, upstream_password=upstream_password, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, verify_ssl=verify_ssl, use_http_proxies=use_http_proxies, product_ids=product_ids)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->post_alternate_content_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type for the Alternate Content Source | [optional]
 **alternate_content_source_type** | **str**| The Alternate Content Source type | [optional]
 **name** | **str**| Name of the alternate content source | [optional]
 **description** | **str**| Description for the alternate content source | [optional]
 **base_url** | **str**| Base URL for finding alternate content | [optional]
 **subpaths** | [**list[str]**](str.md)| Path suffixes for finding alternate content | [optional]
 **smart_proxy_ids** | [**list[str]**](str.md)| Ids of smart proxies to associate | [optional]
 **smart_proxy_names** | [**list[str]**](str.md)| Names of smart proxies to associate | [optional]
 **upstream_username** | **str**| Basic authentication username | [optional]
 **upstream_password** | **str**| Basic authentication password | [optional]
 **ssl_ca_cert_id** | **float**| Identifier of the content credential containing the SSL CA Cert | [optional]
 **ssl_client_cert_id** | **float**| Identifier of the content credential containing the SSL Client Cert | [optional]
 **ssl_client_key_id** | **float**| Identifier of the content credential containing the SSL Client Key | [optional]
 **verify_ssl** | **bool**| If SSL should be verified for the upstream URL | [optional]
 **use_http_proxies** | **bool**| If the smart proxies&#39; assigned HTTP proxies should be used | [optional]
 **product_ids** | [**list[str]**](str.md)| IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alternate_content_sources_id_refresh**
> post_alternate_content_sources_id_refresh(id)

Refresh an alternate content source. Refreshing, like repository syncing, is required before using an alternate content source.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
id = 8.14 # float | Alternate content source ID

try:
    # Refresh an alternate content source. Refreshing, like repository syncing, is required before using an alternate content source.
    api_instance.post_alternate_content_sources_id_refresh(id)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->post_alternate_content_sources_id_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Alternate content source ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alternate_content_sources_id**
> put_alternate_content_sources_id(id, name=name, description=description, base_url=base_url, subpaths=subpaths, smart_proxy_ids=smart_proxy_ids, smart_proxy_names=smart_proxy_names, upstream_username=upstream_username, upstream_password=upstream_password, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, verify_ssl=verify_ssl, use_http_proxies=use_http_proxies, product_ids=product_ids)

Update an alternate content source.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesApi()
id = 8.14 # float | Alternate content source ID
name = 'name_example' # str | Name of the alternate content source (optional)
description = 'description_example' # str | Description for the alternate content source (optional)
base_url = 'base_url_example' # str | Base URL for finding alternate content (optional)
subpaths = ['subpaths_example'] # list[str] | Path suffixes for finding alternate content (optional)
smart_proxy_ids = ['smart_proxy_ids_example'] # list[str] | Ids of smart proxies to associate (optional)
smart_proxy_names = ['smart_proxy_names_example'] # list[str] | Names of smart proxies to associate (optional)
upstream_username = 'upstream_username_example' # str | Basic authentication username (optional)
upstream_password = 'upstream_password_example' # str | Basic authentication password (optional)
ssl_ca_cert_id = 8.14 # float | Identifier of the content credential containing the SSL CA Cert (optional)
ssl_client_cert_id = 8.14 # float | Identifier of the content credential containing the SSL Client Cert (optional)
ssl_client_key_id = 8.14 # float | Identifier of the content credential containing the SSL Client Key (optional)
verify_ssl = true # bool | If SSL should be verified for the upstream URL (optional)
use_http_proxies = true # bool | If the smart proxies' assigned HTTP proxies should be used (optional)
product_ids = ['product_ids_example'] # list[str] | IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type. (optional)

try:
    # Update an alternate content source.
    api_instance.put_alternate_content_sources_id(id, name=name, description=description, base_url=base_url, subpaths=subpaths, smart_proxy_ids=smart_proxy_ids, smart_proxy_names=smart_proxy_names, upstream_username=upstream_username, upstream_password=upstream_password, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, verify_ssl=verify_ssl, use_http_proxies=use_http_proxies, product_ids=product_ids)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesApi->put_alternate_content_sources_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Alternate content source ID |
 **name** | **str**| Name of the alternate content source | [optional]
 **description** | **str**| Description for the alternate content source | [optional]
 **base_url** | **str**| Base URL for finding alternate content | [optional]
 **subpaths** | [**list[str]**](str.md)| Path suffixes for finding alternate content | [optional]
 **smart_proxy_ids** | [**list[str]**](str.md)| Ids of smart proxies to associate | [optional]
 **smart_proxy_names** | [**list[str]**](str.md)| Names of smart proxies to associate | [optional]
 **upstream_username** | **str**| Basic authentication username | [optional]
 **upstream_password** | **str**| Basic authentication password | [optional]
 **ssl_ca_cert_id** | **float**| Identifier of the content credential containing the SSL CA Cert | [optional]
 **ssl_client_cert_id** | **float**| Identifier of the content credential containing the SSL Client Cert | [optional]
 **ssl_client_key_id** | **float**| Identifier of the content credential containing the SSL Client Key | [optional]
 **verify_ssl** | **bool**| If SSL should be verified for the upstream URL | [optional]
 **use_http_proxies** | **bool**| If the smart proxies&#39; assigned HTTP proxies should be used | [optional]
 **product_ids** | [**list[str]**](str.md)| IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
