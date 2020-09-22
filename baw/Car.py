import json

from baw.Const import *


class Car:
    def addCar(self, baserequest, base_url, data):
        url = base_url + ADDCAR
        # 如果不是字典格式的，将其转为字典
        if type(data) != dict:
            # 通过csv读取出来是String，将string转字典
            data = json.loads(data)
        response = baserequest.post(url, data=data, headers=headers)
        return response

    def deleteCar(self, baserequest, base_url, carnumber):
        url = base_url + DELETECAR
        data = {'carnumber': carnumber}
        response = baserequest.post(url, data=data, headers=headers)
        return response
