import readExcel
login_xls = readExcel.readExcel().get_xls('login_info.xlsx', 'sa')
class RunConfig:
    # 运行测试用例的目录或文件
    cases_path="./test_dir/"
    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type="chrome"
    #配置url
    url=login_xls[1][0]

    #失败重跑次数
    rerun="0"

    #最大失败数，到达则停止执行
    max_fail="5"

    #浏览器驱动(不需要修改)
    driver=None

    #报告路径(不需要修改)
    NEW_REPORT=None

    #用户名
    username=login_xls[1][1]
    #姓名
    true_name=login_xls[1][2]
    #密码
    password=str(int(login_xls[1][3]))
    #错误的密码
    wrong_password=str(int(login_xls[1][4]))