import logging
import sys
from unittest import TestCase

from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser

from mfna import NetworkManagementApiLogoutOutput, NasFault, Result, LogoutRequest, NetworkManagementApiLogout, \
    RequestHeader, LogoutInputParms, NetworkManagementApiLogoutInput

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

error_xml = '''\
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Body>
    <SOAP-ENV:Fault>
      <faultcode>SOAP-ENV:Server</faultcode>
      <faultstring>Server Error</faultstring>
        <detail>
          <nas:error xmlns:nas="http://microfocus.com/nas/2020/08">
            <nas:message>Example error message</nas:message>
            <nas:stack>java.lang.Exception: Example exception</nas:stack>
          </nas:error>
        </detail>
    </SOAP-ENV:Fault>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''

error_201_xml = '''\
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <nas:logoutResponse xmlns:nas="http://microfocus.com/nas/2020/08">
      <nas:Result>
        <nas:Status>201 Session sf22a68fa-2bee-4fb8-8ee6-0c7175d55312 does not exist</nas:Status>
      </nas:Result>
    </nas:logoutResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''

success_xml = '''\
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <nas:logoutResponse xmlns:nas="http://microfocus.com/nas/2020/08">
      <nas:Result>
        <nas:Status>200 Logged out</nas:Status>
        <nas:Text>Logged out</nas:Text>
      </nas:Result>
    </nas:logoutResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''

logout_envelope = '<?xml version="1.0" encoding="UTF-8"?><soap-env:Envelope ' \
                  'xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"><soap-env:Header><ns1:RequestHeader ' \
                  'xmlns:ns1="http://microfocus.com/nas/2020/08"><ns1:DropNullElements>true</ns1:DropNullElements' \
                  '></ns1:RequestHeader></soap-env:Header><soap-env:Body><ns1:logout ' \
                  'xmlns:ns1="http://microfocus.com/nas/2020/08"><parameters><ns1:sessionid>sf22a68fa-2bee-4fb8-8ee6' \
                  '-0c7175d55312</ns1:sessionid></parameters></ns1:logout></soap-env:Body></soap-env:Envelope>'


class LogoutOutputParserTests(TestCase):
    def setUp(self):
        self.parser = XmlParser()
        self.parser.config.fail_on_unknown_properties = False  # ideally this should not be required
        self.output = NetworkManagementApiLogoutOutput
        self.client = Client.from_service(NetworkManagementApiLogout)
        self.request_header = RequestHeader(drop_null_elements="true")

    def test_request(self):
        request = LogoutRequest(
            parameters=LogoutInputParms(sessionid="sf22a68fa-2bee-4fb8-8ee6-0c7175d55312")
        )
        request_input = NetworkManagementApiLogoutInput(
            body=NetworkManagementApiLogoutInput.Body(logout=request),
            header=NetworkManagementApiLogoutInput.Header(request_header=self.request_header)
        )
        envelope = self.client.prepare_payload(request_input)
        self.assertEqual(logout_envelope, envelope.replace("\n", ""))

    def test_error(self):
        response = self.parser.from_string(error_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.fault.detail.nas_fault, NasFault)
        self.assertEqual('Example error message', response.body.fault.detail.nas_fault.message)
        self.assertEqual('java.lang.Exception: Example exception', response.body.fault.detail.nas_fault.stack)

    def test_error_201(self):
        response = self.parser.from_string(error_201_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.logout_response.result, Result)
        self.assertEqual(
            "201 Session sf22a68fa-2bee-4fb8-8ee6-0c7175d55312 does not exist",
            response.body.logout_response.result.status
        )

    def test_success(self):
        response = self.parser.from_string(success_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.logout_response.result, Result)
        self.assertEqual("200 Logged out", response.body.logout_response.result.status)
        self.assertEqual("Logged out", response.body.logout_response.result.text)
