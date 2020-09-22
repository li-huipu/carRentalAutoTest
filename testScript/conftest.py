import sys
import os

import pytest

path = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(path)))

from caw.BaseRequests import BaseRequests
from caw.DataRead import DataRead

ENVPATH = 'dataenv/env.ini'


# 从环境文件中读取base_url
@pytest.fixture(scope='session')
def base_url():
    base_url = DataRead().read_ini(ENVPATH, "base_url")
    return base_url


# 从环境文件中读取db信息，返回一个字典
@pytest.fixture(scope='session')
def db_info():
    db_ip = DataRead().read_ini(ENVPATH, "db_ip")
    db_port = DataRead().read_ini(ENVPATH, "db_port")
    db_name = DataRead().read_ini(ENVPATH, "db_name")
    db_user = DataRead().read_ini(ENVPATH, "db_user")
    db_pwd = DataRead().read_ini(ENVPATH, "db_pwd")
    db_info = {"db_ip": db_ip, "db_port": db_port, "db_name": db_name, "db_user": db_user, "db_pwd": db_pwd}
    print(db_info)
    return db_info


# base_request实例化
@pytest.fixture(scope='session')
def base_request():
    return BaseRequests()
