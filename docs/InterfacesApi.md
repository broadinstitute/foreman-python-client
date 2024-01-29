# pyforeman.InterfacesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hosts_host_id_interfaces_id**](InterfacesApi.md#delete_hosts_host_id_interfaces_id) | **DELETE** /hosts/{host_id}/interfaces/{id} | Delete a host&#39;s interface
[**get_domains_domain_id_interfaces**](InterfacesApi.md#get_domains_domain_id_interfaces) | **GET** /domains/{domain_id}/interfaces | List all interfaces for domain
[**get_hosts_host_id_interfaces**](InterfacesApi.md#get_hosts_host_id_interfaces) | **GET** /hosts/{host_id}/interfaces | List all interfaces for host
[**get_hosts_host_id_interfaces_id**](InterfacesApi.md#get_hosts_host_id_interfaces_id) | **GET** /hosts/{host_id}/interfaces/{id} | Show an interface for host
[**get_subnets_subnet_id_interfaces**](InterfacesApi.md#get_subnets_subnet_id_interfaces) | **GET** /subnets/{subnet_id}/interfaces | List all interfaces for subnet
[**post_hosts_host_id_interfaces**](InterfacesApi.md#post_hosts_host_id_interfaces) | **POST** /hosts/{host_id}/interfaces | Create an interface on a host
[**put_hosts_host_id_interfaces_id**](InterfacesApi.md#put_hosts_host_id_interfaces_id) | **PUT** /hosts/{host_id}/interfaces/{id} | Update a host&#39;s interface


# **delete_hosts_host_id_interfaces_id**
> delete_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id)

Delete a host's interface



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
host_id = 'host_id_example' # str | ID or name of host
id = 'id_example' # str | ID of interface
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a host's interface
    api_instance.delete_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling InterfacesApi->delete_hosts_host_id_interfaces_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| ID or name of host |
 **id** | **str**| ID of interface |
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

# **get_domains_domain_id_interfaces**
> get_domains_domain_id_interfaces(domain_id, host_id, subnet_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)

List all interfaces for domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
domain_id = 'domain_id_example' # str | ID or name of domain
host_id = 'host_id_example' # str | ID or name of host
subnet_id = 'subnet_id_example' # str | ID or name of subnet
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all interfaces for domain
    api_instance.get_domains_domain_id_interfaces(domain_id, host_id, subnet_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_domains_domain_id_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| ID or name of domain |
 **host_id** | **str**| ID or name of host |
 **subnet_id** | **str**| ID or name of subnet |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
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

# **get_hosts_host_id_interfaces**
> get_hosts_host_id_interfaces(host_id, domain_id, subnet_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)

List all interfaces for host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
host_id = 'host_id_example' # str | ID or name of host
domain_id = 'domain_id_example' # str | ID or name of domain
subnet_id = 'subnet_id_example' # str | ID or name of subnet
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all interfaces for host
    api_instance.get_hosts_host_id_interfaces(host_id, domain_id, subnet_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_hosts_host_id_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| ID or name of host |
 **domain_id** | **str**| ID or name of domain |
 **subnet_id** | **str**| ID or name of subnet |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
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

# **get_hosts_host_id_interfaces_id**
> get_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id)

Show an interface for host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
host_id = 'host_id_example' # str | ID or name of host
id = 'id_example' # str | ID or name of interface
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an interface for host
    api_instance.get_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_hosts_host_id_interfaces_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| ID or name of host |
 **id** | **str**| ID or name of interface |
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

# **get_subnets_subnet_id_interfaces**
> get_subnets_subnet_id_interfaces(subnet_id, host_id, domain_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)

List all interfaces for subnet



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
subnet_id = 'subnet_id_example' # str | ID or name of subnet
host_id = 'host_id_example' # str | ID or name of host
domain_id = 'domain_id_example' # str | ID or name of domain
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all interfaces for subnet
    api_instance.get_subnets_subnet_id_interfaces(subnet_id, host_id, domain_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_subnets_subnet_id_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**| ID or name of subnet |
 **host_id** | **str**| ID or name of host |
 **domain_id** | **str**| ID or name of domain |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
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

# **post_hosts_host_id_interfaces**
> post_hosts_host_id_interfaces(host_id, location_id=location_id, organization_id=organization_id, interface_mac=interface_mac, interface_ip=interface_ip, interface_ip6=interface_ip6, interface_type=interface_type, interface_name=interface_name, interface_subnet_id=interface_subnet_id, interface_subnet6_id=interface_subnet6_id, interface_domain_id=interface_domain_id, interface_identifier=interface_identifier, interface_managed=interface_managed, interface_primary=interface_primary, interface_provision=interface_provision, interface_username=interface_username, interface_password=interface_password, interface_provider=interface_provider, interface_virtual=interface_virtual, interface_tag=interface_tag, interface_mtu=interface_mtu, interface_attached_to=interface_attached_to, interface_mode=interface_mode, interface_attached_devices=interface_attached_devices, interface_bond_options=interface_bond_options, interface_execution=interface_execution)

Create an interface on a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
host_id = 'host_id_example' # str | ID or name of host
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
interface_mac = 'interface_mac_example' # str | MAC address of interface. Required for managed interfaces on bare metal. (optional)
interface_ip = 'interface_ip_example' # str | IPv4 address of interface (optional)
interface_ip6 = 'interface_ip6_example' # str | IPv6 address of interface (optional)
interface_type = 'interface_type_example' # str | Interface type, e.g. bmc. Default is interface (optional)
interface_name = 'interface_name_example' # str | Interface's DNS name (optional)
interface_subnet_id = 8.14 # float | Foreman subnet ID of IPv4 interface (optional)
interface_subnet6_id = 8.14 # float | Foreman subnet ID of IPv6 interface (optional)
interface_domain_id = 8.14 # float | Foreman domain ID of interface. Required for primary interfaces on managed hosts. (optional)
interface_identifier = 'interface_identifier_example' # str | Device identifier, e.g. eth0 or eth1.1 (optional)
interface_managed = true # bool | Should this interface be managed via DHCP and DNS smart proxy and should it be configured during provisioning? (optional)
interface_primary = true # bool | Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface. (optional)
interface_provision = true # bool | Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface. (optional)
interface_username = 'interface_username_example' # str | Only for BMC interfaces. (optional)
interface_password = 'interface_password_example' # str | Only for BMC interfaces. (optional)
interface_provider = 'interface_provider_example' # str | Interface provider, e.g. IPMI. Only for BMC interfaces. (optional)
interface_virtual = true # bool | Alias or VLAN device (optional)
interface_tag = 'interface_tag_example' # str | VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. (optional)
interface_mtu = 8.14 # float | MTU, this attribute has precedence over the subnet MTU. (optional)
interface_attached_to = 'interface_attached_to_example' # str | Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces. (optional)
interface_mode = 'interface_mode_example' # str | Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. (optional)
interface_attached_devices = ['interface_attached_devices_example'] # list[str] | Identifiers of attached interfaces, e.g. `['eth1', 'eth2']`. For bond interfaces those are the slaves. Only for bond and bridges interfaces. (optional)
interface_bond_options = 'interface_bond_options_example' # str | Space separated options, e.g. miimon=100. Only for bond interfaces. (optional)
interface_execution = true # bool | Should this interface be used for remote execution? (optional)

try:
    # Create an interface on a host
    api_instance.post_hosts_host_id_interfaces(host_id, location_id=location_id, organization_id=organization_id, interface_mac=interface_mac, interface_ip=interface_ip, interface_ip6=interface_ip6, interface_type=interface_type, interface_name=interface_name, interface_subnet_id=interface_subnet_id, interface_subnet6_id=interface_subnet6_id, interface_domain_id=interface_domain_id, interface_identifier=interface_identifier, interface_managed=interface_managed, interface_primary=interface_primary, interface_provision=interface_provision, interface_username=interface_username, interface_password=interface_password, interface_provider=interface_provider, interface_virtual=interface_virtual, interface_tag=interface_tag, interface_mtu=interface_mtu, interface_attached_to=interface_attached_to, interface_mode=interface_mode, interface_attached_devices=interface_attached_devices, interface_bond_options=interface_bond_options, interface_execution=interface_execution)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_hosts_host_id_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| ID or name of host |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **interface_mac** | **str**| MAC address of interface. Required for managed interfaces on bare metal. | [optional]
 **interface_ip** | **str**| IPv4 address of interface | [optional]
 **interface_ip6** | **str**| IPv6 address of interface | [optional]
 **interface_type** | **str**| Interface type, e.g. bmc. Default is interface | [optional]
 **interface_name** | **str**| Interface&#39;s DNS name | [optional]
 **interface_subnet_id** | **float**| Foreman subnet ID of IPv4 interface | [optional]
 **interface_subnet6_id** | **float**| Foreman subnet ID of IPv6 interface | [optional]
 **interface_domain_id** | **float**| Foreman domain ID of interface. Required for primary interfaces on managed hosts. | [optional]
 **interface_identifier** | **str**| Device identifier, e.g. eth0 or eth1.1 | [optional]
 **interface_managed** | **bool**| Should this interface be managed via DHCP and DNS smart proxy and should it be configured during provisioning? | [optional]
 **interface_primary** | **bool**| Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface. | [optional]
 **interface_provision** | **bool**| Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface. | [optional]
 **interface_username** | **str**| Only for BMC interfaces. | [optional]
 **interface_password** | **str**| Only for BMC interfaces. | [optional]
 **interface_provider** | **str**| Interface provider, e.g. IPMI. Only for BMC interfaces. | [optional]
 **interface_virtual** | **bool**| Alias or VLAN device | [optional]
 **interface_tag** | **str**| VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. | [optional]
 **interface_mtu** | **float**| MTU, this attribute has precedence over the subnet MTU. | [optional]
 **interface_attached_to** | **str**| Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces. | [optional]
 **interface_mode** | **str**| Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. | [optional]
 **interface_attached_devices** | [**list[str]**](str.md)| Identifiers of attached interfaces, e.g. &#x60;[&#39;eth1&#39;, &#39;eth2&#39;]&#x60;. For bond interfaces those are the slaves. Only for bond and bridges interfaces. | [optional]
 **interface_bond_options** | **str**| Space separated options, e.g. miimon&#x3D;100. Only for bond interfaces. | [optional]
 **interface_execution** | **bool**| Should this interface be used for remote execution? | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_host_id_interfaces_id**
> put_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id, interface_mac=interface_mac, interface_ip=interface_ip, interface_ip6=interface_ip6, interface_type=interface_type, interface_name=interface_name, interface_subnet_id=interface_subnet_id, interface_subnet6_id=interface_subnet6_id, interface_domain_id=interface_domain_id, interface_identifier=interface_identifier, interface_managed=interface_managed, interface_primary=interface_primary, interface_provision=interface_provision, interface_username=interface_username, interface_password=interface_password, interface_provider=interface_provider, interface_virtual=interface_virtual, interface_tag=interface_tag, interface_mtu=interface_mtu, interface_attached_to=interface_attached_to, interface_mode=interface_mode, interface_attached_devices=interface_attached_devices, interface_bond_options=interface_bond_options, interface_execution=interface_execution)

Update a host's interface



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InterfacesApi()
host_id = 'host_id_example' # str | ID or name of host
id = 'id_example' # str | ID of interface
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
interface_mac = 'interface_mac_example' # str | MAC address of interface. Required for managed interfaces on bare metal. (optional)
interface_ip = 'interface_ip_example' # str | IPv4 address of interface (optional)
interface_ip6 = 'interface_ip6_example' # str | IPv6 address of interface (optional)
interface_type = 'interface_type_example' # str | Interface type, e.g. bmc. Default is interface (optional)
interface_name = 'interface_name_example' # str | Interface's DNS name (optional)
interface_subnet_id = 8.14 # float | Foreman subnet ID of IPv4 interface (optional)
interface_subnet6_id = 8.14 # float | Foreman subnet ID of IPv6 interface (optional)
interface_domain_id = 8.14 # float | Foreman domain ID of interface. Required for primary interfaces on managed hosts. (optional)
interface_identifier = 'interface_identifier_example' # str | Device identifier, e.g. eth0 or eth1.1 (optional)
interface_managed = true # bool | Should this interface be managed via DHCP and DNS smart proxy and should it be configured during provisioning? (optional)
interface_primary = true # bool | Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface. (optional)
interface_provision = true # bool | Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface. (optional)
interface_username = 'interface_username_example' # str | Only for BMC interfaces. (optional)
interface_password = 'interface_password_example' # str | Only for BMC interfaces. (optional)
interface_provider = 'interface_provider_example' # str | Interface provider, e.g. IPMI. Only for BMC interfaces. (optional)
interface_virtual = true # bool | Alias or VLAN device (optional)
interface_tag = 'interface_tag_example' # str | VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. (optional)
interface_mtu = 8.14 # float | MTU, this attribute has precedence over the subnet MTU. (optional)
interface_attached_to = 'interface_attached_to_example' # str | Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces. (optional)
interface_mode = 'interface_mode_example' # str | Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. (optional)
interface_attached_devices = ['interface_attached_devices_example'] # list[str] | Identifiers of attached interfaces, e.g. `['eth1', 'eth2']`. For bond interfaces those are the slaves. Only for bond and bridges interfaces. (optional)
interface_bond_options = 'interface_bond_options_example' # str | Space separated options, e.g. miimon=100. Only for bond interfaces. (optional)
interface_execution = true # bool | Should this interface be used for remote execution? (optional)

try:
    # Update a host's interface
    api_instance.put_hosts_host_id_interfaces_id(host_id, id, location_id=location_id, organization_id=organization_id, interface_mac=interface_mac, interface_ip=interface_ip, interface_ip6=interface_ip6, interface_type=interface_type, interface_name=interface_name, interface_subnet_id=interface_subnet_id, interface_subnet6_id=interface_subnet6_id, interface_domain_id=interface_domain_id, interface_identifier=interface_identifier, interface_managed=interface_managed, interface_primary=interface_primary, interface_provision=interface_provision, interface_username=interface_username, interface_password=interface_password, interface_provider=interface_provider, interface_virtual=interface_virtual, interface_tag=interface_tag, interface_mtu=interface_mtu, interface_attached_to=interface_attached_to, interface_mode=interface_mode, interface_attached_devices=interface_attached_devices, interface_bond_options=interface_bond_options, interface_execution=interface_execution)
except ApiException as e:
    print("Exception when calling InterfacesApi->put_hosts_host_id_interfaces_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| ID or name of host |
 **id** | **str**| ID of interface |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **interface_mac** | **str**| MAC address of interface. Required for managed interfaces on bare metal. | [optional]
 **interface_ip** | **str**| IPv4 address of interface | [optional]
 **interface_ip6** | **str**| IPv6 address of interface | [optional]
 **interface_type** | **str**| Interface type, e.g. bmc. Default is interface | [optional]
 **interface_name** | **str**| Interface&#39;s DNS name | [optional]
 **interface_subnet_id** | **float**| Foreman subnet ID of IPv4 interface | [optional]
 **interface_subnet6_id** | **float**| Foreman subnet ID of IPv6 interface | [optional]
 **interface_domain_id** | **float**| Foreman domain ID of interface. Required for primary interfaces on managed hosts. | [optional]
 **interface_identifier** | **str**| Device identifier, e.g. eth0 or eth1.1 | [optional]
 **interface_managed** | **bool**| Should this interface be managed via DHCP and DNS smart proxy and should it be configured during provisioning? | [optional]
 **interface_primary** | **bool**| Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface. | [optional]
 **interface_provision** | **bool**| Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface. | [optional]
 **interface_username** | **str**| Only for BMC interfaces. | [optional]
 **interface_password** | **str**| Only for BMC interfaces. | [optional]
 **interface_provider** | **str**| Interface provider, e.g. IPMI. Only for BMC interfaces. | [optional]
 **interface_virtual** | **bool**| Alias or VLAN device | [optional]
 **interface_tag** | **str**| VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. | [optional]
 **interface_mtu** | **float**| MTU, this attribute has precedence over the subnet MTU. | [optional]
 **interface_attached_to** | **str**| Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces. | [optional]
 **interface_mode** | **str**| Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. | [optional]
 **interface_attached_devices** | [**list[str]**](str.md)| Identifiers of attached interfaces, e.g. &#x60;[&#39;eth1&#39;, &#39;eth2&#39;]&#x60;. For bond interfaces those are the slaves. Only for bond and bridges interfaces. | [optional]
 **interface_bond_options** | **str**| Space separated options, e.g. miimon&#x3D;100. Only for bond interfaces. | [optional]
 **interface_execution** | **bool**| Should this interface be used for remote execution? | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
