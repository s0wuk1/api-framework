import allure
from api.order_api import OrderApi
from api.cart_api import Cart_Api
order_api = OrderApi()
cart_api = Cart_Api()
@allure.title("订单业务流程")
def test_order_flow():
    # 先选中购物车商品
    update_res = cart_api.update_cart(
        cart_id=10,
        goods_num=1,
        selected=1
    )
    update_body = update_res.json()
    assert update_body["status"] == 1
    print("购物车更新成功")
    # 提交订单
    submit_res = order_api.submit_order()
    assert submit_res.status_code == 200
    submit_body = submit_res.json()
    assert submit_body["status"] == 1
    order_id = submit_body["result"]
    print("订单ID:", order_id)
    # 查询订单详情
    detail_res = order_api.order_detail(order_id)
    assert detail_res.status_code == 200
    print(detail_res.url)