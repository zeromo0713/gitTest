import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

SMTP_SERVER = "smtp.naver.com"
SMTP_PORT = 587
SMTP_USER = "dudah789" #네이버 메일주소
SMTP_PASSWORD = "dladudah123" #네이버 메일비밀번호

recvs = "dudah789@naver.com"

msg =  MIMEMultipart()
msg["Subject"] = "제목" #제목
msg["From"] = SMTP_USER
msg["To"] = recvs

text = "테스트" #본문 텍스트

content = MIMEText(text)
msg.attach(content)

file_path = r'D:\gwonys\workspace\pythons\네이버북 인문50개.xlsx' #파일경로
with open(file_path,'rb') as f:
    attachment = MIMEApplication(f.read())
    attachment.add_header('Content-Disposition','attachment', filename = "네이버북 인문50개.xlsx") #파일이름
    msg.attach(attachment)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.starttls()
s.login(SMTP_USER, SMTP_PASSWORD)
s.sendmail(SMTP_USER, recvs, msg.as_string())
s.quit