import logging
import sys
from unittest import TestCase

from xsdata.formats.dataclass.client import Client
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from mfna import NetworkManagementApiLoginOutput, NasFault, Result, NetworkManagementApiLogin, LoginRequest, \
    LoginInputParms, RequestHeader, NetworkManagementApiLoginInput, LoginResponse

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
            <nas:message>Unable to login with username '***'</nas:message>
            <nas:stack>java.lang.Exception: Unable to login with username '***'</nas:stack>
          </nas:error>
        </detail>
    </SOAP-ENV:Fault>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''

success_xml = '''\
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <nas:loginResponse xmlns:nas="http://microfocus.com/nas/2020/08">
      <nas:Result>
        <nas:Status>200 Logged in</nas:Status>
        <nas:Text>s229dc048-746e-471e-aaf8-66f7317d89d7</nas:Text>
      </nas:Result>
    </nas:loginResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''

xsdata_success_xml = '''\
<?xml version="1.0" encoding="UTF-8"?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
  <soap-env:Body>
    <ns1:loginResponse xmlns:ns1="http://microfocus.com/nas/2020/08">
      <Result>
        <ns1:Status>200 Logged in</ns1:Status>
        <ns1:Text>s229dc048-746e-471e-aaf8-66f7317d89d7</ns1:Text>
      </Result>
    </ns1:loginResponse>
  </soap-env:Body>
</soap-env:Envelope>
'''

soap_ui_success_xml = '''\
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://microfocus.com/nas/2020/08">
 <soapenv:Header/>
 <soapenv:Body>
    <ns:loginResponse>
       <Result>
          <ns:Status>200 Logged in</ns:Status>
          <ns:Text>s229dc048-746e-471e-aaf8-66f7317d89d7</ns:Text>
       </Result>
    </ns:loginResponse>
 </soapenv:Body>
</soapenv:Envelope>
'''

login_envelope = '<?xml version="1.0" encoding="UTF-8"?><soap-env:Envelope ' \
                 'xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"><soap-env:Header><ns1:RequestHeader ' \
                 'xmlns:ns1="http://microfocus.com/nas/2020/08"><ns1:DropNullElements>true</ns1:DropNullElements' \
                 '></ns1:RequestHeader></soap-env:Header><soap-env:Body><ns1:login ' \
                 'xmlns:ns1="http://microfocus.com/nas/2020/08"><parameters><ns1:username>username</ns1:username><ns1' \
                 ':password>password</ns1:password></parameters></ns1:login></soap-env:Body></soap-env' \
                 ':Envelope>'


class LoginOutputParserTests(TestCase):
    def setUp(self):
        self.parser = XmlParser()
        self.parser.config.fail_on_unknown_properties = False  # ideally this should not be required
        self.output = NetworkManagementApiLoginOutput
        self.client = Client.from_service(NetworkManagementApiLogin)
        self.request_header = RequestHeader(drop_null_elements="true")

    def test_request(self):
        request = LoginRequest(
            parameters=LoginInputParms(username="username", password="password")
        )
        request_input = NetworkManagementApiLoginInput(
            body=NetworkManagementApiLoginInput.Body(login=request),
            header=NetworkManagementApiLoginInput.Header(request_header=self.request_header)
        )
        envelope = self.client.prepare_payload(request_input)
        self.assertEqual(login_envelope, envelope.replace("\n", ""))

    def test_error(self):
        response = self.parser.from_string(error_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.fault.detail.nas_fault, NasFault)
        self.assertEqual("Unable to login with username '***'", response.body.fault.detail.nas_fault.message)
        self.assertEqual(
            "java.lang.Exception: Unable to login with username '***'",
            response.body.fault.detail.nas_fault.stack
        )

    def test_success(self):
        response = self.parser.from_string(success_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.login_response.result, Result)
        self.assertEqual("200 Logged in", response.body.login_response.result.status)
        self.assertEqual("s229dc048-746e-471e-aaf8-66f7317d89d7", response.body.login_response.result.text)

    def test_soap_result_without_namespace(self):
        response = self.parser.from_string(success_xml.replace("nas:Result>", "Result>"), self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.login_response.result, Result)
        self.assertEqual("200 Logged in", response.body.login_response.result.status)
        self.assertEqual("s229dc048-746e-471e-aaf8-66f7317d89d7", response.body.login_response.result.text)

    def test_soapui_success(self):
        response = self.parser.from_string(soap_ui_success_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.login_response.result, Result)
        self.assertEqual("200 Logged in", response.body.login_response.result.status)
        self.assertEqual("s229dc048-746e-471e-aaf8-66f7317d89d7", response.body.login_response.result.text)

    def test_xsdata_serialized_response(self):
        test_out = NetworkManagementApiLoginOutput()
        test_out.body = NetworkManagementApiLoginOutput.Body()
        test_out.body.login_response = LoginResponse()
        test_out.body.login_response.result = Result()
        test_out.body.login_response.result.status = "200 Logged in"
        test_out.body.login_response.result.text = "s229dc048-746e-471e-aaf8-66f7317d89d7"
        serializer = XmlSerializer()
        serializer.config.pretty_print = True
        xsdata_xml = serializer.render(test_out)
        self.assertEqual(xsdata_success_xml, xsdata_xml)
        response = self.parser.from_string(xsdata_xml, self.output)
        self.assertIsInstance(response.body.login_response.result, Result)
        self.assertEqual("200 Logged in", response.body.login_response.result.status)
        self.assertEqual("s229dc048-746e-471e-aaf8-66f7317d89d7", response.body.login_response.result.text)
