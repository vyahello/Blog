from blog.api.responses import Response
from tests.markers import smoke

_zero: int = 0


@smoke
def test_default_home_page_url(default_home_url_response: Response, success: int) -> None:
    assert default_home_url_response.status_code() == success


@smoke
def test_home_page_url(home_url_response: Response, success: int) -> None:
    assert home_url_response.status_code() == success


@smoke
def test_default_home_page_content(default_home_url_response: Response) -> None:
    assert len(default_home_url_response.as_str()) > _zero


@smoke
def test_home_page_content(home_url_response: Response) -> None:
    assert len(home_url_response.as_str()) > _zero
