import os
from selenium import webdriver
from bs4 import BeautifulSoup
import argparse
import csv

# 폴더 만들기
if not os.path.exists('./naver_login'):
    os.makedirs('./naver_login')

# 네이버 로그인
driver = webdriver.Chrome('C:/Users/korea/Desktop/NAVER/chromedriver')

# 들어가기
driver.get('https://nid.naver.com/nidlogin.login')
# 문자 입력
driver.find_element_by_name('id').send_keys('id')
driver.find_element_by_name('pw').send_keys('pw')
driver.implicitly_wait(3)

# 경로 입력 and then, click
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.save_screenshot('after_login.png')
driver.implicitly_wait(10)

# 등록 안함 클릭
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > span.btn_cancel > a').click()
driver.implicitly_wait(10)


# 2018년 영화 검색
elem = driver.find_element_by_id("query")
elem.send_keys("2018년 영화")
driver.implicitly_wait(2)
elem.submit()


driver.find_element_by_xpath('//*[@class="section_more _movieRelease-more"]/a').click()



