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

print("======",last_height)
print("&*&*&*&*&*",new_height)
# driver.find_element(By.XPATH,'//*[@id="lnb"]/div/div/ul/li[12]/a').click()

# elem = driver.find_element(By.CLASS_NAME,'category_list_category__DqGyx')
# elem.find_element(By.CSS_SELECTOR,'li:nth-child(1)').click()
# driver.find_element(By.CLASS_NAME,'category_list_category__DqGyx').find_element(By.CSS_SELECTOR,'li:nth-child(2)').click()
# time.sleep(5)



# 2번째 페이지로 이동
driver.find_element(By.CLASS_NAME, 'category_list_category__DqGyx').find_element(By.CSS_SELECTOR, 'li:nth-child(2)').click()
print("====여기는 오나===")
# 페이지 로딩을 기다림
time.sleep(3)  # 추가적인 로딩 시간이 필요한 경우, 더 긴 대기 시간으로 수정
#driver.implicitly_wait(10)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동
time.sleep(3)
print("====여기도 오나===")
print(driver.current_url)
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

print(" 다 내려감 ")
print("======2번째 페이지 반복 후=====",last_height)
print("&*&*&*&*&*",new_height)

# elems = driver.find_elements(By.CLASS_NAME,'bookListItem_item_book__1yCey .bookListItem_text__bglOw')
# for elem in elems :
#     print(elem.text)

#elems = driver.find_elements(By.CLASS_NAME,'bookListItem_info_top__VgpiO linkAnchor .bookListItem_text__bglOw')
titles = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[1]/span')
prices = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/div/div[1]/span')
#dates = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[3]/div[2]/div[2]') #==> 이거로 하니 중간에 div 하나가 추가되는 부분이 있어서 40개를 못가져옴
grades = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[2]')
dates = driver.find_elements(By.CLASS_NAME,'bookListItem_detail__RBQ6x .bookListItem_detail_date___byvG')


total = []
# for title, price, grade, date_element in zip(titles, prices, grades, dates):
#     list_obj = []
#     list_obj.append(title.text)
#     list_obj.append(price.text)
#     list_obj.append(grade.text)
#     list_obj.append(date_element.text)
#     print(list_obj,"===================")
#     total.append(list_obj)


for index,(title, price, grade, date_element) in enumerate(zip(titles, prices, grades, dates)):
    list_obj = []
    list_obj.append(title.text)
    list_obj.append(price.text)
    list_obj.append(grade.text)
    list_obj.append(date_element.text)
    print(list_obj,"===================")
    total.append(list_obj)
    if index >= len(titles) - 1 :
        driver.find_element(By.XPATH,'//*[@id="container"]/div[2]/div[1]/div/div[3]/a[2]').click()

print("===============1페이지 제발 으악==================")
print(list_obj)
print("===============1페이지 제바아아아아아알 으악==================")
print(total)
print(len(titles))
print(len(prices))
print(len(dates))
print(len(grades))




print("=============================2페이지====================================")
#2페이지 다시 시작
time.sleep(4)
print(driver.current_url,"=====> 2페이지여야함")
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
prices = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/div/div[1]/span')
#dates = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[3]/div[2]/div[2]') #==> 이거로 하니 중간에 div 하나가 추가되는 부분이 있어서 40개를 못가져옴
grades = driver.find_elements(By.XPATH,'//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[2]')
dates = driver.find_elements(By.CLASS_NAME,'bookListItem_detail__RBQ6x .bookListItem_detail_date___byvG')
for index,(title, price, grade, date_element) in enumerate(zip(titles, prices, grades, dates)):
    list_obj = []
    list_obj.append(title.text)
    list_obj.append(price.text)
    list_obj.append(grade.text)
    list_obj.append(date_element.text)
    print(list_obj,"===================")
    total.append(list_obj)
    if len(total) >= 60 :
        break
    # if index >= 20 :
    #     break

print("===============2페이지 제발 으악==================")
print(list_obj)
print("===============2페이지 제바아아아아아알 으악==================")
print(total)


# for title in titles :
#     print(title.text)
# print("&*&*&*&*&*&*&*&*&*&**&")
# for price in prices :
#     print(price.text)
# print("&*&*&*&*&*&*&*&*&*&**&")
# for date in dates :
#     print(date.text)
# print("&*&*&*&*&*&*&*&*&*&**&")
# for grade in grades :
#     print(grade.text)
# list_item = []
# for elem in elems :
#     print(elem.text)
#     list_item.append(elem.text)
# print(type(list_item))
# print(list_item)
# print("========================================")
print(len(titles))
print(len(prices))
print(len(dates))
print(len(grades))
print(len(total))

print(total[0])
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&%&%&%&%&%&%&")
print(total[1])


# total 리스트 초기화 및 데이터 수집 코드 ...

# 파일에 쓰기
if total:
    with open('랭킹상위60리스트.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in total:
            writer.writerow(row)
else:
    print("데이터가 없습니다.")
# f = open('랭킹상위60리스트.csv','w',encoding='utf-8-sig')
# writer = csv.writer(f,delimiter=',')

# for i in total.__len__ :
#     writer.writerow(total[i])




input()





