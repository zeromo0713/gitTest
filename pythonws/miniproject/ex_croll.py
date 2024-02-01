from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.keys import Keys # 키보드 입력을 위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


#원하는 개수만큼 데이터 추출
read_num = 300
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

time.sleep(5)


# 2번째 페이지(시/에세이 페이지)로 이동
driver.find_element(By.CLASS_NAME, 'category_list_category__DqGyx').find_element(By.CSS_SELECTOR, 'li:nth-child(2)').click()
print("====여기는 오나===")
# 페이지 로딩을 기다림
time.sleep(3)  # 추가적인 로딩 시간이 필요한 경우, 더 긴 대기 시간으로 수정
#driver.implicitly_wait(10)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
time.sleep(3)
print("====여기도 오나===")
print(driver.current_url)

#얻어온 데이터를 담을 빈 list 생성
total = []
# #원하는 개수만큼 데이터 추출    =====================================위에서 일단 먼저 입력=================================
# read_num = 160                =====================================위에서 일단 먼저 입력=================================

#1페이지에는 40개가 나오고, 60개를 얻어오기 위해선는 2페이지까지 가야하기 때문에 반복해준다
for i in range(1,read_num//40+2) :
    url = f"https://search.shopping.naver.com/book/search/category?bookTabType=ALL&catId=50005544&pageIndex={i}&pageSize=40"
    driver.get(url)
    time.sleep(2)
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    print(last_height)
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
    with open('책리스트.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        colList = '제목, 가격, 연도, 등수'.split(', ')
        writer.writerow(colList)
        for row in total:
            writer.writerow(row)
else:
    print("데이터가 없습니다.")



input()




