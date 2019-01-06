
'''
from bs4 import BeautifulSoup
import re #regex
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li id='naver'><a href='http://www.naver.com'>naver</a></li>
        <li><a href='http://www.daum.net'>daum</a></li>
        <li><a href='https://www.google.com'>google</a></li>
        <li><a href='https://www.tistory.com'>tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
naver = soup.find(id='naver')
print('id:naver >>' + naver.string)

## 정규표현식으로 가져오기
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])

# 02
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open('food-list.html', encoding ='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print('1', soup.select_one('li:nth-of-type(8)').string)
print('2', soup.select_one('#fd-list > li:nth-of-type(4)').string)
print('3', soup.select('#ac-list > li[data-lo="ko"]')[0].string)
print('4', soup.select('#fd-list > li.food.hot')[1].string)

# 파라미터를 쓰고, find 매소드 사용
cond1 = {'data-lo':'jp', 'class':'food'}
cond2 = {'data-lo':'ko', 'class':'alcohol'}

print('5', soup.find('li', cond1).string)

print('6', soup.find(id='ac-list').find('li', cond2).string)

cond3 = soup.find(id='ac-list').find_all('li', {'data-lo':'ko', 'class':'alcohol'})
for item in cond3:
    print(item.string)

for ac in soup.find_all('li'):
    if ac['data-lo'] == 'us':
        print('data-lo ==us', ac.string)
'''

# 03
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

cars = open('cars.html', encoding = 'utf-8')
soup = BeautifulSoup(cars, 'html.parser')

def car_func(selector):
    print('car_func', soup.select_one(selector).string)



car_func('#gr')
car_func('li#gr')
car_func('ul > li#gr') # 자식 태그
car_func('#cars #gr')
car_func('#cars > #gr')
car_func("li[id='gr']")

print('car_func', soup.select('li')[3].string)
print('car_func', soup.find_all('li')[3].string)


## 람다식
car_lambda = lambda q : print('car_lambda', soup.select_one(q).string)


car_lambda('#gr')
car_lambda('li#gr')
car_lambda('ul > li#gr') # 자식 태그
car_lambda('#cars #gr')
car_lambda('#cars > #gr')
car_lambda("li[id='gr']")
