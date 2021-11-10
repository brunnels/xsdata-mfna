
from .login_input import LoginInput
from .login_output import LoginOutput

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


class Login:
    style = "rpc"
    location = "https://localhost/soap"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = LoginInput
    output = LoginOutput
