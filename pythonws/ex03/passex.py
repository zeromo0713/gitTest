import sys
import requests  #웹과 연동하고자 할 때 기본적으로 필요한 라이브러리   (beutifulSoup를 사용할 땐 requests를 먼저 사용해야함)
# a = 20
# if a > 20 :
#     pass
# else :
#     pass
# print(a)
# pass를 활용하여 if문 for문 등 큰 구성과 흐름을 가지고 안에 내용은 나중에 작성
# 어떤 결과를 도출할 지 알고 있기

a = 50
if a > 20 :
    sys.exit()
else :
    pass
print(a)

# 텍스트 파일(exfile01.txt, exfile02.txt)에 '안녕하세요'라는 내용을 저장하시오
# 2가지 방법으로 각각 저장하기

f = open('exfile01.txt','w',encoding='utf-8')
f.write("안녕하세요")
f.close()



with open('exfile02.txt','w') as ff :
    ff.write("안녕하셔유")