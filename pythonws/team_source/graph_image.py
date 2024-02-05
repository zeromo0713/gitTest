from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
from openpyxl.drawing.image import Image 
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

options = Options()

# #최대 화면 조건
# options.add_argument('--start-maximized')
# # 화면 꺼짐 방지 조건
# options.add_experimental_option("detach", True)
# # 불필요한 에러메세지 제거 조건
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 이전 스크롤 위치 초기화
last_height = browser.execute_script("return document.body.scrollHeight")



url = f'https://search.shopping.naver.com/book/home'
browser.get(url)
time.sleep(2)

actions = browser.find_element(By.TAG_NAME,'body')
# 무한 루프로 페이지의 끝까지 스크롤
while True:
    actions.send_keys(Keys.END) 
    time.sleep(0.5)
    # 현재 스크롤 위치 가져오기
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # 스크롤이 더 이상 되지 않으면 루프 종료
    # 이전 스크롤 위치 업데이트
    last_height = new_height
    
#카테고리
    #카테고리 마저도 자동화 가능
elem = browser.find_element(By.CLASS_NAME, 'category_list_category__DqGyx')
categorylist = elem.text.split('\n')
print('_'*30,'이하 카테고리 목럭입니다.', '_'*30)
print(categorylist)
print('_'*80)
print('원하는 카테고리를 <<위의 카테고리 종류>>를 참조하여 입력해주세요(복사붙여넣기)')
inputCategory = input()
xpathIdx = int(categorylist.index(inputCategory))+1
print('xpathIdx===>', xpathIdx)
xpath = '//*[@id="container"]/div/div[11]/div/ul/li[{}]/a'.format(xpathIdx)
print('xpath====>', xpath)
    #elem 덮어쓰기
elem = browser.find_element(By.XPATH, xpath)
getUrlExcPage = elem.get_attribute('href')
    #그냥 클릭하면 새로운 탭으로 연결되기 때문에 href 속성 값을 전부 변경 시킴
browser.execute_script('''
    var elements = document.querySelectorAll(".category_link_category__XlcyC");
    elements.forEach(function(element) {
        element.setAttribute("target", "_self");
    });
''')
time.sleep(1)
elem.click()
time.sleep(1)

print('='*50,'원하는 데이터의 갯수를 입력해주세요', '='*50)
dataNum = int(input())
datalist = []

wb = Workbook()
ws = wb.active
ws.title = "{}".format(inputCategory)
ws.append(["제목","가격","발행일","순위"])


for i in range(1,(dataNum//41)+2):
    getUrl = getUrlExcPage+'&pageIndex={}&pageSize=40'.format(i)
    browser.get(getUrl)
    time.sleep(2)
    actions = browser.find_element(By.TAG_NAME,'body')
    # 무한 루프로 페이지의 끝까지 스크롤
    while True:
        actions.send_keys(Keys.END) 
        time.sleep(0.5)
        # 현재 스크롤 위치 가져오기
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
             break  # 스크롤이 더 이상 되지 않으면 루프 종료
        # 이전 스크롤 위치 업데이트
        last_height = new_height

    price_elements = browser.find_elements(By.CSS_SELECTOR, '.bookPrice_price__zr5dh>em')
    name_elements = browser.find_elements(By.CSS_SELECTOR, '.bookListItem_title__X7f9_')
    published_date_elements = browser.find_elements(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
    rank_elements = browser.find_elements(By.CSS_SELECTOR, '.bookListItem_feature__txTlp')

    for  name,price, date, score in zip(name_elements, price_elements, published_date_elements, rank_elements):
            
            published_date_text = date.get_attribute('textContent').strip()
            price_text = int(price.get_attribute('textContent').replace(',',''))
            name_text = name.get_attribute('textContent').strip()
            rank_text = score.get_attribute('textContent').strip()
        
            datalist.append(name_text)#가져온 문자열을 리스트에 추가(java는 push)
            ws.append([name_text ,price_text , published_date_text, rank_text]) 
           
            if len(datalist) >= dataNum:
                break   
efilename = '네이버북 {}{}개'.format(inputCategory.replace('/', '_'), dataNum)      
wb.save('{}.xlsx'.format(efilename))




plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# Load the Excel file into a DataFrame

data = pd.read_excel('{}.xlsx'.format(efilename))

# Create subplots with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot the scatter plot for book prices
price = data['가격'].sort_values(ascending=True)
axes[0].scatter(x=range(len(price)), y=price)
axes[0].set_xlabel('권 수')
axes[0].set_ylabel('가격')
axes[0].set_title('소설({}) 가격'.format(inputCategory.replace('/', '_')))

# Convert '발행일' to datetime format
data['발행일'] = pd.to_datetime(data['발행일'], errors='coerce')

# Extract only the year from the '발행일' column
data['연도'] = data['발행일'].dt.year

# Plot the count plot for publication years
sns.countplot(x='연도', data=data, ax=axes[1])
axes[1].set_xlabel('연 도')
axes[1].set_ylabel('권 수')
axes[1].set_title('소설({}) 발행일'.format(inputCategory.replace('/', '_')))

# Adjust layout
plt.tight_layout()
plt.savefig('그래프.jpg',format='jpeg')

ws1 = wb.create_sheet('그래프')
img = Image('그래프.jpg')
ws1.add_image(img,'A1')
wb.save('{}.xlsx'.format(efilename))
            