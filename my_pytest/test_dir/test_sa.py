import sys
from time import sleep
from os.path import dirname,abspath
sys.path.insert(0,dirname(dirname(abspath(__file__))))
from page.sa_login_page import SaPage
from selenium import webdriver

import pytest

class TestSaLogin:
    '''
    登录操作
    '''
    #@pytest.mark.skip
    def test_sa_login_case01_success(self,browser,base_url,username,true_name,password):  #,brower,base_url
        ''' 
        sa登录成功
        '''
        #driver=webdriver.Chrome()
        browser.implicitly_wait(10)
        page=SaPage(browser)
        page.get(base_url)
        page.username=username
        page.password=password
        page.login_button.click()
        sleep(5)
        assert page.login_success_username.text==true_name
        page.loginout_button.click()
        page.loginout_sure.click()

    #@pytest.mark.skip
    def test_sa_login_case02_no_usename(self,browser,base_url,password):  #,brower,base_url
        ''' 
        登录名为空
        '''
        #driver=webdriver.Chrome()
        browser.implicitly_wait(10)
        page=SaPage(browser)
        page.get(base_url)
        page.password=password
        page.login_button.click()
        sleep(1)
        alert=browser.switch_to.alert
        alert_text=alert.text
        print(alert_text)
        assert alert_text=="请输入登录名！"
        alert.accept()
        
    #@pytest.mark.skip
    def test_sa_login_case03_no_password(self,browser,base_url,username):  #,brower,base_url
        ''' 
        密码为空
        '''
        #driver=webdriver.Chrome()
        browser.implicitly_wait(10)
        page=SaPage(browser)
        page.get(base_url)
        page.username=username
        page.login_button.click()
        sleep(2)
        alert=browser.switch_to.alert
        alert_text=alert.text
        assert alert_text=="请输入密码！"
        alert.accept()

    #@pytest.mark.skip
    def test_sa_login_case04_no_all(self,browser,base_url):  #,brower,base_url
        ''' 
        账号、密码为空
        '''
        #driver=webdriver.Chrome()
        browser.implicitly_wait(10)
        page=SaPage(browser)
        page.get(base_url)
        page.login_button.click()
        sleep(1)
        alert=browser.switch_to.alert
        alert_text=alert.text
        assert alert_text=="请输入登录名！"
        alert.accept()

    #@pytest.mark.skip
    def test_sa_login_case05_wrong(self,browser,base_url,username,wrong_password):  #,brower,base_url
        ''' 
        账号密码不正确
        '''
        #driver=webdriver.Chrome()
        browser.implicitly_wait(10)
        page=SaPage(browser)
        page.get(base_url)
        page.username=username
        page.password=wrong_password
        page.login_button.click()
        sleep(1)
        assert page.wrong_tips.text=="错误提示：用户名或密码错误，请重新输入！"
        #alert.accept()

#python -m pytest -sv
#python run_tests.py -m run  -m不能在.py前面