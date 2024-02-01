import requests   #서버에 요청하는 것    html파일을 가져오는 것은 request객체
from bs4 import BeautifulSoup       #가져온 텍스트파일에서 데이터를 추출하는 것
# import time <= option이다. 다른 라이브러리로 대치(지연)할 수 있다

useragentvalue = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


url = 'https://search.shopping.naver.com/search/all?adQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&frm=NVSHATC&origQuery=%EC%BB%B4%ED%93%A8%ED%84%B0&pagingIndex=4&pagingSize=40&productSet=total&query=%EC%BB%B4%ED%93%A8%ED%84%B0&sort=price_asc&timestamp=&viewType=list'
res = requests.get(url, headers=useragentvalue)
res.raise_for_status()  #request를 사용을 하면 반드시 사용해야하는 구문
soup = BeautifulSoup(res.text, 'lxml')
#print(soup.prettify())

pricelist = soup.select('span.price')
#pricelist = soup.select('span.price_num__S2p_v')
print("=======================")
print(type(pricelist))
print(pricelist)
for price in pricelist :
    pricelow = price.span
    # print("pricelow의 타입 :",type(pricelow))
    print("pricelow 내용 :", pricelow.get_text())
    # print("price의 타입 :",type(price))


