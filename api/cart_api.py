from api.base_api import BaseApi
from common.config_util import config_util
class Cart_Api(BaseApi):
    def add_cart(self, goods_id, item_id, goods_num):
        config = config_util.read_yaml()
        data = {
            "goods_id": goods_id,
            "item_id": item_id,
            "goods_num": goods_num
        }
        return self.post(
            path=config["cart"]["add_path"],
            data=data
        )
    def update_cart(self, cart_id, goods_num, selected):

        data = {
            "cart[0][id]": cart_id,
            "cart[0][goods_num]": goods_num,
            "cart[0][selected]": selected
        }
        return self.post(
            path=self.config["cart"]["update_path"],
            data=data
        )
# 删除购物车接口
    def delete_cart(self, cart_id):
        data = {
            "cart_ids": [cart_id]
        }
        return self.post(
            path=self.config["cart"]["delete_path"],
            data=data
        )