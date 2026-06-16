import pytest
from api.login_api import LoginApi

login_api = LoginApi()


@pytest.mark.smoke
def test_login():
    res = login_api.login(
        username="17763727177",
        password="123456"
    )

    assert res.status_code == 200