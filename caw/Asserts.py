import pytest_check as check

from caw.MyLog import MyLog


class Asserts:
    def equal(self, response, expect, key_str, assert_msg=''):
        '''
        校验response与expect中，相应的关键字对应的值是否匹配
        :param response: 响应信息
        :param expect: 预期结果
        :param key_str: key字符串，比如"status,code,data"
        :param assert_msg: 校验失败时的提示信息
        :return:
        '''
        try:
            keys = key_str.split(",")  # 将"status,code,data"用逗号分隔
            response = response.json()  # response转换成json格式的
            expect = eval(expect)
            for key in keys:
                ret = str(response.get(key))  # 获取response中key对应的value，并转成字符串
                # print("ret ====" + ret)
                exp = str(expect.get(key))  # 获取预期结果中key对应的value，并转成字符串
                # print("exp ====" + exp)
                check.equal(ret, exp, assert_msg)  # 调用pytest_check来检查实际结果与预期结果是否相符
                MyLog.info(f"响应信息:{response},校验{key},实际结果:{ret},预期结果:{exp},断言成功")
        except Exception as e:
            MyLog.error(f"出现异常,响应信息:{response},校验{key},实际结果:{ret},预期结果:{exp},断言失败{assert_msg}")

    def isTrue(self, real, assert_msg=''):
        '''
        判断一个表达式是否为true
        :param real:
        :param assert_msg:
        :return:
        '''
        try:
            check.is_true(real, assert_msg)
            MyLog.info(f"校验:{real},实际结果:{real},预期结果:True,断言成功")
        except Exception as e:
            MyLog.error(f"校验:{real},实际结果:{real},预期结果:True,断言失败{assert_msg}")
            return


if __name__ == '__main__':
    import requests

    response = requests.get("http://jy001:8080/futureloan/mvc/api/member/register?mobilephone=18291334457&pwd=123456")
    print(response.text)  # 实际返回结果
    expect = {"code": 20111, "data": {}, "msg": "手机号码已被注册", "status": 0}  # 预期结果
    Asserts().equal(response, expect, 'status,code,msg', "校验失败")
