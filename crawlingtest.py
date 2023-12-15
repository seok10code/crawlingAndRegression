from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd

def parserUrl(year, compId, custId):
    url = f"https://www.env-info.kr//user/register/viewUserSearch2.do?YEAR={year}&COMP_ID={compId}&CUST_ID={custId}&OPEN_YN=Y"
    return url


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
service = ChromeService("/mnt/c/Users/김석원/Desktop/python_script/chromedriver")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=chrome_options)


# driver.get('https://www.env-info.kr/member/open/companyTotalInfoSearch.do')
driver.get('https://www.env-info.kr/member/open/companyTotalInfoSearch.do#')
# 유형을 제조로 클릭
driver.find_element(By.XPATH, '//*[@id="schCompDiv"]/option[2]').click()
# 기준연도 2009년 클릭
driver.find_element(By.XPATH, '//*[@id="schYear"]/option[15]').click()
# 페이지 200개씩 클릭
driver.find_element(By.XPATH, '//*[@id="pageRows"]/option[6]').click()

# 검색버튼 클릭
search= driver.find_element(By.XPATH, '//*[@id="env_contents"]/div[2]/table/tbody/tr[2]/td[2]/a')
driver.execute_script('arguments[0].click();', search)








# make text from html
html = driver.page_source
soup = bs(html, 'html.parser')

# 확인용 저장파일
with open('/mnt/c/Users/김석원/Desktop/python_script/test12223.txt', 'w') as file:    
    file.write(str(soup))                    
        


cnt=0

# 9,13,201


url_list = []
compy_list = []
for k in range(0,9):
    for j in range(3, 13):
        for i in range(1,201):
            cnt+=1
            if (cnt > 14432):
                break
            else:
                # value = soup.select(f'#tblDocList > tbody > tr:nth-child({i}) > td:nth-child(7) > a')[0].get('onclick').split('(')[1].split(')')[0].split(',')
                # year_ag = value[0][1:-1]
                # compId_ag = value[1][1:-1]
                # custId_ag = value[2][1:-1]
                compy_list.append(soup.select(f'#tblDocList > tbody > tr:nth-child({i}) > td:nth-child(5)')[0].text)
                # url_list.append(parserUrl(year_ag, compId_ag, custId_ag))
                print(cnt)
        if (cnt > 14432):
            break
        else:
            next_page = driver.find_element(By.XPATH, f'//*[@id="pageViewer1"]/a[{j}]')
            driver.execute_script('arguments[0].click();', next_page)

    if (cnt > 14432):
        break

    else:
        next_area = driver.find_element(By.XPATH, '//*[@id="pageViewer1"]/a[13]/img')
        driver.execute_script('arguments[0].click();', next_area)


df = pd.DataFrame({'cp_name':compy_list})

df.to_csv('/mnt/c/Users/김석원/Desktop/python_script/cmpy_list.csv', encoding='cp949')






