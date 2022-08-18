from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tsj.tw/")

# 瓜 <https://www.youtube.com/watch?v=r60JmZcAoi8&ab_channel=%E7%91%A9%E7%9C%9F%E5%BE%8B%E5%B8%AB>

blow = driver.find_element(by=By.ID, value="click")
blow_count = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

item1 = list()
item1.append(
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))
item1.append(
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
item1.append(
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))

item2 = list()
item2.append(driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
item2.append(driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
item2.append(driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))

for i in range(1000000):
    # # 创建时需要传递参数 执行所有动作
    actions = ActionChains(driver)
    actions.click(blow)
    actions.perform()
    count = int(blow_count.text.replace("您目前擁有", '').replace("技術點", ''))
    # print(blow_count.text.replace("您目前擁有",'').replace("技術點",''))
    for j in range(3):
        price = int(item2[j].text.replace("技術點", ''))
        if count >= price:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item1[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break
