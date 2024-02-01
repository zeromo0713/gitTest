import requests    #서버에 요청하는 것    html파일을 가져오는 것은 request객체
from bs4 import BeautifulSoup       #가져온 텍스트파일에서 데이터를 추출하는 것
# import time <= option이다. 다른 라이브러리로 대치(지연)할 수 있다

# time.sleep(5)  # 웹 크롤링에서는 서버에서 완전하게 데이터를 전달받을 수 있도록 지연시킬 필요가 있다.

useragentvalue = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# searchList = ['new','genre']     ===>이런식으로 공통부분을 찾아서 달라지는 곳만 알고 반복시키도록
# for search in searchList :    
#     url = 'https://comic.naver.com/webtoon?tab='+search
#     requests.get(url,headers=useragentvalue)

#url = 'https://comic.naver.com/index'   #이 페이지는 동적 페이지로 태그들이 자바스크립트를 통해 만들어지기에 selenium을 사용해야한다.
url = 'https://news.naver.com'
res = requests.get(url, headers=useragentvalue)
res.raise_for_status()  #request를 사용을 하면 반드시 사용해야하는 구문
soup = BeautifulSoup(res.text, 'lxml')
# with open('result.html','w',encoding='utf8') as htmlf:
#     htmlf.write(soup.get_text())
print("=========================================================================================")
print(soup.li)    # BeautifulSoup해서 불러온 데이터를 lxml을 통해 parsing 하여 soup.?의 해당하는 그(?) 태그에 해당되는 첫 번째 데이터를 가지고 온다.

seldiv = soup.find_all("div",attrs={'class':'cjs_news_tw'})# 첫 번째 매개변수는 tag
#seldiv = soup.select('div.cjs_news_tw')  #위와 같은 것을 선택한 방법을  select을 이용
print(seldiv)
for selData in seldiv :
    print("-----------**************************-------------")
#    print(selData.prettify())   # 태그들을 이쁘게 출력해주는것   (구조를 조금 더 명확히 볼 수 있다)

    print(type(selData))
    # titleInfo = selData.div.get_text()
    # conInfo = selData.p.get_text()
    eletitleInfo = selData.div
    eleconInfo = selData.p
    #titleInfo와 conInfo를  persistence(excel또는 DB 또는 textFile)에 저장한다.
    # print("titleInfo :", titleInfo)
    # print("conInfo :", conInfo)
    print("eletitleInfo 내용 :", eletitleInfo.get_text())
    print("eleconInfo con 내용 :", eleconInfo.get_text())
    print("elecon요소의 속성값 : ", eleconInfo['class'][0])

sellink = soup.a
print("&*&*&*&*&*&*&*&*&* : ",sellink['href'])  #a링크의 href속성을 볼 수 있다
print(type(sellink['href']))




