from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.keys import Keys # 키보드 입력을 위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains  #일반적인 상황에서 클릭이나 이러한 동작들이 작동을 안할 때 더 면밀하게 찾아주기 위해서
# from selenium.webdriver.support.ui import Select # Select Box를 컨트롤 하기 위해 ==> 클릭으로 컨트롤이 되지 않을 때
# from selenium.webdriver.support.select import Select
import os  #운영체제 일단 임포트
import csv #엑셀 파일(csv파일) 을 열고 데이터를 저장하기 위해서
import time
import re #편하게 쓰기 위한 formatting 방식

options  = Options()

#화면이 켜지고 최대화면이 되도록
options.add_argument('--start-maximized')
#화면이 꺼지는것을 막는 것(True로 했을 경우)
options.add_experimental_option("detach",True)
#화면에 불필요한 에러메시지가 나오는 것을 막기 위함
options.add_experimental_option("excludeSwitches",["enable-logging"])

#옵션이 들어간 크롬을 driver라는 변수에 담아놓음
driver = webdriver.Chrome(options=options)

driver.get("https://search.shopping.naver.com/book/home")
driver.implicitly_wait(10)

#스크롤 하기 전 높이 구하기
last_height = driver.execute_script("return document.documentElement.scrollHeight")
print("===반복 전===",last_height)


# =========================================카테고리 목록 --> categori에 원하는 번호 입력===========================================================
# 1.소설, 2.시/에세이, 3.경제/경영, 4자기계발, 5.인문. 6.역사, 7.사회/정치, 8.자연/과학, 9.예술/대중문화, 10.종교, 11.유아, 12.어린이, 13.가정/요리 ,14.여행, 15.국어/외국어, 16.컴퓨터/IT, 17.청소년, 18.수험서/자격증, 19.만화
# ,20.잡지 , 21.외국도서 ,22.건강/취미, 23.고등학교 참고서, 24.중학교 참고서, 25.초등학교 참고서 , 26.중고도서]
categori = 5
#원하는 개수만큼 데이터 추출
read_num = 30
#스크롤 내리는 것을 함수로 정의
def scroll_down_to_bottom():
    #스크롤 하기 전 높이 구하기
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    print("===반복 전===",last_height)
    #스크롤의 전체 높이가 내린 후의 높이와 같을 때 까지 계속 내리기
    while True :
        #스크롤 끝까지 내리기
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print("Scrolled!")
        #스크롤 내린 후 페이지 로딩 시간 필요
        time.sleep(1)

        #스크롤 내린 후 페이지 높이
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        
        #더이상 스크롤이 내려가지 않을 때 까지 스크롤 내리는 반복문 멈추기
        if new_height == last_height :
            break
        #스크롤 내린 후 페이지 높이를 현재 페이지 높이 변수에 저장
        last_height = new_height
#스크롤 끝까지 내리기
scroll_down_to_bottom()

time.sleep(2)


# 2번째 페이지(원하는 카테고리 페이지)로 이동
driver.find_element(By.CLASS_NAME, 'category_list_category__DqGyx').find_element(By.CSS_SELECTOR, 'li:nth-child({})'.format(categori)).click()
print("====여기는 오나===")
# 페이지 로딩을 기다림
time.sleep(3)  # 추가적인 로딩 시간이 필요한 경우, 더 긴 대기 시간으로 수정
#driver.implicitly_wait(10)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
time.sleep(3)
print("====여기도 오나===")
print(driver.current_url)

current_url = driver.current_url
# 정규표현식을 사용하여 "http://"부터 "&pageIndex=1&pageSize=40"전까지의 부분 추출
match = re.search(r'(https://.+?&catId=\d+)', current_url)
#match가 있다면 (url이 저기까지 일치한다면) 주소를 가져와서, base_url에 담는다.
if match:
    base_url = match.group(1)
    # 결과 출력 또는 변수에 저장
    print("Base URL:", base_url)
    url = base_url+"&pageIndex=2&pageSize=40"
    print(url)


#얻어온 데이터를 담을 빈 list 생성
total = []
#1페이지에는 40개가 나오고, 60개를 얻어오기 위해선는 2페이지까지 가야하기 때문에 반복해준다
for i in range(1,read_num//40+2) :
    url = base_url+"&pageIndex={}&pageSize=40".format(i)
    driver.get(url)
    time.sleep(2)
    scroll_down_to_bottom()

    titles = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[1]/span')
    prices = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/div/div/span/em')
    grades = driver.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')
    dates = driver.find_elements(By.CLASS_NAME,'bookListItem_detail__RBQ6x .bookListItem_detail_date___byvG')


   
    for index,(title, price, grade, date_element) in enumerate(zip(titles, prices, grades, dates)):
        list_obj = []
        list_obj.append(title.text)
        list_obj.append(price.text)
        list_obj.append(grade.text)
        list_obj.append(date_element.text)
        print(list_obj,"===================")
        total.append(list_obj)
        if index >= len(titles) - 1 :  # 더이상 얻어올 데이터가 없으면 계속 반복을 진행하고
            continue
    if len(total) >= read_num : # 총 자료가 원하는개수인 read_num개가 된다면 반복을 그만한다
        break
        
print("실행되는가")
print(len(total))
print(driver.current_url)

    
       

# 파일에 쓰기(csv파일에 저장)
if total:
    with open('책리스트{}.csv'.format(categori), 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        colList = '제목, 가격, 등수, 연도'.split(', ')
        writer.writerow(colList)
        for row in total:
            writer.writerow(row)
else:
    print("데이터가 없습니다.")

time.sleep(2)




