from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#최대 화면 조건
options.add_argument('--start-maximized')
#화면 꺼짐 방지 조건
options.add_experimental_option("detach",True)
#불필요한 에러메세지 제거 조건
options.add_experimental_option("excludeSwitches",["enable-logging"])

driver = wb.Chrome(options=options)
#wb는 webdriver
driver.implicitly_wait(10)
#10초동안 기다리기

driver.get("Https://naver.com")
time.sleep(5)
#input() #터미널 창에 어떠한 명령을 받게 되면 input을 적어두고 터미널창에서 엔터키를 치면 브라우저가 닫힌다. => 계속 꺼지면 작업확인이 어렵기에 프로젝트 만들기가 완료되면 input을 없애주면 된당ㅎㅎ


try :
    driver.get("https://news.naver.com/main/ranking/popularDay.naver")
    elems = driver.find_elements("class name","rankingnews_box")

    for elem in elems:
        name = elem.find_element("class name", "rankingnews_name")
        tex = elem.find_element("class name", "rankingnews_list")
        #print(elem.text,' ')
        print(tex.text, end='')

    input()
except Exception as e :
    print(e)
finally:
    driver.quit()