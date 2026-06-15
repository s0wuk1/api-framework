import pytest
import allure
from api.order_api import OrderApi
from api.cart_api import Cart_Api
from api.login_api import LoginApi
login_api = LoginApi()
from common.db_util import db_util
from common.response_util import ResponseUtil
order_api = OrderApi()
cart_api = Cart_Api()
from common.yaml_util import yaml_util
yaml_data = yaml_util.read_yaml(
    "data/order_data.yaml"
)
@pytest.fixture(scope="session", autouse=True)
def login():
    print("开始登录")
    res = login_api.login(
        username=yaml_data["login"]["username"],
        password=yaml_data["login"]["password"]
    )
    print("登录成功")
    return res

@pytest.fixture
def create_order(login, request):
    data = request.param
    goods_id = data["goods_id"]
    item_id = data["item_id"]
    goods_num = data["goods_num"]
    result = ResponseUtil.get_result(login)
    user_id = result["user_id"]
    sql = f"""
    delete from tp_cart
    where user_id = {user_id}
    """
    with allure.step("清理购物车"):
        db_util.execute(sql)
    # 加购物车
    with allure.step("加入购物车"):
        cart_api.add_cart(
            goods_id=goods_id,
            item_id=item_id,
            goods_num=goods_num
        )
    with allure.step("查询购物车ID"):
        user_id = login.json()["result"]["user_id"]
        sql = f"""
        select id
        from tp_cart
        where user_id = {user_id}
        order by id desc
        limit 1
        """

        result = db_util.query_one(sql)

        cart_id = result["id"]

    with allure.step("选中购物车商品"):
        cart_api.update_cart(
            cart_id=cart_id,
            goods_num=goods_num,
            selected=1
        )

    with allure.step("提交订单"):
        res = order_api.submit_order(
            goods_id=goods_id,
            item_id=item_id,
            goods_num=goods_num
        )
        order_id = res.json()["result"]
    return {
        "order_id": order_id,
        "user_id": user_id,
        "cart_id": cart_id
    }
