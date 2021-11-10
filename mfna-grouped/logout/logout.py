
from .logout_input import LogoutInput
from .logout_output import LogoutOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class Logout:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LogoutInput
    output = LogoutOutput
