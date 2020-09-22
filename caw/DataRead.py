import configparser
import csv

import yaml

from caw.Path import Path


class DataRead:
    project_path = Path().getProjectPath()  # 获取工程的根路径

    def read_ini(self, file_path, key):
        '''
        读取ini配置文件
        :param file_path: ini文件的路径，是一个相对路径，相对工程的路径，比如：dataenv/dataenv.ini
        :param key: 要取值的key
        :return: key对应的value
        '''
        # ini文件的绝对路径
        real_file_path = self.project_path + file_path
        # print(real_file_path)
        # 调用configparser来解析ini文件
        config = configparser.ConfigParser()
        # 读文件
        config.read(real_file_path)
        # 读取key对应的value
        value = config.get("config", key)
        return value

    def read_yaml(self, file_path):
        '''
        读取yaml文件
        :param file_path: yaml文件的路径，是一个相对路径，相对工程的路径，比如：datacase/member/register_success.yaml
        :return: yaml文件内容，字典格式的
        '''
        # yaml文件的绝对路径
        real_file_path = self.project_path + file_path
        # 打开文件并读取文件内容
        with open(real_file_path, "r", encoding='utf-8') as f:
            file_content = f.read()
        # 用load方法将文件内容转成字典格式的
        dict_content = yaml.load(file_content, Loader=yaml.FullLoader)
        return dict_content

    def read_csv1(self, file_path):
        '''
        读CSV文件，转化为字典
        :param csvfile:
        :return:
        '''
        real_file_path = self.project_path + file_path
        with open(real_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            fieldnames = next(reader)
            csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            for row in csv_reader:
                dist_list = {}
                for k, v in row.items():
                    dist_list[k] = v
            return dist_list

    def read_csv(self, csv_name):
        '''
        获取csv文件
        :param csv_name: csv文件名称
        :return: 返回获取到的csv数据,如:
                [('admin','123456'),('xiao1','123456'),('xiao2','123456'),('xiao3','123456')]
        '''
        # 打开csv文件
        real_file_path = self.project_path + csv_name
        par = True
        all_row_list = []
        with open(real_file_path, mode='r') as csv_file:
            csv_data = csv.reader(csv_file)
            # print('获取到的数据是：',csv_data)
            for row in csv_data:
                # print('每行数据是：',row)
                # 过滤标题,只显示内容
                if par:
                    par = False
                    continue
                # 列表转化成元组
                row_tuple = tuple(row)
                all_row_list.append(row_tuple)
            # print('获取到的csv数据是：',all_row_list)
        return all_row_list

# 测试代码，测试读文件的方法是否正确
# print(DataRead().read_ini('dataenv/dataenv.ini', "base_url"))
# print(DataRead().read_yaml('datacase/member/register_success.yaml'))
print(DataRead().read_csv('datacase/addCar.csv'))
