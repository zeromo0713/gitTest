from selenium import webdriver   #webdriver을 통해  작업을 할 것이고
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


# Options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
browser = webdriver.Chrome() # 웹 드라이버는 크롬을 사용하겠다   --> 크롬 브라우저를 통해 데이터를 가져오기 위해 ,  # webdriver.Chrome() -=> 크롬을 동작 시키는 것(브라우저를 동작시는것)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})  #검색을 눌렀을 때 막아놓은 것을 뚫는 역할
browser.get("https://www.coupang.com/")
#browser.page_source()  # ==>  https://www.coupang.com/의 요소(자바 스크립트가 동작하고 최종적으로 만들어진 것)가 들어가있다  (페이지 소스 X)



elem = browser.find_element(By.XPATH,'//*[@id="headerSearchKeyword"]')
time.sleep(3)
elem.send_keys("고구마")
time.sleep(2)
browser.find_element(By.CSS_SELECTOR,'#headerSearchBtn').click()    # 검색 버튼을 클릭 , browser는 홈  //elem.send_keys(Keys.ENTER)로 써주어도 된다
#browser.find_element(By.XPATH,'//*[@id="headerSearchKeyword"]').send_keys("고구마").send_keys(Keys.ENTER)
#16라인부터 20라인까지 하나의 명령으로 만듬(네트워크 상황이나 속도문제로 인해 동작하지 않을 수도 있다)


browser.find_element(By.XPATH,'//*[@id="searchSortingOrder"]/ul/li[2]/label').click()  # 바뀐 홈페이지에서 낮은 가격을 클릭  ==>  browser는 고구마 검색 후 (현재 켜진 브라우저)
#여기까지가 자료를 얻고자 하는 페이지

#현재 페이지에서 데이터 추출이 완료된다면
 #1. beautifulsoup을 이용   <==browser.page_source
 #2. browser.get을 새롭게 해서현재 url을 가져오는 방법

titles = []
prices = []
arrive_date = []
# 빈 list(배열)들을 url 위로 올리는 이유는 url의 페이지에 변화에 따라 for문이 올 수도 있기에 위로 빼놓는다
url = 'https://www.coupang.com/np/search?rocketAll=false&searchId=422c964b13354ee9a2129951cf0b21ca&q=%EA%B3%A0%EA%B5%AC%EB%A7%88&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=87570&component=&rating=0&sorter=salePriceAsc&listSize=36'
browser.get(url)
elems = browser.find_elements(By.CSS_SELECTOR,'.search-product .name')
print(len(elems))

for index , elem in enumerate(elems) :    #enumerate로 하면 tuple을 반환하여 인덱스를 먼저 반환하고, 원래 들어있는 요소를 꺼내와서 반복해준다. *반복하는데 인덱스가 필요하다면enumerate로 감싸게 하면 된다 *
    if index >= 12 :
        break
    #print(elem.text)
    titles.append(elem.text)


elems = browser.find_elements(By.CSS_SELECTOR,'.search-product .sale')
for index , elem in enumerate(elems) :    #enumerate로 하면 tuple을 반환하여 인덱스를 먼저 반환하고, 원래 들어있는 요소를 꺼내와서 반복해준다. *반복하는데 인덱스가 필요하다면enumerate로 감싸게 하면 된다 *
    if index >= 12 :
        break
    #print(elem.text)
    prices.append(elem.text)

elems = browser.find_elements(By.CSS_SELECTOR,'.search-product .arrival-info')
for index , elem in enumerate(elems) :    #enumerate로 하면 tuple을 반환하여 인덱스를 먼저 반환하고, 원래 들어있는 요소를 꺼내와서 반복해준다. *반복하는데 인덱스가 필요하다면enumerate로 감싸게 하면 된다 *
    if index >= 12 :
        break
    #print(elem.text)
    arrive_date.append(elem.text)

print(titles, '\n',prices,'\n',arrive_date)

input()


# time.sleep(5)
# #browser.quit()    #모든 탭을 종료
# browser.close()   #브라우저의 현재 탭(프로그램으로 열은 탭)을 종료
# #browser.page_source()  # 페이지의 요소(자바 스크립트가 동작하고 최종적으로 만들어진 것)를 가져오는 것
# time.sleep(5)







