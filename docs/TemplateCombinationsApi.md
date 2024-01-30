# pyforeman.TemplateCombinationsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template_combinations_id**](TemplateCombinationsApi.md#delete_template_combinations_id) | **DELETE** /template_combinations/{id} | Delete a template combination
[**get_hostgroups_hostgroup_id_template_combinations**](TemplateCombinationsApi.md#get_hostgroups_hostgroup_id_template_combinations) | **GET** /hostgroups/{hostgroup_id}/template_combinations | List template combination
[**get_hostgroups_hostgroup_id_template_combinations_id**](TemplateCombinationsApi.md#get_hostgroups_hostgroup_id_template_combinations_id) | **GET** /hostgroups/{hostgroup_id}/template_combinations/{id} | Show template combination
[**get_provisioning_templates_provisioning_template_id_template_combinations**](TemplateCombinationsApi.md#get_provisioning_templates_provisioning_template_id_template_combinations) | **GET** /provisioning_templates/{provisioning_template_id}/template_combinations | List template combination
[**get_provisioning_templates_provisioning_template_id_template_combinations_id**](TemplateCombinationsApi.md#get_provisioning_templates_provisioning_template_id_template_combinations_id) | **GET** /provisioning_templates/{provisioning_template_id}/template_combinations/{id} | Show template combination
[**get_template_combinations_id**](TemplateCombinationsApi.md#get_template_combinations_id) | **GET** /template_combinations/{id} | Show template combination
[**post_hostgroups_hostgroup_id_template_combinations**](TemplateCombinationsApi.md#post_hostgroups_hostgroup_id_template_combinations) | **POST** /hostgroups/{hostgroup_id}/template_combinations | Add a template combination
[**post_provisioning_templates_provisioning_template_id_template_combinations**](TemplateCombinationsApi.md#post_provisioning_templates_provisioning_template_id_template_combinations) | **POST** /provisioning_templates/{provisioning_template_id}/template_combinations | Add a template combination
[**put_hostgroups_hostgroup_id_template_combinations_id**](TemplateCombinationsApi.md#put_hostgroups_hostgroup_id_template_combinations_id) | **PUT** /hostgroups/{hostgroup_id}/template_combinations/{id} | Update template combination
[**put_provisioning_templates_provisioning_template_id_template_combinations_id**](TemplateCombinationsApi.md#put_provisioning_templates_provisioning_template_id_template_combinations_id) | **PUT** /provisioning_templates/{provisioning_template_id}/template_combinations/{id} | Update template combination


# **delete_template_combinations_id**
> delete_template_combinations_id(id, location_id=location_id, organization_id=organization_id)

Delete a template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a template combination
    api_instance.delete_template_combinations_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->delete_template_combinations_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostgroups_hostgroup_id_template_combinations**
> get_hostgroups_hostgroup_id_template_combinations(hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id)

List template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List template combination
    api_instance.get_hostgroups_hostgroup_id_template_combinations(hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->get_hostgroups_hostgroup_id_template_combinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_id** | **str**| ID of host group |
 **provisioning_template_id** | **str**| ID of config template |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostgroups_hostgroup_id_template_combinations_id**
> get_hostgroups_hostgroup_id_template_combinations_id(hostgroup_id, id, provisioning_template_id, location_id=location_id, organization_id=organization_id)

Show template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
id = 'id_example' # str |
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show template combination
    api_instance.get_hostgroups_hostgroup_id_template_combinations_id(hostgroup_id, id, provisioning_template_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->get_hostgroups_hostgroup_id_template_combinations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_id** | **str**| ID of host group |
 **id** | **str**|  |
 **provisioning_template_id** | **str**| ID of config template |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provisioning_templates_provisioning_template_id_template_combinations**
> get_provisioning_templates_provisioning_template_id_template_combinations(provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id)

List template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List template combination
    api_instance.get_provisioning_templates_provisioning_template_id_template_combinations(provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->get_provisioning_templates_provisioning_template_id_template_combinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_id** | **str**| ID of config template |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provisioning_templates_provisioning_template_id_template_combinations_id**
> get_provisioning_templates_provisioning_template_id_template_combinations_id(provisioning_template_id, id, hostgroup_id, location_id=location_id, organization_id=organization_id)

Show template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
id = 'id_example' # str |
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show template combination
    api_instance.get_provisioning_templates_provisioning_template_id_template_combinations_id(provisioning_template_id, id, hostgroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->get_provisioning_templates_provisioning_template_id_template_combinations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_id** | **str**| ID of config template |
 **id** | **str**|  |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_combinations_id**
> get_template_combinations_id(id, provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id)

Show template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
id = 'id_example' # str |
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show template combination
    api_instance.get_template_combinations_id(id, provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->get_template_combinations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provisioning_template_id** | **str**| ID of config template |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hostgroups_hostgroup_id_template_combinations**
> post_hostgroups_hostgroup_id_template_combinations(hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)

Add a template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_combination_hostgroup_id = 8.14 # float | host group id (optional)

try:
    # Add a template combination
    api_instance.post_hostgroups_hostgroup_id_template_combinations(hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->post_hostgroups_hostgroup_id_template_combinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_id** | **str**| ID of host group |
 **provisioning_template_id** | **str**| ID of config template |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_combination_hostgroup_id** | **float**| host group id | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_provisioning_templates_provisioning_template_id_template_combinations**
> post_provisioning_templates_provisioning_template_id_template_combinations(provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)

Add a template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_combination_hostgroup_id = 8.14 # float | host group id (optional)

try:
    # Add a template combination
    api_instance.post_provisioning_templates_provisioning_template_id_template_combinations(provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->post_provisioning_templates_provisioning_template_id_template_combinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_id** | **str**| ID of config template |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_combination_hostgroup_id** | **float**| host group id | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hostgroups_hostgroup_id_template_combinations_id**
> put_hostgroups_hostgroup_id_template_combinations_id(id, hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)

Update template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
id = 'id_example' # str |
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_combination_hostgroup_id = 8.14 # float | host group id (optional)

try:
    # Update template combination
    api_instance.put_hostgroups_hostgroup_id_template_combinations_id(id, hostgroup_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->put_hostgroups_hostgroup_id_template_combinations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **hostgroup_id** | **str**| ID of host group |
 **provisioning_template_id** | **str**| ID of config template |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_combination_hostgroup_id** | **float**| host group id | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_provisioning_templates_provisioning_template_id_template_combinations_id**
> put_provisioning_templates_provisioning_template_id_template_combinations_id(id, provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)

Update template combination



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateCombinationsApi()
id = 'id_example' # str |
provisioning_template_id = 'provisioning_template_id_example' # str | ID of config template
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_combination_hostgroup_id = 8.14 # float | host group id (optional)

try:
    # Update template combination
    api_instance.put_provisioning_templates_provisioning_template_id_template_combinations_id(id, provisioning_template_id, hostgroup_id, location_id=location_id, organization_id=organization_id, template_combination_hostgroup_id=template_combination_hostgroup_id)
except ApiException as e:
    print("Exception when calling TemplateCombinationsApi->put_provisioning_templates_provisioning_template_id_template_combinations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **provisioning_template_id** | **str**| ID of config template |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_combination_hostgroup_id** | **float**| host group id | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
