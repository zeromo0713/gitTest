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
#wb는 webdriver




try :
    driver.get("https://naver.com")
    elem = driver.find_element(By.ID,'query')
    #elem = driver.find_elements("id",'query')   
    #elem = driver.find_element(By.XPATH,'//*[@id="query"]')
    elem.send_keys('선한피부')
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element(By.CLASS_NAME,('P7gyV'))
    elem.click()
    


    input()
except Exception as e :
    print(e)
finally:
    driver.quit()
