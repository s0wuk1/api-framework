from api.base_api import BaseApi
from common.config_util import config_util
class LoginApi(BaseApi):
    def login(self, username, password):
        config = config_util.read_yaml()
        data = {
            "username": username,
            "password": password
        }
        return self.post(
            path=config["login"]["path"],
            data=data
        )