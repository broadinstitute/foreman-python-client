# pyforeman.ContentViewComponentsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_views_composite_content_view_id_content_view_components**](ContentViewComponentsApi.md#get_content_views_composite_content_view_id_content_view_components) | **GET** /content_views/{composite_content_view_id}/content_view_components | List components attached to this content view
[**get_content_views_composite_content_view_id_content_view_components_id**](ContentViewComponentsApi.md#get_content_views_composite_content_view_id_content_view_components_id) | **GET** /content_views/{composite_content_view_id}/content_view_components/{id} | Show a content view component
[**put_content_views_composite_content_view_id_content_view_components_add**](ContentViewComponentsApi.md#put_content_views_composite_content_view_id_content_view_components_add) | **PUT** /content_views/{composite_content_view_id}/content_view_components/add | Add components to the content view
[**put_content_views_composite_content_view_id_content_view_components_id**](ContentViewComponentsApi.md#put_content_views_composite_content_view_id_content_view_components_id) | **PUT** /content_views/{composite_content_view_id}/content_view_components/{id} | Update a component associated with the content view
[**put_content_views_composite_content_view_id_content_view_components_remove**](ContentViewComponentsApi.md#put_content_views_composite_content_view_id_content_view_components_remove) | **PUT** /content_views/{composite_content_view_id}/content_view_components/remove | Remove components from the content view


# **get_content_views_composite_content_view_id_content_view_components**
> get_content_views_composite_content_view_id_content_view_components(composite_content_view_id)

List components attached to this content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewComponentsApi()
composite_content_view_id = 8.14 # float | composite content view identifier

try:
    # List components attached to this content view
    api_instance.get_content_views_composite_content_view_id_content_view_components(composite_content_view_id)
except ApiException as e:
    print("Exception when calling ContentViewComponentsApi->get_content_views_composite_content_view_id_content_view_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **composite_content_view_id** | **float**| composite content view identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_views_composite_content_view_id_content_view_components_id**
> get_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id)

Show a content view component



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewComponentsApi()
composite_content_view_id = 8.14 # float | composite content view numeric identifier
id = 8.14 # float | content view component ID. Identifier of the component association

try:
    # Show a content view component
    api_instance.get_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id)
except ApiException as e:
    print("Exception when calling ContentViewComponentsApi->get_content_views_composite_content_view_id_content_view_components_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **composite_content_view_id** | **float**| composite content view numeric identifier |
 **id** | **float**| content view component ID. Identifier of the component association |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_composite_content_view_id_content_view_components_add**
> put_content_views_composite_content_view_id_content_view_components_add(composite_content_view_id, components)

Add components to the content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewComponentsApi()
composite_content_view_id = 8.14 # float | composite content view identifier
components = ['components_example'] # list[str] | Array of components to add

try:
    # Add components to the content view
    api_instance.put_content_views_composite_content_view_id_content_view_components_add(composite_content_view_id, components)
except ApiException as e:
    print("Exception when calling ContentViewComponentsApi->put_content_views_composite_content_view_id_content_view_components_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **composite_content_view_id** | **float**| composite content view identifier |
 **components** | [**list[str]**](str.md)| Array of components to add |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_composite_content_view_id_content_view_components_id**
> put_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id, content_view_version_id=content_view_version_id, latest=latest)

Update a component associated with the content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewComponentsApi()
composite_content_view_id = 8.14 # float | composite content view identifier
id = 8.14 # float | content view component ID. Identifier of the component association
content_view_version_id = 8.14 # float | identifier of the version of the component content view (optional)
latest = true # bool | true if the latest version of the components content view is desired (optional)

try:
    # Update a component associated with the content view
    api_instance.put_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id, content_view_version_id=content_view_version_id, latest=latest)
except ApiException as e:
    print("Exception when calling ContentViewComponentsApi->put_content_views_composite_content_view_id_content_view_components_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **composite_content_view_id** | **float**| composite content view identifier |
 **id** | **float**| content view component ID. Identifier of the component association |
 **content_view_version_id** | **float**| identifier of the version of the component content view | [optional]
 **latest** | **bool**| true if the latest version of the components content view is desired | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_composite_content_view_id_content_view_components_remove**
> put_content_views_composite_content_view_id_content_view_components_remove(composite_content_view_id, component_ids)

Remove components from the content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewComponentsApi()
composite_content_view_id = 8.14 # float | composite content view identifier
component_ids = ['component_ids_example'] # list[str] | Array of content view component IDs to remove. Identifier of the component association

try:
    # Remove components from the content view
    api_instance.put_content_views_composite_content_view_id_content_view_components_remove(composite_content_view_id, component_ids)
except ApiException as e:
    print("Exception when calling ContentViewComponentsApi->put_content_views_composite_content_view_id_content_view_components_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **composite_content_view_id** | **float**| composite content view identifier |
 **component_ids** | [**list[str]**](str.md)| Array of content view component IDs to remove. Identifier of the component association |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
