# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "foreman-python-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=2017.4.17", "python-dateutil>=2.1", "six>=1.10", "urllib3>=1.23"]


setup(
    name=NAME,
    version=VERSION,
    description="Foreman (params in:formData)",
    author_email="",
    url="",
    keywords=["Swagger", "Foreman (params in:formData)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
     &lt;p&gt;Foreman API v2 is currently the default API version.&lt;/p&gt;   # noqa: E501
    """,
)
