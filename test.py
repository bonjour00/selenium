# 引入 selenium 的 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化 webdriver 並開啟瀏覽器
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("http://localhost:9000/#/")
# 等待一段時間讓頁面載入結果
time.sleep(1)
driver.get("http://localhost:9000/#/ChatRoom")
time.sleep(1)
message_button = driver.find_element(By.ID, 'messageQ')
message_button.send_keys("資管系")
message_button.send_keys(Keys.ENTER)
time.sleep(3)

pending_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[1]/div/button[1]/span[2]/div/i')
pending_button.click()
time.sleep(1)

edit_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/button[1]/span[2]/i')
edit_button.click()
time.sleep(1)

editAnswer_button = driver.find_element(By.ID, 'qedit')
editAnswer_button.send_keys("資管系")
time.sleep(1)
editOk_button = driver.find_element(By.ID, 'editOK')
editOk_button.click()
time.sleep(2)
delete_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/button[2]/span[2]')
delete_button.click()
time.sleep(1)
deleteroom_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[1]/div/button[3]/span[2]')
deleteroom_button.click()
time.sleep(1)
recover_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/button[1]/span[2]/i')
recover_button.click()
time.sleep(1)
driver.get("http://localhost:9000/#/manage")
time.sleep(3)
page_button = driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div[2]/div/div/div[3]/div/div/div/div/button[2]/span[2]')
page_button.click()
time.sleep(3)
# expected_url = "http://localhost:3000/"
# assert driver.current_url == expected_url, "未正常登出"

# 關閉瀏覽器
driver.quit()