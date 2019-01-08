'''

import sys
import io
import requests as rq
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저 정보
login_info = {
    'user_id':'아이디',
    'user_pw':'비밀번호'
}

# Session 생성, with 구문 안에서 유지
with rq.Session() as s:

    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=login_info)
    # html 소스 확인
    #print('login_req', login_req.text)
    # http header 확인
    #print('login_req', login_req.headers)

    # response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        # 권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4455742&find=&ftext=')
        # 예외 발생
        post_one.raise_for_status()
        #print(post_one.text)
        # BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.pretiffy())
        article = soup.select_one('table:nth-of-type(3)').find_all('p')
        #print(article)
        for i in article:
            if i.string is not None and i.img == None:
                print(i.string)

'''

# 02

import requests as rq
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저 정보
login_info = {
    'log' : 'bigdata3',
    'pwd' : 'qwer1234',
    'user-submit' : rep.quote_plus('로그인'),
    'user-cookies' : 1
}

# Session 생성, with 구문 안에서 유지
with rq.Session() as s:

    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data=login_info)
    # html 소스 확인
    #print('login_req', login_req.text)
    # http header 확인
    #print('login_req', login_req.headers)

    # response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        # 권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('https://www.inflearn.com/members/outsider7224/')
        # 예외 발생
        post_one.raise_for_status()
        #print(post_one.text)
        # BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        badges = soup.select('div.badges > ul > li > a > img')
        # 이미지 쓰기
        for i, z in enumerate(badges, 1):
            fullFileName = os.path.join('C:/Users/hsh01/Downloads/gui/', str(i)+ '.jpg')
            req.urlretrieve(z['src'], fullFileName)
