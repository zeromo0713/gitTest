import openpyxl

path = 'C:\\Users\\임영모\\OneDrive\\바탕 화면\\아아.xlsx'


wb = openpyxl.load_workbook(path)
ws = wb.active
# wb.create_sheet('second')
ws.title = '변경된쉬이트'



ws = wb['변경된쉬이트']

aa = ['영모','이등','삼등','사등','오등','이건','리스트']
aaa = [['일등','이등','삼등','사등','오등','이건','리스트']]
print(type(aaa))
ws.append(aa)
#ws.append(aaa)    #append는 시트를 지정해주어야 사용이 가능하다.












wb.save(path)