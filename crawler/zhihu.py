from selenium import webdriver
import time
import urllib.request
import re


# driver = webdriver.Chrome()
# # 打开百度首页
# driver.get('https://www.baidu.com')
# # 最大化窗口
# driver.maximize_window()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/question/29134042")

i = 0

while i < 10:
    # 下拉菜单拖到最底端
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        driver.find_element_by_css_selector('button.QuestionMainAction').click()
        print("page" + str(i))
        time.sleep(1)
    except:
        break

result_raw = driver.page_source
a = str(result_raw)
print(a)

# 正则匹配 貌似不怎么好用。。。。
content_list = re.findall("img src=\"(.+?)\" ", str(result_raw))

n = 0

while n < len(content_list):
    i = time.time()
    local = (r"./data/%s.jpg" % (i))
    urllib.request.urlretrieve(content_list[n], local)
    print("编号：" + str(i))
    n = n + 1

# 会有登录弹窗

