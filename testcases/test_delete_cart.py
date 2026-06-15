import allure
from api.cart_api import Cart_Api
cart_api = Cart_Api()
@allure.title("删除购物车")
def test_delete_cart():

    res = cart_api.delete_cart(
        cart_ids=5
    )
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == 1
    assert body["msg"] == "删除成功"