# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.dashboard_api import DashboardApi


class TestDashboardApi(unittest.TestCase):
    """DashboardApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardApi()

    def tearDown(self) -> None:
        pass

    def test_get_dashboard(self) -> None:
        """Test case for get_dashboard

        Get dashboard details
        """
        pass


if __name__ == "__main__":
    unittest.main()