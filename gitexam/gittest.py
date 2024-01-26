import openpyxl

workbook = openpyxl.load_workbook('C:\\Users\\user\\Desktop\\새 폴더\\입력하나만.xlsx')

ws = workbook.active

list_data = ['나는영모',27,98]
ws.append(list_data)

workbook.save('C:\\Users\\user\\Desktop\\새 폴더\\입력하나만.xlsx')