import allure
from api.goods_api import GoodsApi
goods_api = GoodsApi()
@allure.title("商品评论接口测试")
def test_goods_api():
    res = goods_api.get_comment(65)
    assert res.status_code == 200
    assert "匿名用户" in res.text
    assert "晒单给大家看看" in res.text