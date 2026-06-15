from common.db_util import db_util
from api.order_api import OrderApi

order_api = OrderApi()

def test_db_order():
    order_info = order_api.get_order_by_id(1515)

    print(order_info)

    assert order_info is not None