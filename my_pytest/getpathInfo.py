import os

def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]  #切割后，0是当前文件的上一级，1是当前文件
    print(os.path.realpath(__file__))
    return path

if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())