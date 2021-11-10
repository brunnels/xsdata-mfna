
from .activate_device_input import ActivateDeviceInput
from .activate_device_output import ActivateDeviceOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class ActivateDevice:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = ActivateDeviceInput
    output = ActivateDeviceOutput
