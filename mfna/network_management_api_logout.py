
from .network_management_api_logout_input import NetworkManagementApiLogoutInput
from .network_management_api_logout_output import NetworkManagementApiLogoutOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class NetworkManagementApiLogout:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NetworkManagementApiLogoutInput
    output = NetworkManagementApiLogoutOutput
