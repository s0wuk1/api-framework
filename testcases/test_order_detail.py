import pytest
import allure
from api.order_api import OrderApi
# from common.excel_util import excel_util
from common.assert_util import assert_util
order_api = OrderApi()
from common.yaml_util import yaml_util
order_data = yaml_util.read_yaml(
    "data/order_data.yaml"
)["goods"]

@pytest.mark.parametrize(
    "create_order",
    order_data,
    indirect=True
)
@allure.feature("订单模块")
@allure.story("订单详情")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("订单详情测试")
def test_order_detail(create_order):

    with allure.step("获取订单信息"):
        order_id = create_order["order_id"]
        user_id = create_order["user_id"]
        order_info = order_api.get_order_by_id(order_id)
        allure.attach(
            str(order_id),
            "订单ID"
        )
        allure.attach(
            str(order_info),
            "订单详情"
        )
    with allure.step("校验订单ID"):

        assert_util.assert_equal(
            order_info["order_id"],
            int(order_id),
            "订单ID校验失败"
        )
    with allure.step("校验用户ID"):

        assert_util.assert_equal(
            order_info["user_id"],
            user_id,
            "用户ID校验失败"
        )
    with allure.step("校验订单状态"):

        assert_util.assert_equal(
            order_info["order_status"],
            0,
            "订单状态校验失败"
        )
    with allure.step("校验支付状态"):

        assert_util.assert_equal(
            order_info["pay_status"],
            0,
            "支付状态校验失败"
        )