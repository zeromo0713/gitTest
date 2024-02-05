import csv

f = open("C:\\Users\\user\\Desktop\\텍스트.txt", 'r',encoding='UTF8')
# ff = f.readline()
# fff = ff.split()
# print(fff)
firstline = []
secondline = []
thirdline = []
totalline = []
while True:
    line = f.readline()
    if not line: break
    print(line)
    sep_line = line.split()
    print("======",sep_line )
    totalline.append(sep_line)
f.close()
print("=======",totalline,"=========")
print(type(totalline))


firstline.append(totalline[0])   # 리스트 하나로 묶어버리기
secondline.append(totalline[1])  # 리스트 하나로 묶어버리기
thirdline.append(totalline[2])   # 리스트 하나로 묶어버리기

print(type(firstline),"&*&*",firstline)
print(type(secondline),"&*&*",secondline)
print(type(thirdline),"&*&*",thirdline)

# firstline[0].splitd


