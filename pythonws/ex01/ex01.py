
print('hello zeromo')
print(20+5)

if 20>30:
    print(True)
else:
    print(False)

for i in range(10):  #range는 범위    0부터 세서 10개를 출력
    #print(i)
    print(i + 1)

a = '영모'
print(a)
a = 30
print(a)
b = 'print a 다음 문자열임'
print(b)
#파이썬의 문자열 나타내는 법은 싱글따옴표, 더블따옴표, 싱글 또는 더블따옴표 3개 -> 여러줄  (자바스크립트에서 ``(백틱)과 똑같음 )

#h = int(input("숫자 입력 해보기"))
h = 34
if h > 50:
    print("50보다 크면 실행")
elif h < 20:
    print("20보다 작으면 실행")
else:
    print("50과 같거나 작고, 20과 같거나 크면 실행")

#while 1 :
#   print(120) 
    
# ctrl + c 눌러서 무한 반복에서 빠져나오기
    

k = 120
print (type(k))
if( type(k) == int):
    print("숫자입니당")
else : 
    print("숫자가 아닙니당")


print("======또 다른 방법==========")

j = '120'
if type("") == type(j):
    print("문자(string)이어유")

c = len("나는 바로 영모다")
#c=len(120)     int에서는 len 기능 안됨,, str(string)에서만 지원
print(c)

p=len((129,25))  #각각의 자료는 int이지만 묶여져있기 때문에 (tuple)형 이기에 결과값 2가 나온다  ===> 묶여져있는 것은 개수를 셀 수 있다
print(p)

print("나의 살던 고향은"[1])
print("나의 살던 고향은"[1:])
print("나의 살던 고향은"[:1])
print("나의 살던 고향은"[0:2])
print("나의 살던 고향은"[1:5])
print("나의살던고향은"[::2])
print("나의살던고향은"[0:5:3])
print("나의살던고향은"[-7:])
print("나의살던고향은"[-7::2])

s = 'show how to index into sequences'.split()
print(s, type(s))
print(s[3])
print(s[:3])
print(s[::2])
print(s[1::2])
print(s[0][3])


basicStr = "나의살던고향은"
print(id(basicStr), "=>" , basicStr)
print("="*50)
print("나"+"는"+"영모당")
#print("영모의 파이썬" + 12) 타입이 다르기에 에러가 나옴
print("영모의 파이썬"+"12")
print("영모의 파이썬"+str(12))
print(id("빵모"))  # id는 메모리상의 주소
print(id(basicStr), id("나의살던고향은") ,"<===========")
print(id(120)==id(120))
print(id(basicStr)== id("나의살던고향은") ,"<===========")


