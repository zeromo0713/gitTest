import requests

url = 'https://blog.naver.com/pigyo123/221482849508'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'} #딕셔너리 형태로 지정, 기계가 접속하는 것이 아닌, 크롬을 통해 접속하는 것으로 속인다         
res_data = requests.get(url, headers=headers)  # ==> 이 작업을 통해 거부하지 않는다(접근금지를 풀어주도록)

res_data.raise_for_status()  # 에러가 발생하면 exception을 발생시키며 바로 프로그램을 종료시키도록

# 효과적인 크롤링 위해서는 정규표현식을 사용할 줄 알아야 한다.
#res_data = requests.get(url)  # 이렇게만 사용하면 경우에 따라 접근금지(403에러)가 발생할 수 있다.(크롤링을 못하도록 차단) 이유는 hearder 값이 다르기에
# print(res_data.status_code)
# if res_data.status_code == requests.codes.OK :
#     print("정상적으로 처리되는 내용이 여기에 들어감")
#     pass
# else : 
#     print("크롤링 실패!!! 권한이 없심더")

#======================>정적인 문서에 대해서 크롤링 할 때는 selenium 쓰지 말고 requests와 beautiful 사용하는 것이 성능이 더 좋음
