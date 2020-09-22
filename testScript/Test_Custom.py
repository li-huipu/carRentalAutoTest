import pytest

from baw.Custom import Custom
from caw.DataRead import DataRead
from caw.MyLog import MyLog

add_custom_path = r'datacase\addCustom.csv'


# 将登录的数据导入进来
@pytest.fixture(params=DataRead().read_csv(add_custom_path))
def add_custom_data(request):
    return request.param


class Test_Custom:
    def test_addCustom(self, base_request, base_url, add_custom_data):
        MyLog.info(f"测试用例ID:{add_custom_data[0]}，测试用例描述:{add_custom_data[1]}")
        resp = Custom().addCustom(base_request, base_url, add_custom_data[2].encode("unicode_escape"))
        MyLog.info(resp.text)
