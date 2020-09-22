import pymysql

from caw.MyLog import MyLog


class MySqlOperaion:
    '''
    数据库操作的类
    '''

    def connect(self, db_info):
        '''
        连接数据库
        :param db_info:  数据库信息的字典
        :return:
        '''
        if type(db_info) != dict:
            MyLog.error("数据格式不正确,请输入字典格式的数据库信息")
            return
        # 从字典里面获取数据库的信息
        db_ip = db_info["db_ip"]
        db_port = int(db_info["db_port"])
        db_user = db_info["db_user"]
        db_pwd = db_info["db_pwd"]
        db_name = db_info["db_name"]
        try:
            conn = pymysql.connect(host=db_ip, port=db_port, user=db_user, password=db_pwd, database=db_name,
                                   charset='utf8')  # 连接数据库
            MyLog.info(f"连接数据库成功,host:{db_ip},port:{db_port}")
            return conn  # 返回连接对象
        except Exception as e:
            MyLog.error(f"连接数据库失败,host:{db_ip},port:{db_port},异常信息为{e}")
            return

    def disconnect(self, conn):
        '''
        断开数据库连接
        :param conn: 连接对象
        '''
        try:
            conn.close()
            MyLog.info("断开数据库连接成功")
        except Exception as e:
            MyLog.error(f"断开数据库连接失败,异常信息为{e}")

    def execute(self, conn, sql):
        '''
        执行sql语句
        :param conn: 连接对象
        :param sql:sql语句
        '''
        try:
            cursor = conn.cursor()  # 获取光标
            cursor.execute(sql)  # 执行sql语句
            conn.commit()  # 提交
            cursor.close()  # 关闭光标
            MyLog.info(f"数据库中执行sql语句{sql}成功")
        except Exception as e:
            MyLog.error(f"数据库中执行sql语句{sql}失败，异常信息为{e}")

# 测试代码，测试数据库的几个AW是否正常
# db_info = {"db_ip": "jy001", "db_port": 3306, "db_user": "root", "db_pwd": "123456", "db_name": "future"}
# conn = MySqlOperaion().connect(db_info)
# sql = "delete from member where MobilePhone=18066668889;"  # 从Member表中删除指定手机号的数据
# MySqlOperaion().execute(conn, sql)
# MySqlOperaion().disconnect(conn)
