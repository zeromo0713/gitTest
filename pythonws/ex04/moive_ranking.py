from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다 (크롬에 있는 옵션을 사용할 것이다) 
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.action_chains import ActionChains  #일반적인 상황에서 클릭이나 이러한 동작들이 작동을 안할 때 더 면밀하게 찾아주기 위해서
#from selenium.webdriver.support.ui import Select # Select Box를 컨트롤 하기 위해 ==> 클릭으로 컨트롤이 되지 않을 때
#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import openpyxl # 엑셀을 열기 위함
import re #편하게 쓰기 위한 formatting 방식
import time # 시간을 지정하기 위해서(기다리는 것)

options  = Options()

#화면이 켜지고 최대화면이 되도록
options.add_argument('--start-maximized')
#화면이 꺼지는것을 막는 것(True로 했을 경우)
options.add_experimental_option("detach",True)
#화면에 불필요한 에러메시지가 나오는 것을 막기 위함
options.add_experimental_option("excludeSwitches",["enable-logging"])

#옵션이 들어간 크롬을 driver라는 변수에 담아놓음
driver = webdriver.Chrome(options=options)

driver.get('https://www.imdb.com/')
driver.find_element(By.ID,'imdbHeader-navDrawerOpen').click()

time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span').click()

time.sleep(3)


title = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a/h3')
print('&*&*&*&*&*',title.text)

movie_list = []
elems = driver.find_elements(By.CSS_SELECTOR,'.ipc-title__text.ipc-title__text')
for elem in elems :
    movie_list.append(elem.text)

print("===============",movie_list)
print("===============길이 : ",len(movie_list))
input()
