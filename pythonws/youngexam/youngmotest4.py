from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
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

#오피넷이라는 주유소관련 사이트를 가져와서 driver에 담아놓았다.
driver.get("https://www.hira.or.kr/main.do")
#화면을 열고 10초간 기다리도록 한다.
driver.implicitly_wait(10)

#메인화면에서 비급여 진료비 정보 클릭
driver.find_element(By.XPATH,'//*[@id="shortcut01"]/ul/li[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="uuid-1j"]/a').click()

#비급여 진료비용 상세 검색 창과 팝업창 지우기
driver.find_element(By.XPATH,'//*[@id="uuid-tj"]/div/div/div/div[1]/div').click()
driver.find_element(By.XPATH,'//*[@id="uuid-tm"]/div/a/div[1]').click()

#지역 중 경기 를 입력하기 위함
driver.find_element(By.XPATH,'//*[@id="uuid-ip"]/div/div[1]').click()
driver.find_element(By.XPATH,'//div[@id=\'pt-ip/i7\']/div').click()

#지역 중 화성시를 입력하기 위함
driver.find_element(By.XPATH,'//*[@id="uuid-iq"]/div/div[2]').click()
driver.find_element(By.XPATH,'//div[@id=\'pt-iq/i44\']/div').click()



#지역 중 반송동을 입력하기 위함
driver.find_element(By.XPATH,'//*[@id="uuid-ir"]/div/div[2]').click()
driver.find_element(By.XPATH,'//div[@id=\'pt-ir/i10\']/div').click()


input()