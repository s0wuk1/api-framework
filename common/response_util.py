class ResponseUtil:

    @staticmethod
    def get_status(response):
        return response.json()["status"]

    @staticmethod
    def get_msg(response):
        return response.json()["msg"]

    @staticmethod
    def get_result(response):
        return response.json()["result"]