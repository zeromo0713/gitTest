from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import time

options = Options()
#최대 화면 조건
options.add_argument('--start-maximized')
#화면 꺼짐 방지 조건
options.add_experimental_option("detach",True)
#불필요한 에러메세지 제거 조건
options.add_experimental_option("excludeSwitches",["enable-logging"])

driver = wb.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
#wb는 webdriver
driver.get("https://naver.com")
elem = driver.find_element(By.ID,'query')
#elem = driver.find_elements("id",'query')   
#elem = driver.find_element(By.XPATH,'//*[@id="query"]')
elem.send_keys('쿠팡')
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.CLASS_NAME,('link_name'))
elem.click()



elem = driver.find_element(By.ID, 'headerSearchKeyword')
time.sleep(2)
elem.send_keys("피아노")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#headerSearchBtn').click() #elem.send_keys(Keys.ENTER)
# # search = driver.find_element(By.ID,'headerSearchKeyword')

# # #elem.click()
# # search.send_keys('피아노')
# # search.send_keys(Keys.RETURN)

input()



