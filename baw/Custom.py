import json

from baw.Const import *


class Custom:
    def addCustom(self, baserequest, base_url, data):
        url = base_url + ADDCUSTOM
        # 如果不是字典格式的，将其转为字典
        if type(data) != dict:
            # 通过csv读取出来是String，将string转字典
            data = json.loads(data)
        # response = baserequest.post(url, data=data, proxies=Const().proxies, headers=Const().headers)
        response = baserequest.post(url, data=data, headers=headers)

        return response
