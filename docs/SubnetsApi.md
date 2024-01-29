# foreman.SubnetsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subnets_id**](SubnetsApi.md#delete_subnets_id) | **DELETE** /subnets/{id} | Delete a subnet
[**get_domains_domain_id_subnets**](SubnetsApi.md#get_domains_domain_id_subnets) | **GET** /domains/{domain_id}/subnets | List of subnets for a domain
[**get_locations_location_id_subnets**](SubnetsApi.md#get_locations_location_id_subnets) | **GET** /locations/{location_id}/subnets | List of subnets per location
[**get_organizations_organization_id_subnets**](SubnetsApi.md#get_organizations_organization_id_subnets) | **GET** /organizations/{organization_id}/subnets | List of subnets per organization
[**get_subnets**](SubnetsApi.md#get_subnets) | **GET** /subnets | List of subnets
[**get_subnets_id**](SubnetsApi.md#get_subnets_id) | **GET** /subnets/{id} | Show a subnet
[**get_subnets_id_freeip**](SubnetsApi.md#get_subnets_id_freeip) | **GET** /subnets/{id}/freeip | Provides an unused IP address in this subnet
[**post_subnets**](SubnetsApi.md#post_subnets) | **POST** /subnets | Create a subnet
[**put_subnets_id**](SubnetsApi.md#put_subnets_id) | **PUT** /subnets/{id} | Update a subnet


# **delete_subnets_id**
> delete_subnets_id(id, location_id=location_id, organization_id=organization_id)

Delete a subnet

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
    api_instance = foreman.SubnetsApi(api_client)
    id = 3.4 # float | Subnet numeric identifier
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a subnet
        api_instance.delete_subnets_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SubnetsApi->delete_subnets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Subnet numeric identifier | 
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

# **get_domains_domain_id_subnets**
> get_domains_domain_id_subnets(domain_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of subnets for a domain

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
    api_instance = foreman.SubnetsApi(api_client)
    domain_id = 'domain_id_example' # str | ID of domain
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List of subnets for a domain
        api_instance.get_domains_domain_id_subnets(domain_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_domains_domain_id_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| ID of domain | 
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

# **get_locations_location_id_subnets**
> get_locations_location_id_subnets(location_id, domain_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of subnets per location

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
    api_instance = foreman.SubnetsApi(api_client)
    location_id = 3.4 # float | Scope by locations
    domain_id = 'domain_id_example' # str | ID of domain
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List of subnets per location
        api_instance.get_locations_location_id_subnets(location_id, domain_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_locations_location_id_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | 
 **domain_id** | **str**| ID of domain | 
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

# **get_organizations_organization_id_subnets**
> get_organizations_organization_id_subnets(organization_id, domain_id, location_id, search=search, order=order, page=page, per_page=per_page)

List of subnets per organization

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
    api_instance = foreman.SubnetsApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    domain_id = 'domain_id_example' # str | ID of domain
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List of subnets per organization
        api_instance.get_organizations_organization_id_subnets(organization_id, domain_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_organizations_organization_id_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations | 
 **domain_id** | **str**| ID of domain | 
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

# **get_subnets**
> get_subnets(domain_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List of subnets

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
    api_instance = foreman.SubnetsApi(api_client)
    domain_id = 'domain_id_example' # str | ID of domain
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List of subnets
        api_instance.get_subnets(domain_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| ID of domain | 
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

# **get_subnets_id**
> get_subnets_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a subnet

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
    api_instance = foreman.SubnetsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    show_hidden_parameters = True # bool | Display hidden parameter values (optional)

    try:
        # Show a subnet
        api_instance.get_subnets_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_subnets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **show_hidden_parameters** | **bool**| Display hidden parameter values | [optional] 

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

# **get_subnets_id_freeip**
> get_subnets_id_freeip(id, location_id=location_id, organization_id=organization_id, mac=mac, excluded_ips=excluded_ips)

Provides an unused IP address in this subnet

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
    api_instance = foreman.SubnetsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    mac = 'mac_example' # str | MAC address to reuse the IP for this host (optional)
    excluded_ips = ['excluded_ips_example'] # List[str] | IP addresses that should be excluded from suggestion (optional)

    try:
        # Provides an unused IP address in this subnet
        api_instance.get_subnets_id_freeip(id, location_id=location_id, organization_id=organization_id, mac=mac, excluded_ips=excluded_ips)
    except Exception as e:
        print("Exception when calling SubnetsApi->get_subnets_id_freeip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **mac** | **str**| MAC address to reuse the IP for this host | [optional] 
 **excluded_ips** | [**List[str]**](str.md)| IP addresses that should be excluded from suggestion | [optional] 

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

# **post_subnets**
> post_subnets(subnet_name, subnet_network, location_id=location_id, organization_id=organization_id, subnet_description=subnet_description, subnet_network_type=subnet_network_type, subnet_cidr=subnet_cidr, subnet_mask=subnet_mask, subnet_gateway=subnet_gateway, subnet_dns_primary=subnet_dns_primary, subnet_dns_secondary=subnet_dns_secondary, subnet_ipam=subnet_ipam, subnet_externalipam_group=subnet_externalipam_group, subnet_from=subnet_from, subnet_to=subnet_to, subnet_vlanid=subnet_vlanid, subnet_mtu=subnet_mtu, subnet_domain_ids=subnet_domain_ids, subnet_dhcp_id=subnet_dhcp_id, subnet_tftp_id=subnet_tftp_id, subnet_httpboot_id=subnet_httpboot_id, subnet_externalipam_id=subnet_externalipam_id, subnet_dns_id=subnet_dns_id, subnet_template_id=subnet_template_id, subnet_bmc_id=subnet_bmc_id, subnet_boot_mode=subnet_boot_mode, subnet_subnet_parameters_attributes=subnet_subnet_parameters_attributes, subnet_location_ids=subnet_location_ids, subnet_organization_ids=subnet_organization_ids, subnet_remote_execution_proxy_ids=subnet_remote_execution_proxy_ids)

Create a subnet

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
    api_instance = foreman.SubnetsApi(api_client)
    subnet_name = 'subnet_name_example' # str | Subnet name
    subnet_network = 'subnet_network_example' # str | Subnet network
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    subnet_description = 'subnet_description_example' # str | Subnet description (optional)
    subnet_network_type = 'subnet_network_type_example' # str | Type or protocol, IPv4 or IPv6, defaults to IPv4 (optional)
    subnet_cidr = 'subnet_cidr_example' # str | Network prefix in CIDR notation (optional)
    subnet_mask = 'subnet_mask_example' # str | Netmask for this subnet (optional)
    subnet_gateway = 'subnet_gateway_example' # str | Subnet gateway (optional)
    subnet_dns_primary = 'subnet_dns_primary_example' # str | Primary DNS for this subnet (optional)
    subnet_dns_secondary = 'subnet_dns_secondary_example' # str | Secondary DNS for this subnet (optional)
    subnet_ipam = 'subnet_ipam_example' # str | IP Address auto suggestion mode for this subnet. (optional)
    subnet_externalipam_group = 'subnet_externalipam_group_example' # str | External IPAM group - only relevant when IPAM is set to external (optional)
    subnet_from = 'subnet_from_example' # str | Starting IP Address for IP auto suggestion (optional)
    subnet_to = 'subnet_to_example' # str | Ending IP Address for IP auto suggestion (optional)
    subnet_vlanid = 'subnet_vlanid_example' # str | VLAN ID for this subnet (optional)
    subnet_mtu = 3.4 # float | MTU for this subnet (optional)
    subnet_domain_ids = ['subnet_domain_ids_example'] # List[str] | Domains in which this subnet is part (optional)
    subnet_dhcp_id = 3.4 # float | DHCP Proxy ID to use within this subnet (optional)
    subnet_tftp_id = 3.4 # float | TFTP Proxy ID to use within this subnet (optional)
    subnet_httpboot_id = 3.4 # float | HTTPBoot Proxy ID to use within this subnet (optional)
    subnet_externalipam_id = 3.4 # float | External IPAM Proxy ID to use within this subnet (optional)
    subnet_dns_id = 3.4 # float | DNS Proxy ID to use within this subnet (optional)
    subnet_template_id = 3.4 # float | Template HTTP(S) Proxy ID to use within this subnet (optional)
    subnet_bmc_id = 3.4 # float | BMC Proxy ID to use within this subnet (optional)
    subnet_boot_mode = 'subnet_boot_mode_example' # str | Default boot mode for interfaces assigned to this subnet. (optional)
    subnet_subnet_parameters_attributes = ['subnet_subnet_parameters_attributes_example'] # List[str] | Array of parameters (name, value) (optional)
    subnet_location_ids = ['subnet_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    subnet_organization_ids = ['subnet_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)
    subnet_remote_execution_proxy_ids = ['subnet_remote_execution_proxy_ids_example'] # List[str] | List of proxy IDs to be used for remote execution (optional)

    try:
        # Create a subnet
        api_instance.post_subnets(subnet_name, subnet_network, location_id=location_id, organization_id=organization_id, subnet_description=subnet_description, subnet_network_type=subnet_network_type, subnet_cidr=subnet_cidr, subnet_mask=subnet_mask, subnet_gateway=subnet_gateway, subnet_dns_primary=subnet_dns_primary, subnet_dns_secondary=subnet_dns_secondary, subnet_ipam=subnet_ipam, subnet_externalipam_group=subnet_externalipam_group, subnet_from=subnet_from, subnet_to=subnet_to, subnet_vlanid=subnet_vlanid, subnet_mtu=subnet_mtu, subnet_domain_ids=subnet_domain_ids, subnet_dhcp_id=subnet_dhcp_id, subnet_tftp_id=subnet_tftp_id, subnet_httpboot_id=subnet_httpboot_id, subnet_externalipam_id=subnet_externalipam_id, subnet_dns_id=subnet_dns_id, subnet_template_id=subnet_template_id, subnet_bmc_id=subnet_bmc_id, subnet_boot_mode=subnet_boot_mode, subnet_subnet_parameters_attributes=subnet_subnet_parameters_attributes, subnet_location_ids=subnet_location_ids, subnet_organization_ids=subnet_organization_ids, subnet_remote_execution_proxy_ids=subnet_remote_execution_proxy_ids)
    except Exception as e:
        print("Exception when calling SubnetsApi->post_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_name** | **str**| Subnet name | 
 **subnet_network** | **str**| Subnet network | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **subnet_description** | **str**| Subnet description | [optional] 
 **subnet_network_type** | **str**| Type or protocol, IPv4 or IPv6, defaults to IPv4 | [optional] 
 **subnet_cidr** | **str**| Network prefix in CIDR notation | [optional] 
 **subnet_mask** | **str**| Netmask for this subnet | [optional] 
 **subnet_gateway** | **str**| Subnet gateway | [optional] 
 **subnet_dns_primary** | **str**| Primary DNS for this subnet | [optional] 
 **subnet_dns_secondary** | **str**| Secondary DNS for this subnet | [optional] 
 **subnet_ipam** | **str**| IP Address auto suggestion mode for this subnet. | [optional] 
 **subnet_externalipam_group** | **str**| External IPAM group - only relevant when IPAM is set to external | [optional] 
 **subnet_from** | **str**| Starting IP Address for IP auto suggestion | [optional] 
 **subnet_to** | **str**| Ending IP Address for IP auto suggestion | [optional] 
 **subnet_vlanid** | **str**| VLAN ID for this subnet | [optional] 
 **subnet_mtu** | **float**| MTU for this subnet | [optional] 
 **subnet_domain_ids** | [**List[str]**](str.md)| Domains in which this subnet is part | [optional] 
 **subnet_dhcp_id** | **float**| DHCP Proxy ID to use within this subnet | [optional] 
 **subnet_tftp_id** | **float**| TFTP Proxy ID to use within this subnet | [optional] 
 **subnet_httpboot_id** | **float**| HTTPBoot Proxy ID to use within this subnet | [optional] 
 **subnet_externalipam_id** | **float**| External IPAM Proxy ID to use within this subnet | [optional] 
 **subnet_dns_id** | **float**| DNS Proxy ID to use within this subnet | [optional] 
 **subnet_template_id** | **float**| Template HTTP(S) Proxy ID to use within this subnet | [optional] 
 **subnet_bmc_id** | **float**| BMC Proxy ID to use within this subnet | [optional] 
 **subnet_boot_mode** | **str**| Default boot mode for interfaces assigned to this subnet. | [optional] 
 **subnet_subnet_parameters_attributes** | [**List[str]**](str.md)| Array of parameters (name, value) | [optional] 
 **subnet_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **subnet_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 
 **subnet_remote_execution_proxy_ids** | [**List[str]**](str.md)| List of proxy IDs to be used for remote execution | [optional] 

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

# **put_subnets_id**
> put_subnets_id(id, location_id=location_id, organization_id=organization_id, subnet_name=subnet_name, subnet_description=subnet_description, subnet_network_type=subnet_network_type, subnet_network=subnet_network, subnet_cidr=subnet_cidr, subnet_mask=subnet_mask, subnet_gateway=subnet_gateway, subnet_dns_primary=subnet_dns_primary, subnet_dns_secondary=subnet_dns_secondary, subnet_ipam=subnet_ipam, subnet_externalipam_group=subnet_externalipam_group, subnet_from=subnet_from, subnet_to=subnet_to, subnet_vlanid=subnet_vlanid, subnet_mtu=subnet_mtu, subnet_domain_ids=subnet_domain_ids, subnet_dhcp_id=subnet_dhcp_id, subnet_tftp_id=subnet_tftp_id, subnet_httpboot_id=subnet_httpboot_id, subnet_externalipam_id=subnet_externalipam_id, subnet_dns_id=subnet_dns_id, subnet_template_id=subnet_template_id, subnet_bmc_id=subnet_bmc_id, subnet_boot_mode=subnet_boot_mode, subnet_subnet_parameters_attributes=subnet_subnet_parameters_attributes, subnet_location_ids=subnet_location_ids, subnet_organization_ids=subnet_organization_ids, subnet_remote_execution_proxy_ids=subnet_remote_execution_proxy_ids)

Update a subnet

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
    api_instance = foreman.SubnetsApi(api_client)
    id = 3.4 # float | Subnet numeric identifier
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    subnet_name = 'subnet_name_example' # str | Subnet name (optional)
    subnet_description = 'subnet_description_example' # str | Subnet description (optional)
    subnet_network_type = 'subnet_network_type_example' # str | Type or protocol, IPv4 or IPv6, defaults to IPv4 (optional)
    subnet_network = 'subnet_network_example' # str | Subnet network (optional)
    subnet_cidr = 'subnet_cidr_example' # str | Network prefix in CIDR notation (optional)
    subnet_mask = 'subnet_mask_example' # str | Netmask for this subnet (optional)
    subnet_gateway = 'subnet_gateway_example' # str | Subnet gateway (optional)
    subnet_dns_primary = 'subnet_dns_primary_example' # str | Primary DNS for this subnet (optional)
    subnet_dns_secondary = 'subnet_dns_secondary_example' # str | Secondary DNS for this subnet (optional)
    subnet_ipam = 'subnet_ipam_example' # str | IP Address auto suggestion mode for this subnet. (optional)
    subnet_externalipam_group = 'subnet_externalipam_group_example' # str | External IPAM group - only relevant when IPAM is set to external (optional)
    subnet_from = 'subnet_from_example' # str | Starting IP Address for IP auto suggestion (optional)
    subnet_to = 'subnet_to_example' # str | Ending IP Address for IP auto suggestion (optional)
    subnet_vlanid = 'subnet_vlanid_example' # str | VLAN ID for this subnet (optional)
    subnet_mtu = 3.4 # float | MTU for this subnet (optional)
    subnet_domain_ids = ['subnet_domain_ids_example'] # List[str] | Domains in which this subnet is part (optional)
    subnet_dhcp_id = 3.4 # float | DHCP Proxy ID to use within this subnet (optional)
    subnet_tftp_id = 3.4 # float | TFTP Proxy ID to use within this subnet (optional)
    subnet_httpboot_id = 3.4 # float | HTTPBoot Proxy ID to use within this subnet (optional)
    subnet_externalipam_id = 3.4 # float | External IPAM Proxy ID to use within this subnet (optional)
    subnet_dns_id = 3.4 # float | DNS Proxy ID to use within this subnet (optional)
    subnet_template_id = 3.4 # float | Template HTTP(S) Proxy ID to use within this subnet (optional)
    subnet_bmc_id = 3.4 # float | BMC Proxy ID to use within this subnet (optional)
    subnet_boot_mode = 'subnet_boot_mode_example' # str | Default boot mode for interfaces assigned to this subnet. (optional)
    subnet_subnet_parameters_attributes = ['subnet_subnet_parameters_attributes_example'] # List[str] | Array of parameters (name, value) (optional)
    subnet_location_ids = ['subnet_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    subnet_organization_ids = ['subnet_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)
    subnet_remote_execution_proxy_ids = ['subnet_remote_execution_proxy_ids_example'] # List[str] | List of proxy IDs to be used for remote execution (optional)

    try:
        # Update a subnet
        api_instance.put_subnets_id(id, location_id=location_id, organization_id=organization_id, subnet_name=subnet_name, subnet_description=subnet_description, subnet_network_type=subnet_network_type, subnet_network=subnet_network, subnet_cidr=subnet_cidr, subnet_mask=subnet_mask, subnet_gateway=subnet_gateway, subnet_dns_primary=subnet_dns_primary, subnet_dns_secondary=subnet_dns_secondary, subnet_ipam=subnet_ipam, subnet_externalipam_group=subnet_externalipam_group, subnet_from=subnet_from, subnet_to=subnet_to, subnet_vlanid=subnet_vlanid, subnet_mtu=subnet_mtu, subnet_domain_ids=subnet_domain_ids, subnet_dhcp_id=subnet_dhcp_id, subnet_tftp_id=subnet_tftp_id, subnet_httpboot_id=subnet_httpboot_id, subnet_externalipam_id=subnet_externalipam_id, subnet_dns_id=subnet_dns_id, subnet_template_id=subnet_template_id, subnet_bmc_id=subnet_bmc_id, subnet_boot_mode=subnet_boot_mode, subnet_subnet_parameters_attributes=subnet_subnet_parameters_attributes, subnet_location_ids=subnet_location_ids, subnet_organization_ids=subnet_organization_ids, subnet_remote_execution_proxy_ids=subnet_remote_execution_proxy_ids)
    except Exception as e:
        print("Exception when calling SubnetsApi->put_subnets_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Subnet numeric identifier | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **subnet_name** | **str**| Subnet name | [optional] 
 **subnet_description** | **str**| Subnet description | [optional] 
 **subnet_network_type** | **str**| Type or protocol, IPv4 or IPv6, defaults to IPv4 | [optional] 
 **subnet_network** | **str**| Subnet network | [optional] 
 **subnet_cidr** | **str**| Network prefix in CIDR notation | [optional] 
 **subnet_mask** | **str**| Netmask for this subnet | [optional] 
 **subnet_gateway** | **str**| Subnet gateway | [optional] 
 **subnet_dns_primary** | **str**| Primary DNS for this subnet | [optional] 
 **subnet_dns_secondary** | **str**| Secondary DNS for this subnet | [optional] 
 **subnet_ipam** | **str**| IP Address auto suggestion mode for this subnet. | [optional] 
 **subnet_externalipam_group** | **str**| External IPAM group - only relevant when IPAM is set to external | [optional] 
 **subnet_from** | **str**| Starting IP Address for IP auto suggestion | [optional] 
 **subnet_to** | **str**| Ending IP Address for IP auto suggestion | [optional] 
 **subnet_vlanid** | **str**| VLAN ID for this subnet | [optional] 
 **subnet_mtu** | **float**| MTU for this subnet | [optional] 
 **subnet_domain_ids** | [**List[str]**](str.md)| Domains in which this subnet is part | [optional] 
 **subnet_dhcp_id** | **float**| DHCP Proxy ID to use within this subnet | [optional] 
 **subnet_tftp_id** | **float**| TFTP Proxy ID to use within this subnet | [optional] 
 **subnet_httpboot_id** | **float**| HTTPBoot Proxy ID to use within this subnet | [optional] 
 **subnet_externalipam_id** | **float**| External IPAM Proxy ID to use within this subnet | [optional] 
 **subnet_dns_id** | **float**| DNS Proxy ID to use within this subnet | [optional] 
 **subnet_template_id** | **float**| Template HTTP(S) Proxy ID to use within this subnet | [optional] 
 **subnet_bmc_id** | **float**| BMC Proxy ID to use within this subnet | [optional] 
 **subnet_boot_mode** | **str**| Default boot mode for interfaces assigned to this subnet. | [optional] 
 **subnet_subnet_parameters_attributes** | [**List[str]**](str.md)| Array of parameters (name, value) | [optional] 
 **subnet_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **subnet_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 
 **subnet_remote_execution_proxy_ids** | [**List[str]**](str.md)| List of proxy IDs to be used for remote execution | [optional] 

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

