# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class SpuAttributes1212(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'breakfast': 'SpuAttributes1212Breakfast',
        'extra_bed': 'SpuAttributes1212Response',
        'extra': 'str'
    }

    attribute_map = {
        'breakfast': 'breakfast',
        'extra_bed': 'extra_bed',
        'extra': 'extra'
    }

    def __init__(self, breakfast=None, extra_bed=None, extra=None):  # noqa: E501
        """SpuAttributes1212 - a model defined in Swagger"""  # noqa: E501
        self._breakfast = None
        self._extra_bed = None
        self._extra = None
        self.discriminator = None
        self.breakfast = breakfast
        self.extra_bed = extra_bed
        if extra is not None:
            self.extra = extra

    @property
    def breakfast(self):
        """Gets the breakfast of this SpuAttributes1212.  # noqa: E501


        :return: The breakfast of this SpuAttributes1212.  # noqa: E501
        :rtype: SpuAttributes1212Breakfast
        """
        return self._breakfast

    @breakfast.setter
    def breakfast(self, breakfast):
        """Sets the breakfast of this SpuAttributes1212.


        :param breakfast: The breakfast of this SpuAttributes1212.  # noqa: E501
        :type: SpuAttributes1212Breakfast
        """
        if breakfast is None:
            raise ValueError("Invalid value for `breakfast`, must not be `None`")  # noqa: E501

        self._breakfast = breakfast

    @property
    def extra_bed(self):
        """Gets the extra_bed of this SpuAttributes1212.  # noqa: E501


        :return: The extra_bed of this SpuAttributes1212.  # noqa: E501
        :rtype: SpuAttributes1212Response
        """
        return self._extra_bed

    @extra_bed.setter
    def extra_bed(self, extra_bed):
        """Sets the extra_bed of this SpuAttributes1212.


        :param extra_bed: The extra_bed of this SpuAttributes1212.  # noqa: E501
        :type: SpuAttributes1212Response
        """
        if extra_bed is None:
            raise ValueError("Invalid value for `extra_bed`, must not be `None`")  # noqa: E501

        self._extra_bed = extra_bed

    @property
    def extra(self):
        """Gets the extra of this SpuAttributes1212.  # noqa: E501

        费用政策自定义内容  # noqa: E501

        :return: The extra of this SpuAttributes1212.  # noqa: E501
        :rtype: str
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this SpuAttributes1212.

        费用政策自定义内容  # noqa: E501

        :param extra: The extra of this SpuAttributes1212.  # noqa: E501
        :type: str
        """

        self._extra = extra

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SpuAttributes1212, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpuAttributes1212):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other