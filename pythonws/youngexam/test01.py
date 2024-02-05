import gspread
from oauth2client.service_account import ServiceAccountCredentials

test = ['http://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('test2.json',test)

gs = gspread.authorize(credentials)
# 위에는 api 연동 과정

doc = gs.open_by_url('https://docs.google.com/spreadsheets/d/1J-tYTHVTkaqD9d-SzXz0r-YN4EOAJAXt-UwOaYfe0iE/edit#gid=0')
ws = doc.get_worksheet(0) 
# 만들어진 워크시트와 연동

val = ws.acell('C2').value
print(val)

val = ws.row_values('1')
print(val)

val = ws.col_values('1')
print(val)

vals = ws.range('A2:C4')
print(type(vals) , "========리스트 타입으로 밑의 문장은 향상된 for문(forEach 느낌으로 출력)========")
for val in vals:
    print(val.value)

val = ws.update_acell('B1','나이') #엑셀에 있는 값을 바꿔주는 것



