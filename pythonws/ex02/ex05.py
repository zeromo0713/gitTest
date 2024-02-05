def allArgs(data1, data2,*data3,data4='나는 기본 매개변수1',data5='나는 기본 매개변수2') :
    print(data1,data2,sep=" , ")
    print(data3)
    print(data4,data5,sep=" / ", end="\n\n===>")
    return data1,data2,data4,data5


#allArgs(10,20 )
#allArgs(10,20,30,40,50)
#allArgs(10,50,data4='바뀐 매개변수 1')
allArgs(data5='바뀐 매개변수2',data4="바뀐변수11",data2=500,data1=40000)
allArgs(40000,500,data4="순서대로1",data5='순서대로2')
allArgs(40000,500,80,40,"순서대로작성1",'순서대로작성22')

