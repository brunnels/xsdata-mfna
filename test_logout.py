import logging
import sys
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser

from mfna import NetworkManagementApiLogoutOutput

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

error_xml = '''\
<?xml version="1.0" encoding="utf-8" ?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <nas:logoutResponse xmlns:nas="http://microfocus.com/nas/2020/08">
      <nas:Result>
        <nas:Status>201 Session sf22a68fa-2bee-4fb8-8ee6-0c7175d55312 does not exists</nas:Status>
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


class LogoutOutputParserTests(TestCase):
    def setUp(self):
        self.parser = XmlParser()
        self.parser.config.fail_on_unknown_properties = False  # ideally this should not be required
        self.output = NetworkManagementApiLogoutOutput

    def test_error(self):
        response = self.parser.from_string(error_xml, self.output)
        self.assertIsInstance(response, self.output)

    def test_success(self):
        response = self.parser.from_string(success_xml, self.output)
        self.assertIsInstance(response, self.output)
