import re #정규식 사용을 위해서는 re import 해주어야 함

# 정규식에서 .은 글자 한 개를 의미함   -> yang, yaag등 적용이됨 ynag는 안됨
# 정규식에서 ^ 는 시작을 의미함 -> (^young 라면 무조건 young로 시작해야 함)
# 정규식에서 $ 는 끝을 의미함
p = re.compile('ya.g') #괄호 안에 정규식 작성    -->정규식에서 .은 글자 한 개를 의미함   -> yang, yaag등 적용이됨 ynag는 안됨
print( type(p)) #**************어떤 타입으로 출력되는지를 먼저 알고****************
print(p)#************* 어떤 것이 출력되는지 확인 *****************
k = p.match("yangdoll")
print(k, "    /    " , type(k))
if k :
    print(k.group()) # 정규식에 맞는 단어를 출력 ,    실제 자료를 찍는 것은 group
    print(k.string) # 정규식에 테스트되는 단어를 출력 =>  yangdoll
    # print(k.start(),type(k.start()))
    # print(k.end(),type(k.end()))
    # print(k.span(),type(k.span()))# 위치값을 반환하는 메소드 k.start(), k.end(), k.span()
    startIndex , endIndex = k.span()
    print(startIndex)
else :
    print("주어진 단어는 일치하지 않습니다.")