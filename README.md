### 환경정보공개시스템 
url: https://www.env-info.kr/member/open/companyTotalInfoSearch.do#

##환경설정
Package            Version
------------------ ---------
async-generator    1.10
attrs              22.1.0
beautifulsoup4     4.12.2
brotlipy           0.7.0
certifi            2022.9.24
cffi               1.15.1
charset-normalizer 3.3.2
cryptography       38.0.3
exceptiongroup     1.0.4
h11                0.14.0
idna               3.4
numpy              1.23.4
outcome            1.2.0
packaging          23.2
pandas             1.5.1
pip                22.3.1
pycparser          2.21
pyOpenSSL          22.1.0
PySocks            1.7.1
python-dateutil    2.8.2
python-dotenv      1.0.0
pytz               2022.6
requests           2.31.0
selenium           4.6.0
setuptools         65.5.1
six                1.16.0
sniffio            1.3.0
sortedcontainers   2.4.0
soupsieve          2.5
trio               0.22.0
trio-websocket     0.9.2
typing_extensions  4.4.0
urllib3            1.26.11
webdriver-manager  4.0.1
wheel              0.38.4
wsproto            1.2.0

##환경 설정 주의
chrome driver랑 google-chrome 버전이랑 맞춰줘야한다.

크롬 버전 확인 방법
google-chrome --version

크롬 드라이버 설치
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip


크롬 설치
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt-get install google-chrome-stable


120 버전은 webdriver_manager를 사용하기 어려워서
84버전으로 다운그레이드 해서 사용하려 했으나 이미 84버전의 드라이버를 설치했었어서 그냥 드라이버를 매핑해서 사용

크롤링 과정에서 
"selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:"와 같은 에러가 발생하여
driver.implicitly_wait(5)를 이용해 url이 켜진 후에 프로세스가 진행되도록 했음

class를 만들어 병렬처리를 하려 했으나 노트북 스팩이 좋아 불필요할거라 판단해 팻스


click버튼이 안먹힐때가 있었음 
"Message: element click intercepted: Element <button type="button" class="btn_cancel">...</button> is not clickable at point (337, 698)"대략 이런 메세지였음
    select10 = driver.find_element(By.XPATH, "/html/body/div/form[2]/div/div/div[1]/table/tbody/tr[5]/td/li[1]/div/a")
    driver.execute_script('arguments[0].click();', select10)
    위와 같은 코드로 처리해버림


