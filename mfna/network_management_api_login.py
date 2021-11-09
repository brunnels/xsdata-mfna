
from .network_management_api_login_input import NetworkManagementApiLoginInput
from .network_management_api_login_output import NetworkManagementApiLoginOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class NetworkManagementApiLogin:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NetworkManagementApiLoginInput
    output = NetworkManagementApiLoginOutput
