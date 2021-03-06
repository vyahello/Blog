from blog.api.requests import Request
from tests.markers import performance

_xtime: int = 1000
_zero: int = 0
_inc: int = 1


@performance
def test_endurance(default_home_request: Request, success: int) -> None:
    times: int = _xtime
    while times > _zero:
        assert default_home_request.response().status_code() == success
        times -= _inc
