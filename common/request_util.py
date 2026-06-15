import requests
from common.log_util import logger
from common import global_var
class RequestUtil:
    def __init__(self):
        self.session = requests.Session()
    # GET 请求
    def get(self, url, params=None, headers=None):
        res = self.session.get(
            url=url,
            params=params,
            headers=headers
        )
        return res

    # POST 请求
    def post(self, url, data=None, headers=None):
        if headers is None:
            headers = {}
        # if global_var.TOKEN:
        #         # 自动放进请求头
        #     headers["token"] = global_var.TOKEN
        logger.info(f" 请求地址：{url}")
        logger.info(f"请求参数: {data}")
        res = self.session.post(url=url, data=data, headers=headers)
        logger.info(f"状态码: {res.status_code}")
        logger.info(f"响应数据: {res.text}")
        return res


request = RequestUtil()