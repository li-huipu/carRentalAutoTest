import requests

from caw.MyLog import MyLog




class BaseRequests:

    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        '''
        get方法
        :param url:
        :param kwargs:
        :return:
        '''
        try:
            response = self.session.get(url, **kwargs)
            MyLog.info(f"发送get请求,url={url},请求参数={kwargs}")
            return response
        except Exception as e:
            MyLog.error(f"发送get请求,url={url},请求参数={kwargs},异常信息{e}")
            return

    def post(self, url, data=None, json=None, **kwargs):
        '''
        post方法
        :param url:
        :param kwargs:
        :return:
        '''
        try:
            response = self.session.post(url, data=data, json=json, **kwargs)
            MyLog.info(f"发送post请求,url={url},请求参数={data}{json}{kwargs}")
            return response
        except Exception as e:
            MyLog.error(f"发送post请求,url={url},请求参数={data}{json}{kwargs},异常信息{e}")
            return
