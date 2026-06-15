import allure
from api.cart_api import Cart_Api
cart_api = Cart_Api()
@allure.title('加入购物车')
def test_add_cart():
    res = cart_api.add_cart(
        goods_id=65,
        item_id = 122,
        goods_num = 1
    )
    assert res.status_code == 200
    body = res.json()
    assert body['status'] == 1
    assert body['msg'] == "成功加入购物车"