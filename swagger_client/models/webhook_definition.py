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
from swagger_client.models.connection_definition import ConnectionDefinition  # noqa: F401,E501
from swagger_client.models.header import Header  # noqa: F401,E501


class WebhookDefinition(ConnectionDefinition):
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
        'url': 'str',
        'headers': 'list[Header]',
        'custom_headers': 'list[Header]',
        'default_payload': 'str',
        'webhook_type': 'str'
    }
    if hasattr(ConnectionDefinition, "swagger_types"):
        swagger_types.update(ConnectionDefinition.swagger_types)

    attribute_map = {
        'url': 'url',
        'headers': 'headers',
        'custom_headers': 'customHeaders',
        'default_payload': 'defaultPayload',
        'webhook_type': 'webhookType'
    }
    if hasattr(ConnectionDefinition, "attribute_map"):
        attribute_map.update(ConnectionDefinition.attribute_map)

    def __init__(self, url=None, headers=None, custom_headers=None, default_payload=None, webhook_type='Webhook', *args, **kwargs):  # noqa: E501
        """WebhookDefinition - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._headers = None
        self._custom_headers = None
        self._default_payload = None
        self._webhook_type = None
        self.discriminator = None
        self.url = url
        if headers is not None:
            self.headers = headers
        if custom_headers is not None:
            self.custom_headers = custom_headers
        self.default_payload = default_payload
        if webhook_type is not None:
            self.webhook_type = webhook_type
        ConnectionDefinition.__init__(self, *args, **kwargs)

    @property
    def url(self):
        """Gets the url of this WebhookDefinition.  # noqa: E501

        URL for the webhook connection.  # noqa: E501

        :return: The url of this WebhookDefinition.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookDefinition.

        URL for the webhook connection.  # noqa: E501

        :param url: The url of this WebhookDefinition.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this WebhookDefinition.  # noqa: E501

        List of access authorization headers.  # noqa: E501

        :return: The headers of this WebhookDefinition.  # noqa: E501
        :rtype: list[Header]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this WebhookDefinition.

        List of access authorization headers.  # noqa: E501

        :param headers: The headers of this WebhookDefinition.  # noqa: E501
        :type: list[Header]
        """

        self._headers = headers

    @property
    def custom_headers(self):
        """Gets the custom_headers of this WebhookDefinition.  # noqa: E501

        List of custom webhook headers.  # noqa: E501

        :return: The custom_headers of this WebhookDefinition.  # noqa: E501
        :rtype: list[Header]
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        """Sets the custom_headers of this WebhookDefinition.

        List of custom webhook headers.  # noqa: E501

        :param custom_headers: The custom_headers of this WebhookDefinition.  # noqa: E501
        :type: list[Header]
        """

        self._custom_headers = custom_headers

    @property
    def default_payload(self):
        """Gets the default_payload of this WebhookDefinition.  # noqa: E501

        Default payload of the webhook.  # noqa: E501

        :return: The default_payload of this WebhookDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_payload

    @default_payload.setter
    def default_payload(self, default_payload):
        """Sets the default_payload of this WebhookDefinition.

        Default payload of the webhook.  # noqa: E501

        :param default_payload: The default_payload of this WebhookDefinition.  # noqa: E501
        :type: str
        """
        if default_payload is None:
            raise ValueError("Invalid value for `default_payload`, must not be `None`")  # noqa: E501

        self._default_payload = default_payload

    @property
    def webhook_type(self):
        """Gets the webhook_type of this WebhookDefinition.  # noqa: E501

        Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, and `NewRelic`.  # noqa: E501

        :return: The webhook_type of this WebhookDefinition.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this WebhookDefinition.

        Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, and `NewRelic`.  # noqa: E501

        :param webhook_type: The webhook_type of this WebhookDefinition.  # noqa: E501
        :type: str
        """

        self._webhook_type = webhook_type

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
        if issubclass(WebhookDefinition, dict):
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
        if not isinstance(other, WebhookDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
