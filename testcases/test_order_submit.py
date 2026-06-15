import allure
import pytest
@allure.title("提交订单")
@pytest.mark.parametrize(
    "goods_id,item_id,goods_num",
    [
        (65, 122, 1),
        (65, 122, 2),
        (65, 122, 3)
    ]
)
def test_submit_order(goods_id,item_id,goods_num):
    print(goods_id)
    print(item_id)
    print(goods_num)