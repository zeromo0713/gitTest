import os
from selenium import webdriver # seleniium 라이브러리에서 webdriver을 임포트한다  
from selenium.webdriver.chrome.options import Options # 웹드라이버에서 크롬을 사용할 것이다
from selenium.webdriver.common.by import By #element(요소)들을 찾기 위해서
from selenium.webdriver.common.action_chains import ActionChains  #일반적인 상황에서 클릭이나 이러한 동작들이 작동을 안할 때 더 면밀하게 찾아주기 위해서
from selenium.webdriver.support.ui import WebDriverWait # Select Box를 컨트롤 하기 위해 ==> 클릭으로 컨트롤이 되지 않을 때
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import pyperclip
import openpyxl # 엑셀을 열기 위함
import re #편하게 쓰기 위한 formatting 방식 (정규식)
import time # 시간을 지정하기 위해서(기다리는 것)

options  = Options()

#화면이 켜지고 최대화면이 되도록
options.add_argument('--start-maximized')
#화면이 꺼지는것을 막는 것(True로 했을 경우)
options.add_experimental_option("detach",True)
#화면에 불필요한 에러메시지가 나오는 것을 막기 위함
options.add_experimental_option("excludeSwitches",["enable-logging"])

#옵션이 들어간 크롬을 driver라는 변수에 담아놓음
driver = webdriver.Chrome(options=options)

#네이버 사이트를 가져와서 driver에 담아놓았다.
driver.get("https:/www.naver.com")
#화면을 열고 10초간 기다리도록 한다.
driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()

# =====> pyperclip 사용예제
# # 클립보드로 텍스트 복사
# pyperclip.copy("안녕하세요, Pyperclip!")

# # 클립보드에서 텍스트 붙여넣기
# text = pyperclip.paste()
# print(text)  # 출력: 안녕하세요, Pyperclip

#네이버 자동 로그인
my_id = "dudah789"
my_pwd = "dladudah123!"
pyperclip.copy(my_id)
driver.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')
pyperclip.copy(my_pwd)
driver.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
driver.find_element(By.ID,'log.login').click()

#메일 함 들어가는 작업
driver.find_element(By.XPATH,'//*[@id="account"]/div[2]/div/div/ul/li[1]').click()
driver.find_element(By.XPATH,'//*[@id="account"]/div[3]/div[2]/div[1]/a').click()
print(driver.current_url)
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동    메일은 새로운 탭이 열리기에 탭 이동을 해준다
print(driver.current_url)
time.sleep(7)

#일단 내게쓰기 한 후 엑셀 업로드 후 메일 보내기
driver.find_element(By.XPATH,'//*[@id="root"]/div/nav/div/div[1]/div[2]/a[2]').click()
time.sleep(1)
#driver.find_element(By.CLASS_NAME,'button_upload').click()


# 엑셀 파일 경로
excel_file_path =  r'D:\zeromo\workspace\pythonws\책리스트.csv'
# 파일 업로드
file_input = driver.find_element(By.ID, 'ATTACH_LOCAL_FILE_ELEMENT_ID')
file_input.send_keys(os.path.abspath(excel_file_path))

# 첨부한 파일이 업로드될 때까지 대기
wait = WebDriverWait(driver, 10)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'file_upload_progress')))

driver.find_element(By.CLASS_NAME,'button_write_task').click()




input()