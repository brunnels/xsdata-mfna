import logging
import sys
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser

from mfna import NetworkManagementApiLoginOutput, NasFault, Result

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


class LoginOutputParserTests(TestCase):
    def setUp(self):
        self.parser = XmlParser()
        self.parser.config.fail_on_unknown_properties = False  # ideally this should not be required
        self.output = NetworkManagementApiLoginOutput

    def test_error(self):
        response = self.parser.from_string(error_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.fault.detail.nas_fault, NasFault)

    def test_success(self):
        response = self.parser.from_string(success_xml, self.output)
        self.assertIsInstance(response, self.output)
        self.assertIsInstance(response.body.login_response.result, Result)
