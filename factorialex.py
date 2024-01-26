def fact(n):
    if(n > 1 ):
        return n* fact(n-1)
    return 1

print( " 3! => ", fact(3))
print( " 4! => ", fact(4))
print( " 5! => ", fact(5))
print( " 6! => ", fact(6))


#재귀호출 === 자기가 자기를 부르는 것
# 재귀호출은 알고리즘 중 가장 기본적인 부분
# 추가 되는지


