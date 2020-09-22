import os


class Path:
    def getProjectPath(self):
        '''
        获取工程根路径
        :return:
        '''
        # 获取当前文件的路径
        current_file_path = os.path.realpath(__file__)
        # print(current_file_path)

        # 当前文件所在的目录
        current_dir_path = os.path.dirname(current_file_path)
        # print(current_dir_path)

        current_project_path = os.path.dirname(current_dir_path)
        # print(current_project_path)
        return current_project_path + "\\"

# 测试一下getProjectPath的功能是否正确
# Path().getProjectPath()
