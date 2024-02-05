import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive',
         'https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('test2.json',scope)

gs = gspread.authorize(credentials)

doc = gs.create('글로벌직업전문학교')

ws = doc.get_worksheet(0)

for i in range(5):
    ws.append_row([i,str(i) + 'data'])

doc.share('dladudah@gmail.com',perm_type='user', role='reader')