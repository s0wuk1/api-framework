from api.base_api import BaseApi
from common.config_util import config_util
class GoodsApi(BaseApi):
    def get_comment(self,goods_id):
        config = config_util.read_yaml()
        url = (
            config['env']['base_url']
            + f"/index.php?m=Home&c=goods&a=ajaxComment"
            + f"&goods_id={goods_id}"
            + "&commentType=1&p=1"
        )
        return self.get(url=url)