# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.host_tracer_api import HostTracerApi


class TestHostTracerApi(unittest.TestCase):
    """HostTracerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HostTracerApi()

    def tearDown(self) -> None:
        pass

    def test_get_hosts_host_id_traces(self) -> None:
        """Test case for get_hosts_host_id_traces

        List services that need restarting on the host
        """
        pass

    def test_put_hosts_host_id_traces_resolve(self) -> None:
        """Test case for put_hosts_host_id_traces_resolve

        Resolve traces
        """
        pass


if __name__ == "__main__":
    unittest.main()
