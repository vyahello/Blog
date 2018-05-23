import pytest
from server.api.requests import Get
from server.api.responses import Response

_about_url: str = 'http://localhost:5000/about'


@pytest.fixture(scope='module')
def about_url_response(url_endpoint) -> Response:
    """Represent response from `about` page"""

    return Get(url_endpoint + '/about').response()
