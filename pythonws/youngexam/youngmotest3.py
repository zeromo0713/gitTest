from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.action_chains import ActionChains  #일반적인 상황에서 클릭이나 이러한 동작들이 작동을 안할 때 더 면밀하게 찾아주기 위해서
from selenium.webdriver.support.ui import Select # Select Box를 컨트롤 하기 위해 ==> 클릭으로 컨트롤이 되지 않을 때
from selenium.webdriver.support.select import Select
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
driver.get("https://www.opinet.co.kr/user/main/mainView.do")
#화면을 열고 10초간 기다리도록 한다.
driver.implicitly_wait(10)

#오피넷 홈페이지에서 강원버튼을 클릭하려는데 그냥 클릭하면 클릭이 되지 않는다.
#=>  ActionChains를 활용하여 클릭을 할 수 있도록 하고 그에 맞는 문법 사용
elem = driver.find_element(By.XPATH,'//*[@id="m_42"]/span[1]')
actions = webdriver.ActionChains(driver).click(elem)
actions.perform()

#강원을 클릭한 후 강원도 평균과 전국 평균을 출력하여준다
gangwonPriceAvg = driver.find_element(By.XPATH,'//*[@id="sido_price1"]/span[1]').text
totalPriceAvg = driver.find_element(By.XPATH,'//*[@id="oilcon1"]/div/dl[1]/dd/span[1]').text
print("강원도 평균 :",gangwonPriceAvg)
print("전국 평균 : ", totalPriceAvg)


#체크박스에서 '춘천시'를 선택하기 위해 select하기에 select라이브러리를 이용하여 작용
#두 번째 체크박스에서 '저가순' 을 선택하도록 하고  select하기에 select라이브러리를 이용하여 작용
cityBox = driver.find_element(By.XPATH,'//*[@id="selected1"]')
priceSeqBox = driver.find_element(By.XPATH,'//*[@id="selected2"]')
select = Select(cityBox)
select.select_by_visible_text('춘천시')
select = Select(priceSeqBox)
select.select_by_visible_text('저가순')

#저가순으로 나온 주유소들을 출력하기 위해 선택을 한다
#주유소 리스트들을 보여주는 창인 tbody는 하나이기에 element를 사용하고
#각각의 주유소들을 나타내기 위해서는 tbody(gasStationList)안에 여러개가 있기에 elements를 사용하였다.
# ./tr/td/a 이렇게 잡은 이유는 ./가  현재 경로를 의미하며 , 저 밑으로 있는 것들을 찾는다는 뜻에서 사용한다
gasStationList = driver.find_element(By.XPATH,'//*[@id="os_t1"]/tbody')
gasStationtexts = gasStationList.find_elements(By.XPATH,'./tr/td/a')




workbook = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\새 폴더\\통합 문서1.xlsx')
sheet = workbook['Sheet1']
sheet['B1'] = totalPriceAvg
sheet['B2'] = gangwonPriceAvg
workbook.save('C:\\Users\\user\\Desktop\\새 폴더\\통합 문서1.xlsx')

i=1
for stationName in gasStationtexts:
    print(stationName.text)
    sheet['D'+str(i)] = stationName.text
    i=i+1
workbook.save('C:\\Users\\user\\Desktop\\새 폴더\\통합 문서1.xlsx')


#하나를 눌러서 지도를 나오도록 한다
driver.find_element(By.XPATH,'//*[@id="os_t1"]/tbody/tr[1]/td[2]/a').click()

#팝업창이 뜬 것을 x표시를 눌러서 없애준다
driver.find_element(By.XPATH,'//*[@id="os_dtail_info"]/div[3]/a/img').click()


gasStationBox = driver.find_element(By.XPATH,'//*[@id="body1"]') #모든것을 감싸는 body
# staName= gasStationBox.find_elements(By.XPATH,'./tr/td/a') # 주유소명
# oilPrice = gasStationBox.find_elements(By.XPATH,'./tr/td') # 휘발유값
# gasPrice = gasStationBox.find_elements(By.XPATH,'./tr/td/font') # 경유값





stationList = gasStationBox.find_elements(By.XPATH,'./tr')   # <==이렇게 하면 이미지까지 그림으로 나옴..

print("======================")

print("======================")

i=1
for station in stationList:
    print(station.text)
    sheet['F'+str(i)] = station.text
    i=i+1
# i=1
# for station in stationList:
#     print(station.text)
#     print("*&*&*&*&*&*&*&*&*&*&*&")
#     print(station.find_element(By.XPATH,'//*[@id="body1"]/tr['+str(i)+']/td[1]/a').text)
#     sheet['F'+str(i)] = station.text
#     i=i+1

    
workbook.save('C:\\Users\\user\\Desktop\\새 폴더\\통합 문서1.xlsx')

input()