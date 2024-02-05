a=[[2,5]]*3
print(a)
a[0].append(7)
print(a)
print("="*30)
b = [[2,5]]* 3
print(b)
b = [[2,5,7]]*3
print(b)

a = [1,5,5,3,6,7,0,1,2]
print(a.count(5))
print(a.count(0))

b = ["서울","수원","부산","오산","서울","병점"]
print(b.count("서울"),"<===========")

m = "나는 파이썬을 잘하고 싶다".split()
print(m)
m.sort(key=len)
print(m)
m.sort(reverse=True)
print(m)
print(m[2])
print("="*30)
y = sorted(m)
