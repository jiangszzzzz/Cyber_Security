from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

## 配置的chromedriver
# def getDriver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-gpu")
#     # options.add_argument("--no-sandbox") # linux only
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     driver = webdriver.Chrome(options=options)
#     driver.execute_cdp_cmd("Network.enable", {})
#     driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#         "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#                 get: () => undefined
#             })
#         """
#     })
#     return driver


driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://www.baidu.com")
driver.get("https://www.dcard.tw/f")

# search = driver.find_element_by_name("wd")
# search.send_keys("美女")
# search.send_keys(Keys.RETURN)

# search = driver.find_element(by=By.NAME, value="wd")
# search = driver.find_element(by=By.ID, value="kw")

search = driver.find_element(by=By.NAME, value="query")
search.clear()
search.send_keys("美女")
search.send_keys(Keys.RETURN)

# 页面跳转需要时间
# time.sleep(10)

# 等最多10s，直到 ID  myDynamicElement 出现 不好用。。。。
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "j38qb8-1"))
# )
i = 0
while i < 10:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    i += 1

time.sleep(1)

# 查找网页中元素 按class name
titles = driver.find_elements(by=By.CLASS_NAME, value="sc-d28862ca-3")
for title in titles:
    print(title.text)

time.sleep(5)
driver.quit()
