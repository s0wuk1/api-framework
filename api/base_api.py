from common.config_util import config_util
from common.request_util import request
class BaseApi:
    def __init__(self):
        config = config_util.read_yaml()
        self.config = config_util.read_yaml()
        self.base_url = config["env"]["base_url"]
    def get(self, path, params=None):
        url = self.base_url + path
        return request.get(
            url=url,
            params=params
        )
    def post(self, path, data=None):
        url = self.base_url + path
        return request.post(
            url=url,
            data=data
        )