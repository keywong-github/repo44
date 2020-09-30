import os
from config import RunConfig
import pytest
from selenium import webdriver

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
REPORT_DIR=BASE_DIR+"/test_report/"

'''
function 测试函数、用例前后
class 测试类前后
module 每个.py文件一次
session 多个文件调用一次，可以跨多个.py,每个.py就是每个module
'''




#定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    return RunConfig.url
#用户名
@pytest.fixture(scope='function')
def username():
    return RunConfig.username
#用户姓名
@pytest.fixture(scope='function')
def true_name():
    return RunConfig.true_name
#密码
@pytest.fixture(scope='function')
def password():
    return RunConfig.password
#错误的密码
@pytest.fixture(scope='function')
def wrong_password():
    return RunConfig.wrong_password


#启动浏览器
@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()
    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver


#关闭浏览器
@pytest.fixture(scope="session",autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")