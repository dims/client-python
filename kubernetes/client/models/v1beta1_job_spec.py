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


class V1beta1JobSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active_deadline_seconds=None, auto_selector=None, completions=None, parallelism=None, selector=None, template=None):
        """
        V1beta1JobSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_deadline_seconds': 'int',
            'auto_selector': 'bool',
            'completions': 'int',
            'parallelism': 'int',
            'selector': 'UnversionedLabelSelector',
            'template': 'V1PodTemplateSpec'
        }

        self.attribute_map = {
            'active_deadline_seconds': 'activeDeadlineSeconds',
            'auto_selector': 'autoSelector',
            'completions': 'completions',
            'parallelism': 'parallelism',
            'selector': 'selector',
            'template': 'template'
        }

        self._active_deadline_seconds = active_deadline_seconds
        self._auto_selector = auto_selector
        self._completions = completions
        self._parallelism = parallelism
        self._selector = selector
        self._template = template

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds of this V1beta1JobSpec.
        Optional duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer

        :return: The active_deadline_seconds of this V1beta1JobSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds of this V1beta1JobSpec.
        Optional duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer

        :param active_deadline_seconds: The active_deadline_seconds of this V1beta1JobSpec.
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def auto_selector(self):
        """
        Gets the auto_selector of this V1beta1JobSpec.
        AutoSelector controls generation of pod labels and pod selectors. It was not present in the original extensions/v1beta1 Job definition, but exists to allow conversion from batch/v1 Jobs, where it corresponds to, but has the opposite meaning as, ManualSelector. More info: http://releases.k8s.io/HEAD/docs/design/selector-generation.md

        :return: The auto_selector of this V1beta1JobSpec.
        :rtype: bool
        """
        return self._auto_selector

    @auto_selector.setter
    def auto_selector(self, auto_selector):
        """
        Sets the auto_selector of this V1beta1JobSpec.
        AutoSelector controls generation of pod labels and pod selectors. It was not present in the original extensions/v1beta1 Job definition, but exists to allow conversion from batch/v1 Jobs, where it corresponds to, but has the opposite meaning as, ManualSelector. More info: http://releases.k8s.io/HEAD/docs/design/selector-generation.md

        :param auto_selector: The auto_selector of this V1beta1JobSpec.
        :type: bool
        """

        self._auto_selector = auto_selector

    @property
    def completions(self):
        """
        Gets the completions of this V1beta1JobSpec.
        Completions specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: http://kubernetes.io/docs/user-guide/jobs

        :return: The completions of this V1beta1JobSpec.
        :rtype: int
        """
        return self._completions

    @completions.setter
    def completions(self, completions):
        """
        Sets the completions of this V1beta1JobSpec.
        Completions specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: http://kubernetes.io/docs/user-guide/jobs

        :param completions: The completions of this V1beta1JobSpec.
        :type: int
        """

        self._completions = completions

    @property
    def parallelism(self):
        """
        Gets the parallelism of this V1beta1JobSpec.
        Parallelism specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: http://kubernetes.io/docs/user-guide/jobs

        :return: The parallelism of this V1beta1JobSpec.
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """
        Sets the parallelism of this V1beta1JobSpec.
        Parallelism specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: http://kubernetes.io/docs/user-guide/jobs

        :param parallelism: The parallelism of this V1beta1JobSpec.
        :type: int
        """

        self._parallelism = parallelism

    @property
    def selector(self):
        """
        Gets the selector of this V1beta1JobSpec.
        Selector is a label query over pods that should match the pod count. Normally, the system sets this field for you. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors

        :return: The selector of this V1beta1JobSpec.
        :rtype: UnversionedLabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1beta1JobSpec.
        Selector is a label query over pods that should match the pod count. Normally, the system sets this field for you. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors

        :param selector: The selector of this V1beta1JobSpec.
        :type: UnversionedLabelSelector
        """

        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1beta1JobSpec.
        Template is the object that describes the pod that will be created when executing a job. More info: http://kubernetes.io/docs/user-guide/jobs

        :return: The template of this V1beta1JobSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1beta1JobSpec.
        Template is the object that describes the pod that will be created when executing a job. More info: http://kubernetes.io/docs/user-guide/jobs

        :param template: The template of this V1beta1JobSpec.
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

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
