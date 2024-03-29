# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyforeman
from pyforeman.api.host_tracer_api import HostTracerApi  # noqa: E501
from pyforeman.rest import ApiException


class TestHostTracerApi(unittest.TestCase):
    """HostTracerApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.host_tracer_api.HostTracerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_hosts_host_id_traces(self):
        """Test case for get_hosts_host_id_traces

        List services that need restarting on the host  # noqa: E501
        """
        pass

    def test_put_hosts_host_id_traces_resolve(self):
        """Test case for put_hosts_host_id_traces_resolve

        Resolve traces  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
