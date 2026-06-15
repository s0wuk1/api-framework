import pytest
from api.login_api import LoginApi
login_api = LoginApi()
from common.config_util import config_util
config = config_util.read_yaml()
import allure
@allure.title("登录接口测试")
@allure.description("测试登录接口是否正常")
@pytest.mark.parametrize("account",config["accounts"])
def test_login(account):

    # 第一步：准备测试数据
    with allure.step("准备登录数据"):
        username = account["username"]
        password = account["password"]

    # 第二步：发送请求
    with allure.step("发送登录请求"):
        res = login_api.login(username = username, password = password)

    # 第三步：状态码断言
    with allure.step("校验状态码"):
        assert res.status_code == 200

        # 第四步：业务断言
    with allure.step("校验登录结果"):
        result = res.json()
        assert result["status"] == account["expect_status"]