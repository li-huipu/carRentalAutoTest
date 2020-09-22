import json

import pytest

from baw.Car import Car
from caw.Asserts import Asserts
from caw.DataRead import DataRead
from caw.MyLog import MyLog

add_car_path = r'datacase\addCar.csv'


# 将登录的数据导入进来
@pytest.fixture(params=DataRead().read_csv(add_car_path))
def add_car_data(request):
    return request.param


class Test_Car:
    def test_addCar(self, base_request, base_url, add_car_data):
        MyLog.info(f"测试用例ID:{add_car_data[0]}，测试用例描述:{add_car_data[1]}")
        resp = Car().addCar(base_request, base_url, add_car_data[2])
        MyLog.info(resp.text)
        Asserts().equal(resp, add_car_data[3], 'code,msg')
        test_data = json.loads(add_car_data[2])
        resp = Car().deleteCar(base_request, base_url, test_data['carnumber'])
        MyLog.info(resp.text)
