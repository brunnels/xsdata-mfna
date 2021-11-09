
from .network_management_api_activate_device_input import NetworkManagementApiActivateDeviceInput
from .network_management_api_activate_device_output import NetworkManagementApiActivateDeviceOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class NetworkManagementApiActivateDevice:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = NetworkManagementApiActivateDeviceInput
    output = NetworkManagementApiActivateDeviceOutput
