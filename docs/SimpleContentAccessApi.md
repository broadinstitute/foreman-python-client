# pyforeman.SimpleContentAccessApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organizations_organization_id_simple_content_access_eligible**](SimpleContentAccessApi.md#get_organizations_organization_id_simple_content_access_eligible) | **GET** /organizations/{organization_id}/simple_content_access/eligible | Check if the specified organization is eligible for Simple Content Access. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
[**get_organizations_organization_id_simple_content_access_status**](SimpleContentAccessApi.md#get_organizations_organization_id_simple_content_access_status) | **GET** /organizations/{organization_id}/simple_content_access/status | Check if the specified organization has Simple Content Access enabled. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
[**put_organizations_organization_id_simple_content_access_disable**](SimpleContentAccessApi.md#put_organizations_organization_id_simple_content_access_disable) | **PUT** /organizations/{organization_id}/simple_content_access/disable | Disable simple content access for a manifest. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
[**put_organizations_organization_id_simple_content_access_enable**](SimpleContentAccessApi.md#put_organizations_organization_id_simple_content_access_enable) | **PUT** /organizations/{organization_id}/simple_content_access/enable | Enable simple content access for a manifest


# **get_organizations_organization_id_simple_content_access_eligible**
> get_organizations_organization_id_simple_content_access_eligible(organization_id)

Check if the specified organization is eligible for Simple Content Access. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SimpleContentAccessApi()
organization_id = 8.14 # float |

try:
    # Check if the specified organization is eligible for Simple Content Access. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
    api_instance.get_organizations_organization_id_simple_content_access_eligible(organization_id)
except ApiException as e:
    print("Exception when calling SimpleContentAccessApi->get_organizations_organization_id_simple_content_access_eligible: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_simple_content_access_status**
> get_organizations_organization_id_simple_content_access_status(organization_id)

Check if the specified organization has Simple Content Access enabled. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SimpleContentAccessApi()
organization_id = 8.14 # float | Organization ID

try:
    # Check if the specified organization has Simple Content Access enabled. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
    api_instance.get_organizations_organization_id_simple_content_access_status(organization_id)
except ApiException as e:
    print("Exception when calling SimpleContentAccessApi->get_organizations_organization_id_simple_content_access_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_organization_id_simple_content_access_disable**
> put_organizations_organization_id_simple_content_access_disable(organization_id)

Disable simple content access for a manifest. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SimpleContentAccessApi()
organization_id = 8.14 # float | Organization ID

try:
    # Disable simple content access for a manifest. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
    api_instance.put_organizations_organization_id_simple_content_access_disable(organization_id)
except ApiException as e:
    print("Exception when calling SimpleContentAccessApi->put_organizations_organization_id_simple_content_access_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_organization_id_simple_content_access_enable**
> put_organizations_organization_id_simple_content_access_enable(organization_id)

Enable simple content access for a manifest



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SimpleContentAccessApi()
organization_id = 8.14 # float | Organization ID

try:
    # Enable simple content access for a manifest
    api_instance.put_organizations_organization_id_simple_content_access_enable(organization_id)
except ApiException as e:
    print("Exception when calling SimpleContentAccessApi->put_organizations_organization_id_simple_content_access_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
