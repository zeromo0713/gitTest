from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.keys import Keys # 키보드 입력을 위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
# from selenium.webdriver.common.action_chains import ActionChains  #일반적인 상황에서 클릭이나 이러한 동작들이 작동을 안할 때 더 면밀하게 찾아주기 위해서
# from selenium.webdriver.support.ui import Select # Select Box를 컨트롤 하기 위해 ==> 클릭으로 컨트롤이 되지 않을 때
# from selenium.webdriver.support.select import Select
import os  #운영체제 일단 임포트
import csv #엑셀 파일(csv파일) 을 열고 데이터를 저장하기 위해서
import time
import re #편하게 쓰기 위한 formatting 방식
import pandas as pd
import openpyxl
import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
import matplotlib.pyplot as plt
from io import BytesIO
import warnings
import pyperclip
import openpyxl # 엑셀을 열기 위함
import re #편하게 쓰기 위한 formatting 방식 (정규식)
import time # 시간을 지정하기 위해서(기다리는 것)

# 들어간 py파일  = croll.py - excel_croll.py(csv) - graph_filter.py - send_mail.py

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
categori = 10
#원하는 개수만큼 데이터 추출
read_num = 100
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

print("실행되는가")
print(len(total))
print(driver.current_url)

    
       

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

#===============================================================================================================================================================
#===============================================================================================================================================================
#===========================================크롤링 후 csv 파일 저장 하는 것 까지==================================================================================
#===============================================================================================================================================================
#===============================================================================================================================================================



# 합칠 엑셀 파일 이름
output_excel_name = '통합파일.xlsx'

# 폴더 내 모든 CSV(확장파일) 파일에 대해 반복
csv_folder_path =  r'D:\zeromo\workspace\pythonws' # ========================파일경로는 각자 경로===============================
csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]   # f.endswith('.csv')여기 부분  확장파일 csv파일 말고 xlsx등 변경 가능

with pd.ExcelWriter(output_excel_name, engine='xlsxwriter') as writer:
    for idx, csv_file in enumerate(csv_files, start=1):    # idx와 enumerate 을 붙여서 인덱스 번호를 부여해준다 ㅎ.ㅎ
        # CSV 파일을 읽어옴
        current_csv_path = os.path.join(csv_folder_path, csv_file)

        # CSV 파일을 데이터프레임으로 읽어옴
        df = pd.read_csv(current_csv_path)

        # 원하는 컬럼만 선택
        selected_columns = ['제목', '가격']
        df = df[selected_columns]

        # 엑셀 시트 이름을 현재 파일의 이름과 결합하여 저장
        sheet_name = f"시트{idx}_{os.path.splitext(csv_file)[0]}"  #여기의 시트{idx}_이 부분 때문에 특수문자 복잡해짐..
        df.to_excel(writer, sheet_name=sheet_name, index=False)

time.sleep(2)

#===============================================================================================================================================================
#===============================================================================================================================================================
#===========================================csv파일 저장 후 원하는 컬럼 추출하여 엑셀 파일에 시트별 저장============================================================
#===============================================================================================================================================================
#===============================================================================================================================================================




# 경고 메시지 무시 설정      ====> 경고가 계속 나와서 일단 무시하고 넘어가기 위해서 적용해보았으요
# warnings.simplefilter(action='ignore', category=FutureWarning)

# 그래프에 한글이 깨지는 것을 방지해줌   ==> 그래프에 한글이 깨지면 글씨 부분이 ㅁㅁ이런식으로 네모로 나와버린다
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 또는 엑셀 파일을 Pandas DataFrame으로 읽기
file_path = '통합파일.xlsx'
# sheet_name=None으로 설정하여 모든 시트를 읽습니다.
df_dict = pd.read_excel(file_path, sheet_name=None)

# 엑셀 파일에 이미지 추가
#위 코드에서는 mode='a'로 설정하여 기존 엑셀 파일에 이미지를 추가합니다. 또한 writer.book을 사용하지 않고 excel_writer.sheets를 직접 활용하여 이미지를 추가합니다
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as excel_writer:
    for sheet_name, df in df_dict.items():
        # '가격' 컬럼을 숫자로 변환 (천 단위 쉼표 제거)
        df['가격'] = df['가격'].replace(r'[\$,]', '', regex=True).astype(float)

        # '가격대' 컬럼을 추가하여 가격대별로 그룹화
        bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, float('inf')]  # 가격대 구간 설정
        labels = ['0-5000', '5000-10000', '10000-15000', '15000-20000', '20000-25000', '25000-30000', '30000+']
        df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels, right=False)

        # 가격대별 빈도를 막대 그래프로 시각화
        price_groups = df.groupby('가격대').size()

        # 그래프 설정
        fig, ax = plt.subplots()
        ax.bar(price_groups.index, price_groups.values, color='skyblue')

        # 그래프에 추가 설명 넣기
        ax.set_title(f'{sheet_name} - 가격대별 상품 수')  # 그래프 제목
        ax.set_xlabel('가격대')  # x축 레이블
        ax.set_ylabel('상품 수')  # y축 레이블

        # 가격대 별 권수 표시
        for i, v in enumerate(price_groups.values):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

        # 총 권수 표시
        total_books = price_groups.sum()
        ax.text(len(price_groups) / 2, max(price_groups.values) + 1, f'총 권수: {total_books}', ha='center', va='bottom')

        # 그래프를 이미지로 저장
        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        plt.close()

        # BytesIO에서 파일로 저장
        image_stream.seek(0)
        
        # 특수문자 제거하여 시트 이름 정의
        clean_sheet_name = re.sub(r'\W+', '', sheet_name)
        
        image_path = f'{clean_sheet_name}_그래프.png'
        with open(image_path, 'wb') as img_file:
            img_file.write(image_stream.read())

        # 이미지 삽입
        img = openpyxl.drawing.image.Image(image_stream)
        img.width = 400  # 이미지의 가로 크기 조정
        img.height = 300  # 이미지의 세로 크기 조정
        img.anchor = 'K2'  # 이미지를 원하는 위치에 삽입
        img.title = f'{sheet_name}_그래프'  # 이미지 제목 설정
        excel_writer.sheets[clean_sheet_name].add_image(img)

time.sleep(2)

#===============================================================================================================================================================
#===============================================================================================================================================================
#===========================================각 시트별 그래프 만들어서 넣기========================================================================================
#===============================================================================================================================================================
#===============================================================================================================================================================



#네이버 사이트를 가져와서 driver에 담아놓았다.
driver.get("https:/www.naver.com")
#화면을 열고 10초간 기다리도록 한다.
driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()

# =====> pyperclip 사용예제
# # 클립보드로 텍스트 복사
# pyperclip.copy("안녕하세요, Pyperclip!")

# # 클립보드에서 텍스트 붙여넣기
# text = pyperclip.paste()
# print(text)  # 출력: 안녕하세요, Pyperclip

#네이버 자동 로그인
my_id = "네이버 아이디"      #=================================각자의 메일 아이디 비밀번호 =======================================
my_pwd = "네이버 비밀번호!"    #=================================각자의 메일 아이디 비밀번호 =======================================
pyperclip.copy(my_id)
driver.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')
pyperclip.copy(my_pwd)
driver.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
driver.find_element(By.ID,'log.login').click()

#메일 함 들어가는 작업
driver.find_element(By.XPATH,'//*[@id="account"]/div[2]/div/div/ul/li[1]').click()
driver.find_element(By.XPATH,'//*[@id="account"]/div[3]/div[2]/div[1]/a').click()
print(driver.current_url)
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동    메일은 새로운 탭이 열리기에 탭 이동을 해준다
print(driver.current_url)
time.sleep(7)

#일단 내게쓰기 한 후 엑셀 업로드 후 메일 보내기
driver.find_element(By.XPATH,'//*[@id="root"]/div/nav/div/div[1]/div[2]/a[2]').click()
time.sleep(1)
#driver.find_element(By.CLASS_NAME,'button_upload').click()


# 엑셀 파일 경로
excel_file_path =  r'D:\zeromo\workspace\pythonws\통합파일.xlsx'  # ==================================각자의 파일 경로==============================
# 파일 업로드
file_input = driver.find_element(By.ID, 'ATTACH_LOCAL_FILE_ELEMENT_ID')
file_input.send_keys(os.path.abspath(excel_file_path))

# 첨부한 파일이 업로드될 때까지 대기
wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'file_upload_progress')))

driver.find_element(By.CLASS_NAME,'button_write_task').click()


#===============================================================================================================================================================
#===============================================================================================================================================================
#===========================================완성된 엑셀 파일 네이버 메일로  나에게 보내기===========================================================================
#============================================이 부분은 네이버 로그인 하면 등록이 나오는 경우도 있는데 나는 나오지 않아서 몰랐심다..====================================
#============================================등록 부분을 추가 하거나, 메일 보내는 과정을 페이지로 띄우지 않고 하도록==================================================
#============================================ 네이버 메일로 한 이유는 멋져보여서 헤헤^^============================================================================
#=====================================================이것으로 사용하면 빠릅니다 ㅎ.ㅎ=============================================================================
                # SMTP_SERVER = "smtp.naver.com"    #<= 구글이면 알아서 잘
                # SMTP_PORT = 587     #  <==== 네이버 smtp 포트 주소, 구글은 알아서 찾아서
                # SMTP_USER = "네이버 아이디" #네이버 메일주소  (아이디만 입력해도 됨)
                # SMTP_PASSWORD = "네이버 비밀번호" #네이버 메일비밀번호

                # recvs = "dudah789@naver.com" #받는 사람
                # file_name = ''   #파일명

                # msg =  MIMEMultipart()
                # msg["Subject"] = "제목" #제목
                # msg["From"] = SMTP_USER
                # msg["To"] = recvs

                # text = "테스트" #본문 텍스트

                # content = MIMEText(text)
                # msg.attach(content)

                # file_path = r'D:\zeromo\workspace\pythonws\{}'.format(file_name) #파일경로
                # with open(file_path,'rb') as f:
                #     attachment = MIMEApplication(f.read())
                #     attachment.add_header('Content-Disposition','attachment', filename = "{}".format(file_name)) #파일이름
                #     msg.attach(attachment)

                # s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                # s.starttls()
                # s.login(SMTP_USER, SMTP_PASSWORD)
                # s.sendmail(SMTP_USER, recvs, msg.as_string())
                # s.quit
#===============================================================================================================================================================
#===============================================================================================================================================================

time.sleep(5)   # ===> 5초 있다가 인터넷도 닫아버리장 ^o^


#굉장히 설치하고 업그레이드 한 것이 많아요..
#다 외우지는 못했으나.. 나중에 생각나는대로,, 그리고 앞으로 프로그램 할 때 필요한 업그레이드나 다운로드 받는것은 그때그때 적어두는 것으로 = ^o^ =






