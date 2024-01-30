# pyforeman.DomainsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_domains_id**](DomainsApi.md#delete_domains_id) | **DELETE** /domains/{id} | Delete a domain
[**get_domains**](DomainsApi.md#get_domains) | **GET** /domains | List of domains
[**get_domains_id**](DomainsApi.md#get_domains_id) | **GET** /domains/{id} | Show a domain
[**get_locations_location_id_domains**](DomainsApi.md#get_locations_location_id_domains) | **GET** /locations/{location_id}/domains | List of domains per location
[**get_organizations_organization_id_domains**](DomainsApi.md#get_organizations_organization_id_domains) | **GET** /organizations/{organization_id}/domains | List of domains per organization
[**get_subnets_subnet_id_domains**](DomainsApi.md#get_subnets_subnet_id_domains) | **GET** /subnets/{subnet_id}/domains | List of domains per subnet
[**post_domains**](DomainsApi.md#post_domains) | **POST** /domains | Create a domain
[**put_domains_id**](DomainsApi.md#put_domains_id) | **PUT** /domains/{id} | Update a domain


# **delete_domains_id**
> delete_domains_id(id, location_id=location_id, organization_id=organization_id)

Delete a domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a domain
    api_instance.delete_domains_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling DomainsApi->delete_domains_id: %s\n" % e)
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

# **get_domains**
> get_domains(subnet_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of domains



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
subnet_id = 'subnet_id_example' # str | ID of subnet
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of domains
    api_instance.get_domains(subnet_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**| ID of subnet |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains_id**
> get_domains_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
id = 'id_example' # str | Numerical ID or domain name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
show_hidden_parameters = true # bool | Display hidden parameter values (optional)

try:
    # Show a domain
    api_instance.get_domains_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domains_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Numerical ID or domain name |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **show_hidden_parameters** | **bool**| Display hidden parameter values | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_location_id_domains**
> get_locations_location_id_domains(location_id, subnet_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of domains per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
location_id = 8.14 # float | Scope by locations
subnet_id = 'subnet_id_example' # str | ID of subnet
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of domains per location
    api_instance.get_locations_location_id_domains(location_id, subnet_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling DomainsApi->get_locations_location_id_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **subnet_id** | **str**| ID of subnet |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_domains**
> get_organizations_organization_id_domains(organization_id, subnet_id, location_id, search=search, order=order, page=page, per_page=per_page)

List of domains per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
organization_id = 8.14 # float | Scope by organizations
subnet_id = 'subnet_id_example' # str | ID of subnet
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of domains per organization
    api_instance.get_organizations_organization_id_domains(organization_id, subnet_id, location_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling DomainsApi->get_organizations_organization_id_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations |
 **subnet_id** | **str**| ID of subnet |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets_subnet_id_domains**
> get_subnets_subnet_id_domains(subnet_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of domains per subnet



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
subnet_id = 'subnet_id_example' # str | ID of subnet
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of domains per subnet
    api_instance.get_subnets_subnet_id_domains(subnet_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling DomainsApi->get_subnets_subnet_id_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**| ID of subnet |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_domains**
> post_domains(domain_name, location_id=location_id, organization_id=organization_id, domain_fullname=domain_fullname, domain_dns_id=domain_dns_id, domain_domain_parameters_attributes=domain_domain_parameters_attributes, domain_location_ids=domain_location_ids, domain_organization_ids=domain_organization_ids)

Create a domain

        The <b>fullname</b> field is used for human readability in reports         and other pages that refer to domains, and also available as         an external node parameter

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
domain_name = 'domain_name_example' # str | The full DNS domain name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
domain_fullname = 'domain_fullname_example' # str | Description of the domain (optional)
domain_dns_id = 8.14 # float | DNS proxy ID to use within this domain (optional)
domain_domain_parameters_attributes = ['domain_domain_parameters_attributes_example'] # list[str] | Array of parameters (name, value) (optional)
domain_location_ids = ['domain_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
domain_organization_ids = ['domain_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create a domain
    api_instance.post_domains(domain_name, location_id=location_id, organization_id=organization_id, domain_fullname=domain_fullname, domain_dns_id=domain_dns_id, domain_domain_parameters_attributes=domain_domain_parameters_attributes, domain_location_ids=domain_location_ids, domain_organization_ids=domain_organization_ids)
except ApiException as e:
    print("Exception when calling DomainsApi->post_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The full DNS domain name |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **domain_fullname** | **str**| Description of the domain | [optional]
 **domain_dns_id** | **float**| DNS proxy ID to use within this domain | [optional]
 **domain_domain_parameters_attributes** | [**list[str]**](str.md)| Array of parameters (name, value) | [optional]
 **domain_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **domain_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_domains_id**
> put_domains_id(id, location_id=location_id, organization_id=organization_id, domain_name=domain_name, domain_fullname=domain_fullname, domain_dns_id=domain_dns_id, domain_domain_parameters_attributes=domain_domain_parameters_attributes, domain_location_ids=domain_location_ids, domain_organization_ids=domain_organization_ids)

Update a domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DomainsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
domain_name = 'domain_name_example' # str | The full DNS domain name (optional)
domain_fullname = 'domain_fullname_example' # str | Description of the domain (optional)
domain_dns_id = 8.14 # float | DNS proxy ID to use within this domain (optional)
domain_domain_parameters_attributes = ['domain_domain_parameters_attributes_example'] # list[str] | Array of parameters (name, value) (optional)
domain_location_ids = ['domain_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
domain_organization_ids = ['domain_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update a domain
    api_instance.put_domains_id(id, location_id=location_id, organization_id=organization_id, domain_name=domain_name, domain_fullname=domain_fullname, domain_dns_id=domain_dns_id, domain_domain_parameters_attributes=domain_domain_parameters_attributes, domain_location_ids=domain_location_ids, domain_organization_ids=domain_organization_ids)
except ApiException as e:
    print("Exception when calling DomainsApi->put_domains_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **domain_name** | **str**| The full DNS domain name | [optional]
 **domain_fullname** | **str**| Description of the domain | [optional]
 **domain_dns_id** | **float**| DNS proxy ID to use within this domain | [optional]
 **domain_domain_parameters_attributes** | [**list[str]**](str.md)| Array of parameters (name, value) | [optional]
 **domain_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **domain_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
