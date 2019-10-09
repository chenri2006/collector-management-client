# coding: utf-8

"""
    Sumo Logic API

    # Getting Started Welcome to the Sumo Logic API reference. You can use these APIs to interact with the Sumo Logic platform. For information on the collector and search APIs see our [API home page](https://help.sumologic.com/APIs). ## API Endpoints Sumo Logic has several deployments in different geographic locations. You'll need to use the Sumo Logic API endpoint corresponding to your geographic location. See the table below for the different API endpoints by deployment. For details determining your account's deployment see [API endpoints](https://help.sumologic.com/?cid=3011). <table>   <tr>     <td> <strong>Deployment</strong> </td>     <td> <strong>Endpoint</strong> </td>   </tr> <tr>     <td> AU </td>     <td> https://api.au.sumologic.com/api/ </td>   </tr>   <tr>     <td> CA </td>     <td> https://api.ca.sumologic.com/api/ </td>   </tr> <tr>     <td> DE </td>     <td> https://api.de.sumologic.com/api/ </td>   </tr>   <tr>     <td> EU </td>     <td> https://api.eu.sumologic.com/api/ </td>   </tr>   <tr>     <td> JP </td>     <td> https://api.jp.sumologic.com/api/ </td>   </tr>   <tr>     <td> US1 </td>     <td> https://api.sumologic.com/api/ </td>   </tr>   <tr>     <td> US2 </td>     <td> https://api.us2.sumologic.com/api/ </td>   </tr> </table> ## Authentication Sumo Logic supports the following options for API authentication: - Access ID and Access Key - Base64 encoded Access ID and Access Key  See [Access Keys](https://help.sumologic.com/Manage/Security/Access-Keys) to generate an Access Key. Make sure to copy the key you create, because it is displayed only once. When you have an Access ID and Access Key you can execute requests such as the following:   ```bash   curl -u \"<accessId>:<accessKey>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```  Where `deployment` is either `au`, `ca`, `de`, `eu`, `jp`, `us1`, or `us2`. See [API endpoints](#section/API-Endpoints) for details.  If you prefer to use basic access authentication, you can do a Base64 encoding of your `<accessId>:<accessKey>` to authenticate your HTTPS request. The following is an example request, replace the placeholder `<encoded>` with your encoded Access ID and Access Key string:   ```bash   curl -H \"Authorization: Basic <encoded>\" -X GET https://api.<deployment>.sumologic.com/api/v1/users   ```   Refer to [API Authentication](https://help.sumologic.com/?cid=3012) for a Base64 example.  ## Status Codes Generic status codes that apply to all our APIs. See the [HTTP status code registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) for reference. <table>   <tr>     <td> <strong>HTTP Status Code</strong> </td>     <td> <strong>Error Code</strong> </td>     <td> <strong>Description</strong> </td>   </tr>   <tr>     <td> 301 </td>     <td> moved </td>     <td> The requested resource SHOULD be accessed through returned URI in Location Header.</td>   </tr>   <tr>     <td> 401 </td>     <td> unauthorized </td>     <td> Credential could not be verified. </td>   </tr>   <tr>     <td> 403 </td>     <td> forbidden </td>     <td> This operation is not allowed for your account type or the user doesn't have the role capability to perform this action. </td>   </tr>   <tr>     <td> 404 </td>     <td> notfound </td>     <td> Requested resource could not be found. </td>   </tr>   <tr>     <td> 405 </td>     <td> method.unsupported </td>     <td> Unsupported method for URL. </td>   </tr>   <tr>     <td> 415 </td>     <td> contenttype.invalid </td>     <td> Invalid content type. </td>   </tr>   <tr>     <td> 429 </td>     <td> rate.limit.exceeded </td>     <td> The API request rate is higher than 4 request per second or inflight API requests are higher than 10 request per second. </td>   </tr>   <tr>     <td> 500 </td>     <td> internal.error </td>     <td> Internal server error. </td>   </tr>   <tr>     <td> 503 </td>     <td> service.unavailable </td>     <td> Service is currently unavailable. </td>   </tr> </table> ## Filtering Some API endpoints support filtering results on a specified set of fields. Each endpoint that supports filtering will list the fields that can be filtered. Multiple fields can be combined by using an ampersand `&` character.  For example, to get 20 users whose `firstName` is `John` and `lastName` is `Doe`:   ```bash   api.sumologic.com/v1/users?limit=20&firstName=John&lastName=Doe   ```  ## Sorting Some API endpoints support sorting fields by using the `sortBy` query parameter. The default sort order is ascending. Prefix the field with a minus sign `-` to sort in descending order.  For example, to get 20 users sorted by their `email` in descending order:   ```bash   api.sumologic.com/v1/users?limit=20&sort=-email   ```  ## Rate Limiting * A rate limit of four API requests per second (240 requests per minute) applies to all API calls from a user. * A rate limit of 10 concurrent requests to any API endpoint applies to an access key.  If a rate is exceeded, a rate limit exceeded 429 status code is returned.  ## Generating Clients You can use [OpenAPI Generator](https://openapi-generator.tech) to generate clients from the YAML file to access the API.  ### Using [NPM](https://www.npmjs.com/get-npm) 1. Install [NPM package wrapper](https://github.com/openapitools/openapi-generator-cli) globally, exposing the CLI   on the command line:   ```bash   npm install @openapitools/openapi-generator-cli -g   ```   You can see detailed instructions [here](https://openapi-generator.tech/docs/installation#npm).  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   ### Using [Homebrew](https://brew.sh/) 1. Install OpenAPI Generator   ```bash   brew install openapi-generator   ```  2. Download the [YAML file](/docs/sumologic-api.yaml) and save it locally. Let's say the file is saved as `sumologic-api.yaml`. 3. Use the following command to generate `python` client side code inside the `sumo/client/python` directory:   ```bash   openapi-generator generate -i sumologic-api.yaml -g python -o sumo/client/python   ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.aggregation import Aggregation  # noqa: F401,E501
from swagger_client.models.filter import Filter  # noqa: F401,E501
from swagger_client.models.rule_actions import RuleActions  # noqa: F401,E501
from swagger_client.models.rules_library_base import RulesLibraryBase  # noqa: F401,E501


class RulesLibraryRule(RulesLibraryBase):
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
        'status': 'str',
        'filters': 'list[Filter]',
        'join_expression': 'str',
        'aggregation': 'Aggregation',
        'rule_actions': 'RuleActions'
    }
    if hasattr(RulesLibraryBase, "swagger_types"):
        swagger_types.update(RulesLibraryBase.swagger_types)

    attribute_map = {
        'status': 'status',
        'filters': 'filters',
        'join_expression': 'joinExpression',
        'aggregation': 'aggregation',
        'rule_actions': 'ruleActions'
    }
    if hasattr(RulesLibraryBase, "attribute_map"):
        attribute_map.update(RulesLibraryBase.attribute_map)

    def __init__(self, status=None, filters=None, join_expression=None, aggregation=None, rule_actions=None, *args, **kwargs):  # noqa: E501
        """RulesLibraryRule - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._filters = None
        self._join_expression = None
        self._aggregation = None
        self._rule_actions = None
        self.discriminator = None
        self.status = status
        self.filters = filters
        if join_expression is not None:
            self.join_expression = join_expression
        if aggregation is not None:
            self.aggregation = aggregation
        self.rule_actions = rule_actions
        RulesLibraryBase.__init__(self, *args, **kwargs)

    @property
    def status(self):
        """Gets the status of this RulesLibraryRule.  # noqa: E501

        The status of the cloud SIEM rule, either active or inactive.  # noqa: E501

        :return: The status of this RulesLibraryRule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RulesLibraryRule.

        The status of the cloud SIEM rule, either active or inactive.  # noqa: E501

        :param status: The status of this RulesLibraryRule.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def filters(self):
        """Gets the filters of this RulesLibraryRule.  # noqa: E501

        A list of expressions describing what the cloud SIEM rule filters.  # noqa: E501

        :return: The filters of this RulesLibraryRule.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this RulesLibraryRule.

        A list of expressions describing what the cloud SIEM rule filters.  # noqa: E501

        :param filters: The filters of this RulesLibraryRule.  # noqa: E501
        :type: list[Filter]
        """
        if filters is None:
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501

        self._filters = filters

    @property
    def join_expression(self):
        """Gets the join_expression of this RulesLibraryRule.  # noqa: E501

        An expression describing what the cloud SIEM rule joins.  # noqa: E501

        :return: The join_expression of this RulesLibraryRule.  # noqa: E501
        :rtype: str
        """
        return self._join_expression

    @join_expression.setter
    def join_expression(self, join_expression):
        """Sets the join_expression of this RulesLibraryRule.

        An expression describing what the cloud SIEM rule joins.  # noqa: E501

        :param join_expression: The join_expression of this RulesLibraryRule.  # noqa: E501
        :type: str
        """

        self._join_expression = join_expression

    @property
    def aggregation(self):
        """Gets the aggregation of this RulesLibraryRule.  # noqa: E501


        :return: The aggregation of this RulesLibraryRule.  # noqa: E501
        :rtype: Aggregation
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this RulesLibraryRule.


        :param aggregation: The aggregation of this RulesLibraryRule.  # noqa: E501
        :type: Aggregation
        """

        self._aggregation = aggregation

    @property
    def rule_actions(self):
        """Gets the rule_actions of this RulesLibraryRule.  # noqa: E501


        :return: The rule_actions of this RulesLibraryRule.  # noqa: E501
        :rtype: RuleActions
        """
        return self._rule_actions

    @rule_actions.setter
    def rule_actions(self, rule_actions):
        """Sets the rule_actions of this RulesLibraryRule.


        :param rule_actions: The rule_actions of this RulesLibraryRule.  # noqa: E501
        :type: RuleActions
        """
        if rule_actions is None:
            raise ValueError("Invalid value for `rule_actions`, must not be `None`")  # noqa: E501

        self._rule_actions = rule_actions

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
        if issubclass(RulesLibraryRule, dict):
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
        if not isinstance(other, RulesLibraryRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
