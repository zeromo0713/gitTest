from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import re
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서


def scroll_down_to_bottom(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    print("===반복 전===", last_height)

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print("Scrolled!")
        time.sleep(1)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

options = Options()
options.add_argument('--start-maximized')
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get("https://search.shopping.naver.com/book/home")
driver.implicitly_wait(10)

# 스크롤 함수 호출 (driver를 인자로 전달)
scroll_down_to_bottom(driver)

# =========================================카테고리 목록 --> categori에 원하는 번호 입력===========================================================
# 1.소설, 2.시/에세이, 3.경제/경영, 4자기계발, 5.인문. 6.역사, 7.사회/정치, 8.자연/과학, 9.예술/대중문화, 10.종교, 11.유아, 12.어린이, 13.가정/요리 ,14.여행, 15.국어/외국어, 16.컴퓨터/IT, 17.청소년, 18.수험서/자격증, 19.만화
# ,20.잡지 , 21.외국도서 ,22.건강/취미, 23.고등학교 참고서, 24.중학교 참고서, 25.초등학교 참고서 , 26.중고도서]
categori = 9
#원하는 개수만큼 데이터 추출
read_num = 100

# 2번째 페이지(원하는 카테고리 페이지)로 이동
driver.find_element(By.CLASS_NAME,'category_list_category__DqGyx').find_element(By.CSS_SELECTOR,'li:nth-child({})'.format(categori)).click()
print("====여기는 오나===")
# 페이지 로딩을 기다림
time.sleep(3)  # 추가적인 로딩 시간이 필요한 경우, 더 긴 대기 시간으로 수정
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
    scroll_down_to_bottom(driver)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    list_all = soup.select('.list_book .bookListItem_item_book__1yCey')
    print("titles의 타입 ========>",type(list_all)) 
    print(len(list_all))
    for index, book in enumerate(list_all):
        list_obj = []
        #제목
        title = book.select_one('.bookListItem_title__X7f9_').text
        print(title)
        list_obj.append(title)
        #저자
        try:
            writer = book.select_one('div.bookListItem_detail__RBQ6x > div:nth-child(1) > span.bookListItem_define_data__kKD8t').text
            print(writer)
            list_obj.append(writer)
        except AttributeError as e:
            print("--저자 요소가 없심다--")
            list_obj.append(" ")
        #그림
        try:
            draw = book.select_one('div:nth-child(2) > span.bookListItem_define_data__kKD8t').text
            print(draw)
            list_obj.append(draw)
        except AttributeError as e:
            print("--그림 요소가 없심다--")
            list_obj.append(" ")
        #출판
        publish = book.select_one('div.bookListItem_define_item__LdTib.bookListItem_publish____VOP > div.bookListItem_detail_publish__FgPYQ > span.bookListItem_define_data__kKD8t').text
        print(publish)
        list_obj.append(publish)  
        #가격
        price = book.select_one('.list_book .bookListItem_item_book__1yCey > div > div > div:nth-child(1) > span > em').text
        print(price)
        list_obj.append(price)
        #e-book 가격
        try:
            ebook_price = book.select_one('.list_book .bookListItem_item_book__1yCey > div > div > div:nth-child(2) > span > em').text
            print(ebook_price)
            list_obj.append(ebook_price)
        except AttributeError as e:
            print("--ebook_price 요소가 없심다--")
            list_obj.append(" ")
        # 오디오북 가격
        try:
            audio_price = book.select_one('.list_book .bookListItem_item_book__1yCey > div > div > div:nth-child(3) > span > em').text
            print(audio_price)
            list_obj.append(audio_price)
        except AttributeError as e:
            print("--audio_price 요소가 없심다--")
            list_obj.append(" ")
        #순위
        try :    
            rank = book.select_one('.bookListItem_feature__txTlp').text
            print(rank)
            list_obj.append(rank)
        except AttributeError as e :
            print("--순위 요소가 없심다--")
            list_obj.append(" ")
        #날짜
        date = book.select_one('.bookListItem_detail__RBQ6x .bookListItem_detail_date___byvG').text
        print(date)
        list_obj.append(date)
        #평점
        try:
            grade = book.select_one('div.bookListItem_text_area__hF892 > div.bookListItem_grade__tywh2').text
            print(grade)
            list_obj.append(grade)
        except AttributeError as e:
            print("--평점 요소가 없심다--")
            list_obj.append(" ")

        total.append(list_obj)
        print("=====================================================")

        if len(total) >= read_num:
            break
print(len(total))
# 파일에 쓰기(csv파일에 저장)
if total:
    with open('책리스트{}.csv'.format(categori), 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        colList = '제목, 저자, 그림, 출판, 가격, e-book가격, 오디오북가격, 순위, 날짜, 평점'.split(', ')
        writer.writerow(colList)
        for row in total:
            writer.writerow(row)
else:
    print("데이터가 없습니다.")

time.sleep(2)
driver.quit()
