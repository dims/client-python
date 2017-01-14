# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DeleteOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, grace_period_seconds=None, kind=None, orphan_dependents=None, preconditions=None):
        """
        V1DeleteOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'grace_period_seconds': 'int',
            'kind': 'str',
            'orphan_dependents': 'bool',
            'preconditions': 'V1Preconditions'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'grace_period_seconds': 'gracePeriodSeconds',
            'kind': 'kind',
            'orphan_dependents': 'orphanDependents',
            'preconditions': 'preconditions'
        }

        self._api_version = api_version
        self._grace_period_seconds = grace_period_seconds
        self._kind = kind
        self._orphan_dependents = orphan_dependents
        self._preconditions = preconditions

    @property
    def api_version(self):
        """
        Gets the api_version of this V1DeleteOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1DeleteOptions.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1DeleteOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1DeleteOptions.
        :type: str
        """

        self._api_version = api_version

    @property
    def grace_period_seconds(self):
        """
        Gets the grace_period_seconds of this V1DeleteOptions.
        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.

        :return: The grace_period_seconds of this V1DeleteOptions.
        :rtype: int
        """
        return self._grace_period_seconds

    @grace_period_seconds.setter
    def grace_period_seconds(self, grace_period_seconds):
        """
        Sets the grace_period_seconds of this V1DeleteOptions.
        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.

        :param grace_period_seconds: The grace_period_seconds of this V1DeleteOptions.
        :type: int
        """

        self._grace_period_seconds = grace_period_seconds

    @property
    def kind(self):
        """
        Gets the kind of this V1DeleteOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1DeleteOptions.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1DeleteOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1DeleteOptions.
        :type: str
        """

        self._kind = kind

    @property
    def orphan_dependents(self):
        """
        Gets the orphan_dependents of this V1DeleteOptions.
        Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list.

        :return: The orphan_dependents of this V1DeleteOptions.
        :rtype: bool
        """
        return self._orphan_dependents

    @orphan_dependents.setter
    def orphan_dependents(self, orphan_dependents):
        """
        Sets the orphan_dependents of this V1DeleteOptions.
        Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list.

        :param orphan_dependents: The orphan_dependents of this V1DeleteOptions.
        :type: bool
        """

        self._orphan_dependents = orphan_dependents

    @property
    def preconditions(self):
        """
        Gets the preconditions of this V1DeleteOptions.
        Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.

        :return: The preconditions of this V1DeleteOptions.
        :rtype: V1Preconditions
        """
        return self._preconditions

    @preconditions.setter
    def preconditions(self, preconditions):
        """
        Sets the preconditions of this V1DeleteOptions.
        Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.

        :param preconditions: The preconditions of this V1DeleteOptions.
        :type: V1Preconditions
        """

        self._preconditions = preconditions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
