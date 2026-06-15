import allure
from api.cart_api import Cart_Api

cart_api = Cart_Api()
@allure.title('修改购物车')
def test_update_cart():

    res = cart_api.update_cart(
    cart_id = 8,
    goods_num = 1,
    selected = 1
    )
    assert res.status_code == 200
    body = res.json()
    cart_id = body['result']["cartList"][0]['id']
    print("cart_id=",cart_id)
    assert body['status'] == 1