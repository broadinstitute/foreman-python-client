# pyforeman.TemplateInputsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_templates_template_id_template_inputs_id**](TemplateInputsApi.md#delete_templates_template_id_template_inputs_id) | **DELETE** /templates/{template_id}/template_inputs/{id} | Delete a template input
[**get_templates_template_id_template_inputs**](TemplateInputsApi.md#get_templates_template_id_template_inputs) | **GET** /templates/{template_id}/template_inputs | List template inputs
[**get_templates_template_id_template_inputs_id**](TemplateInputsApi.md#get_templates_template_id_template_inputs_id) | **GET** /templates/{template_id}/template_inputs/{id} | Show template input details
[**post_templates_template_id_template_inputs**](TemplateInputsApi.md#post_templates_template_id_template_inputs) | **POST** /templates/{template_id}/template_inputs | Create a template input
[**put_templates_template_id_template_inputs_id**](TemplateInputsApi.md#put_templates_template_id_template_inputs_id) | **PUT** /templates/{template_id}/template_inputs/{id} | Update a template input


# **delete_templates_template_id_template_inputs_id**
> delete_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id)

Delete a template input



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateInputsApi()
template_id = 'template_id_example' # str |
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a template input
    api_instance.delete_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateInputsApi->delete_templates_template_id_template_inputs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
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

# **get_templates_template_id_template_inputs**
> get_templates_template_id_template_inputs(template_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List template inputs



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateInputsApi()
template_id = 'template_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List template inputs
    api_instance.get_templates_template_id_template_inputs(template_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling TemplateInputsApi->get_templates_template_id_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates_template_id_template_inputs_id**
> get_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id)

Show template input details



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateInputsApi()
template_id = 'template_id_example' # str |
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show template input details
    api_instance.get_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling TemplateInputsApi->get_templates_template_id_template_inputs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
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

# **post_templates_template_id_template_inputs**
> post_templates_template_id_template_inputs(template_id, template_input_name, template_input_input_type, location_id=location_id, organization_id=organization_id, template_input_description=template_input_description, template_input_required=template_input_required, template_input_advanced=template_input_advanced, template_input_fact_name=template_input_fact_name, template_input_variable_name=template_input_variable_name, template_input_options=template_input_options, template_input_default=template_input_default, template_input_hidden_value=template_input_hidden_value, template_input_value_type=template_input_value_type, template_input_resource_type=template_input_resource_type)

Create a template input



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateInputsApi()
template_id = 'template_id_example' # str |
template_input_name = 'template_input_name_example' # str | Input name
template_input_input_type = 'template_input_input_type_example' # str | Input type
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_input_description = 'template_input_description_example' # str | Input description (optional)
template_input_required = true # bool | Input is required (optional)
template_input_advanced = true # bool | Input is advanced (optional)
template_input_fact_name = 'template_input_fact_name_example' # str | Fact name, used when input type is Fact value (optional)
template_input_variable_name = 'template_input_variable_name_example' # str | Variable name, used when input type is Variable (optional)
template_input_options = ['template_input_options_example'] # list[str] | Selectable values for user inputs (optional)
template_input_default = 'template_input_default_example' # str | Default value for user input (optional)
template_input_hidden_value = true # bool | The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords (optional)
template_input_value_type = 'template_input_value_type_example' # str | Value type, defaults to plain (optional)
template_input_resource_type = 'template_input_resource_type_example' # str | For values of type search, this is the resource the value searches in (optional)

try:
    # Create a template input
    api_instance.post_templates_template_id_template_inputs(template_id, template_input_name, template_input_input_type, location_id=location_id, organization_id=organization_id, template_input_description=template_input_description, template_input_required=template_input_required, template_input_advanced=template_input_advanced, template_input_fact_name=template_input_fact_name, template_input_variable_name=template_input_variable_name, template_input_options=template_input_options, template_input_default=template_input_default, template_input_hidden_value=template_input_hidden_value, template_input_value_type=template_input_value_type, template_input_resource_type=template_input_resource_type)
except ApiException as e:
    print("Exception when calling TemplateInputsApi->post_templates_template_id_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
 **template_input_name** | **str**| Input name |
 **template_input_input_type** | **str**| Input type |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_input_description** | **str**| Input description | [optional]
 **template_input_required** | **bool**| Input is required | [optional]
 **template_input_advanced** | **bool**| Input is advanced | [optional]
 **template_input_fact_name** | **str**| Fact name, used when input type is Fact value | [optional]
 **template_input_variable_name** | **str**| Variable name, used when input type is Variable | [optional]
 **template_input_options** | [**list[str]**](str.md)| Selectable values for user inputs | [optional]
 **template_input_default** | **str**| Default value for user input | [optional]
 **template_input_hidden_value** | **bool**| The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords | [optional]
 **template_input_value_type** | **str**| Value type, defaults to plain | [optional]
 **template_input_resource_type** | **str**| For values of type search, this is the resource the value searches in | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_templates_template_id_template_inputs_id**
> put_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id, template_input_name=template_input_name, template_input_description=template_input_description, template_input_required=template_input_required, template_input_advanced=template_input_advanced, template_input_input_type=template_input_input_type, template_input_fact_name=template_input_fact_name, template_input_variable_name=template_input_variable_name, template_input_options=template_input_options, template_input_default=template_input_default, template_input_hidden_value=template_input_hidden_value, template_input_value_type=template_input_value_type, template_input_resource_type=template_input_resource_type)

Update a template input



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.TemplateInputsApi()
template_id = 'template_id_example' # str |
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
template_input_name = 'template_input_name_example' # str | Input name (optional)
template_input_description = 'template_input_description_example' # str | Input description (optional)
template_input_required = true # bool | Input is required (optional)
template_input_advanced = true # bool | Input is advanced (optional)
template_input_input_type = 'template_input_input_type_example' # str | Input type (optional)
template_input_fact_name = 'template_input_fact_name_example' # str | Fact name, used when input type is Fact value (optional)
template_input_variable_name = 'template_input_variable_name_example' # str | Variable name, used when input type is Variable (optional)
template_input_options = ['template_input_options_example'] # list[str] | Selectable values for user inputs (optional)
template_input_default = 'template_input_default_example' # str | Default value for user input (optional)
template_input_hidden_value = true # bool | The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords (optional)
template_input_value_type = 'template_input_value_type_example' # str | Value type, defaults to plain (optional)
template_input_resource_type = 'template_input_resource_type_example' # str | For values of type search, this is the resource the value searches in (optional)

try:
    # Update a template input
    api_instance.put_templates_template_id_template_inputs_id(template_id, id, location_id=location_id, organization_id=organization_id, template_input_name=template_input_name, template_input_description=template_input_description, template_input_required=template_input_required, template_input_advanced=template_input_advanced, template_input_input_type=template_input_input_type, template_input_fact_name=template_input_fact_name, template_input_variable_name=template_input_variable_name, template_input_options=template_input_options, template_input_default=template_input_default, template_input_hidden_value=template_input_hidden_value, template_input_value_type=template_input_value_type, template_input_resource_type=template_input_resource_type)
except ApiException as e:
    print("Exception when calling TemplateInputsApi->put_templates_template_id_template_inputs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **template_input_name** | **str**| Input name | [optional]
 **template_input_description** | **str**| Input description | [optional]
 **template_input_required** | **bool**| Input is required | [optional]
 **template_input_advanced** | **bool**| Input is advanced | [optional]
 **template_input_input_type** | **str**| Input type | [optional]
 **template_input_fact_name** | **str**| Fact name, used when input type is Fact value | [optional]
 **template_input_variable_name** | **str**| Variable name, used when input type is Variable | [optional]
 **template_input_options** | [**list[str]**](str.md)| Selectable values for user inputs | [optional]
 **template_input_default** | **str**| Default value for user input | [optional]
 **template_input_hidden_value** | **bool**| The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords | [optional]
 **template_input_value_type** | **str**| Value type, defaults to plain | [optional]
 **template_input_resource_type** | **str**| For values of type search, this is the resource the value searches in | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
