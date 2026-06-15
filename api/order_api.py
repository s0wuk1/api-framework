from api.base_api import BaseApi
from common.config_util import config_util
from common.db_util import db_util
class OrderApi(BaseApi):
    def submit_order(
            self,
            goods_id,
            item_id,
            goods_num,
            address_id=829
    ):
        config = config_util.read_yaml()
        data = {
            "goods_id": goods_id,
            "item_id": item_id,
            "goods_num": goods_num,
            "address_id": address_id,
            "invoice_desc": "不开发票",
            "shipping_code": "shentong",
            "user_note": "17763727177",
            "paypwd": "123456",
            "act": "submit_order"
        }
        return self.post(
            path=config["order"]["submit_path"],
            data=data
        )
    def order_detail(self, order_id):
        params = {
            "id": order_id
        }
        return self.get(
            path=self.config["order"]["detail_path"],
            params=params
        )
    def get_order_by_id(self, order_id):
        sql = f"""
        select *
        from tp_order
        where order_id = {order_id}
        """
        return db_util.query_one(sql)