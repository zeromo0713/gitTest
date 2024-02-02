import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

SMTP_SERVER = "smtp.naver.com"
SMTP_PORT = 587
SMTP_USER = "각자 메일 아이디/ (아이디 주소)" #네이버 메일주소 
SMTP_PASSWORD = "각자 메일 비밀번호" #네이버 메일비밀번호

recvs = "dudah789@naver.com"  # 각자 받고싶은 곳으로(메일 보내고자 하는곳) 

msg =  MIMEMultipart()
msg["Subject"] = "제목" #제목
msg["From"] = SMTP_USER
msg["To"] = recvs

text = "테스트" #본문 텍스트

content = MIMEText(text)
msg.attach(content)

file_path = r'D:\zeromo\workspace\pythons\네이버북 인문50개.xlsx' #파일경로와 파일 이름 알아서 잘
with open(file_path,'rb') as f:
    attachment = MIMEApplication(f.read())
    attachment.add_header('Content-Disposition','attachment', filename = "네이버북 인문50개.xlsx") #파일이름 알아서 잘
    msg.attach(attachment)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.starttls()
s.login(SMTP_USER, SMTP_PASSWORD)
s.sendmail(SMTP_USER, recvs, msg.as_string())
s.quit


#메일보내는 코드
            #=====================예시==============================
# SMTP_SERVER = "smtp.naver.com"    #<= 구글이면 알아서 잘
# SMTP_PORT = 587     #  <==== 네이버 smtp 포트 주소, 구글은 알아서 찾아서
# SMTP_USER = "네이버 아이디" #네이버 메일주소  (아이디만 입력해도 됨)
# SMTP_PASSWORD = "네이버 비밀번호" #네이버 메일비밀번호

# recvs = "dudah789@naver.com" #받는 사람
# file_name = ''   #파일명

# msg =  MIMEMultipart()
# msg["Subject"] = "제목" #제목
# msg["From"] = SMTP_USER
# msg["To"] = recvs

# text = "테스트" #본문 텍스트

# content = MIMEText(text)
# msg.attach(content)

# file_path = r'D:\zeromo\workspace\pythonws\{}'.format(file_name) #파일경로
# with open(file_path,'rb') as f:
#     attachment = MIMEApplication(f.read())
#     attachment.add_header('Content-Disposition','attachment', filename = "{}".format(file_name)) #파일이름
#     msg.attach(attachment)

# s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# s.starttls()
# s.login(SMTP_USER, SMTP_PASSWORD)
# s.sendmail(SMTP_USER, recvs, msg.as_string())
# s.quit