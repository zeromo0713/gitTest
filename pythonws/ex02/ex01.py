#tuple  사용법,      특징을 잘 알고, 응용하고 사용할 줄 알아야 함
def minmax(data):
    return min(data),max(data)

(minNum, maxNum) = minmax([1,11,25,3,6,9,48,72,66])

print('가장 작은 숫자 : {0} 입니다'.format(minNum))
print('가장 큰 숫자 : {0} 입니다'.format(maxNum))
print("========================================")
a = '감자'
b = '고구마'
print(a , '   ' ,b)

# 전통적인 언어싀 swap방식
c = a 
a = b 
b = c
print(a , '   ' ,b)

#파이썬에서 제공하는 tuple을 이용한 바로  swap가능
c='사과'
d='복숭아'
(c,d)=(d,c)
print(c , '   ' ,c)

numData = 1,2,3,4,5
#numData[0] = 10   #튜플이기 때문에 직접 변경 불가능
imsi = list(numData)
imsi[0] = 10 #리스트로 타입을 바꿔주었기에 타입 볍경 가능
numData = tuple(imsi)
print(numData, type(numData)) 

list(numData)[1]=20
#================================
#파이썬은 기본적으로 복소수를 지원한다. 복소수 사칙연산법 알아두고 정리해두기 기억해두기 
complexDataA = 2 + 3j
complexDataB = 2 + 3j
completxAddResult= complexDataA + complexDataB # 복소수 더하기는 실수 부분과 헣수 부분들을 따로 더함 (2+2) + (3+;)
print("복소수 결과 : " , completxAddResult)