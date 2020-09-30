from poium import Page,PageElement,PageElements

class SaPage(Page):
    username=PageElement(id_="username",describe="用户名输入框")
    password=PageElement(css="[name='password']",describe="密码输入框")
    login_button=PageElement(xpath="//*[@class='table_logn']/tbody/tr[4]/td/input",describe="登录按钮")
    login_success_username=PageElement(xpath="/html/body/table/tbody/tr[1]/td/div/div[2]/div[1]/a[2]",describe="登录成功用户的登录名")
    loginout_button=PageElement(xpath="/html/body/table/tbody/tr[1]/td/div/div[2]/div[1]/a[8]",describe="登出按钮")
    loginout_sure=PageElement(xpath="/html/body/div[5]/div[2]/div[4]/a[1]/span/span",describe="确定登出")
    wrong_tips=PageElement(xpath="//*[@id='showError']/td/font",describe="登录账号或密码错误的提示")