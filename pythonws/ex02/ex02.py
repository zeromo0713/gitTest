# listData = [["alice" , [10,20,30]],["bob", [10,25,35]]]
# dictData = dict(listData)
# print(dictData)

# basicDick = {
#     'alice' : {'국어': 100, 
#                '영어' : 20 , 
#                '수학' : 80},
#     'bob' :{'국어': 40, 
#             '영어' : 50 , 
#             '수학' : 30},
# }

# print(basicDick)


listDickData = [ ["alice", dict([['국어' , 100],['영어' , 20 ],['수학' , 80]])],
                 ["bob", dict([['국어', 100],['영어',  20 ],['수학' , 80]]) ] ]
            
listDickData.append( ["young", dict([['국어', 100],['영어',  20 ],['수학' , 80]]) ] )
result = dict(listDickData)
print(type(listDickData))
print(type(result))
print(result)