import os
from selenium import webdriver
from bs4 import BeautifulSoup
import argparse
import time
import csv

from pprint import pprint

# 폴더 만들기
if not os.path.exists('./movie_review_crawling'):
    os.makedirs('./movie_review_crawling')


def movie_review_find():

    parser = argparse.ArgumentParser(description='crawling naver shop homepage')
    parser.add_argument('-u','--url',
                        type=str,
                        default="https://movie.naver.com/",
                        help='which site to be crawled')
    parser.add_argument('-d', '--dir',
                        type=str,
                        default='C:/Users/korea/Desktop/NAVER/chromedriver',
                        help='location of chromedriver')
    parser.add_argument('-s', '--search',
                        type=str,
                        default='갱스 오브 뉴욕',
                        help='word for searching')
    args = vars(parser.parse_args())
    driver = webdriver.Chrome(args['dir'])
    driver.get(args['url'])
    elem = driver.find_element_by_xpath('//*[@id="ipt_tx_srch"]')
    elem.send_keys(args['search'])

    # selenium 에서 xpath 를 이용해서 크롤링 하기
    driver.find_element_by_xpath('//*[@id="jSearchArea"]/div/button').click()
    # 기다리는 시간 설정
    driver.implicitly_wait(5)
    
    driver.find_element_by_xpath('//*[@id="old_content"]/ul[2]/li/dl/dt/a/strong').click()
    driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[5]/a').click()

    # driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[1]/a/span').click()
    driver.switch_to_frame('pointAfterListIframe')
    driver.find_element_by_xpath('//*[@id="orderCheckbox"]/ul/li[2]/a').click()
    driver.implicitly_wait(20)

    # window_after = driver.window_handles[1]
    # driver.switch_to.window(window_after)

# 죽은 시인의 사회
# 어벤져스
# 저스티스 리그
# 토이 스토리 3


    html = driver.page_source
    bsobj = BeautifulSoup(html, 'html.parser')
    # reviews = bsobj.find_all('div', {'class':"score_result"})
    # reviews = bsobj.findAll('li')
    score = bsobj.findAll('div', {'class': 'star_score'})
    reviews = bsobj.findAll('div', {'class':"score_reple"})
    # print(score[1])
    # print(reviews)
    score = score[1:]

    # for i, each_review in zip(score, reviews):
    #     review_score = i.get_text()
    #     review_content = each_review.get_text()
    #     print('*'*30)
    #     # print('{}번째 리뷰'.format(i))
    #     print('점수 : {}'.format(review_score))
    #     print('내용 : {}'.format(review_content))
# //*[@id="pagerTagAnchor1"]
    page = 1

    file_name_path = "./movie_review_crawling/" + args['search'] + ".csv"
    print(file_name_path)
    while True:
        print("="*200)
        print("="*200)
        try:
            driver.find_element_by_xpath('//*[@id="pagerTagAnchor{}"]'.format(page)).click()
            # driver.implicitly_wait(10)
            time.sleep(1)
            html = driver.page_source
            bsobj = BeautifulSoup(html, 'html.parser')

            score = bsobj.findAll('div', {'class': 'star_score'})
            score = score[1:]
            reviews = bsobj.findAll('div', {'class':"score_reple"})

            for i, each_review in zip(score, reviews):
                review_score = i.get_text()
                review_content = each_review.find('p').get_text()
                print('*'*30)
                # print('{}번째 리뷰'.format(i))
                print('점수 : {}'.format(review_score))
                print('내용 : {}'.format(review_content))
# , encoding='utf-8'
                with open(file_name_path, 'a', newline='') as csvf:
                    fieldnames=['점수', '내용']
                    writer=csv.DictWriter(csvf, fieldnames=fieldnames)
                    writer.writerow({'점수':int(review_score), '내용':review_content})

            page += 1
        # 
        except:
            print("크롤링 끝")
            break



if __name__ == "__main__":
    movie_review_find()




