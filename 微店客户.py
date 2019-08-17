# pip安装selenium、pyquery，下载chromedriver放到python目录下，新建环境变量
# VS Code里安装code runner，文件>首选项>配置>python.linting.pylintArgs里增加pylint
from selenium import webdriver
from pyquery import PyQuery
import time

# 身份信息
pho="15611231586"
psd="20170324syzg"

# 打开谷歌浏览器，等待5秒
driver = webdriver.Chrome()
time.sleep(2)

# 打开微店首页网址
driver.get("https://www.weidian.com/?from=baidu-biaoti")
time.sleep(2)

# 最大化窗口，获取窗口位置
driver.maximize_window()
print(driver.get_window_position())

# 找到登录按钮并单击
driver.find_element("class","login").click()