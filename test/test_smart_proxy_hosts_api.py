# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.smart_proxy_hosts_api import SmartProxyHostsApi


class TestSmartProxyHostsApi(unittest.TestCase):
    """SmartProxyHostsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SmartProxyHostsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_smart_proxies_smart_proxy_id_hosts_host_id(self) -> None:
        """Test case for delete_smart_proxies_smart_proxy_id_hosts_host_id

        Unassign a given host from the smart proxy
        """
        pass

    def test_get_smart_proxies_smart_proxy_id_hosts(self) -> None:
        """Test case for get_smart_proxies_smart_proxy_id_hosts

        Get hosts forming the smart proxy
        """
        pass

    def test_put_smart_proxies_smart_proxy_id_hosts_host_id(self) -> None:
        """Test case for put_smart_proxies_smart_proxy_id_hosts_host_id

        Assign a host to the smart proxy
        """
        pass


if __name__ == "__main__":
    unittest.main()