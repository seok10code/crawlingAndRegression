from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd


service = ChromeService("/mnt/c/Users/김석원/Desktop/python_script/chromedriver")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=chrome_options)

df = pd.read_csv('/mnt/c/Users/김석원/Desktop/python_script/url_list.csv', encoding='cp949')

investment_cost = []
for idx, items in df.iterrows():

    driver.get(items['url'])
    select10 = driver.find_element(By.XPATH, "/html/body/div/form[2]/div/div/div[1]/table/tbody/tr[5]/td/li[1]/div/a")
    driver.execute_script('arguments[0].click();', select10)
    result_sum = 0
    # make text from html
    html = driver.page_source
    soup = bs(html, 'html.parser')
    print(idx)
    if soup.select('#inquiry10 > table > tbody >tr'):
        num = str(soup.select('#inquiry10 > table > tbody > tr > td.last')).count('만원')
        for i in range(0,num):
            if soup.select(f'#inquiry10 > table > tbody > tr:nth-child({((4*i)+2)}) > td.last'):
                result_sum += float(soup.select(f'#inquiry10 > table > tbody > tr:nth-child({((4*i)+2)}) > td.last')[0].text.split(' ')[0].replace(',',''))
        investment_cost.append(result_sum*1000000)
    else:
        investment_cost.append(None)
    print(result_sum)
    print('-'*70)
df['investment_cost'] = investment_cost

df.to_csv('/mnt/c/Users/김석원/Desktop/python_script/result.csv', encoding='cp949')
# 확인용 저장파일
# with open('/mnt/c/Users/김석원/Desktop/python_script/test.txt', 'w') as file:    
#     file.write(str(soup))  

















