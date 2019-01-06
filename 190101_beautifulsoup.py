from urllib.parse import urljoin
'''
baseurl = 'http://test.com/html/a.html'
print(">>", urljoin(baseurl, "b.html"))
print(">>", urljoin(baseurl, 'sub/c.html'))
print(">>", urljoin(baseurl, '../index.html'))
print(">>", urljoin(baseurl, '../img/hoge.png'))
print(">>", urljoin(baseurl, '../css/hoge.css'))


#02 직접접근 가져오기

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
    <h1>Find VS Select 차이</h1>
    <p>CSS 선택자를 사용 및 다중 반환</p>
    <p>태그 선택자 사용 및 단일 반환</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print('soup', type(soup))
h1 = soup.html.body.h1
print('h1', type(h1))
print(h1.string)
print(h1)
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling.next_sibling
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print('h1 = ' + h1.string)
print('p =' + p1.string)
print('p =' + p2.string)



# 03 태그 선택자로 가져오기
from bs4 import BeautifulSoup
html = """
<html>
<body>
    <ul>
        <li><a href='http://www.naver.com'>naver</a></li>
        <li><a href='http://www.daum.net'>daum</a></li>
        <li><a href='https://www.google.com'>google</a></li>
        <li><a href='https://www.tistory.com'>tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

print('prettify', soup.prettify())
a= soup.find_all('a', string='daum')
b= soup.find_all(string=['naver', 'daum'])
c= soup.find_all('a', limit=2)
print('a', a)
print('b', b)
print('c', c)

links = soup.find_all('a')
print('links', links)

## 츨력
for a in links:
    print('a', type(a), a)
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)

'''
# 04 css 선택자로 가져오기

from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<div id ='main'>
    <h1>강의목록</h1>
    <ul class='lecs'>
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
print('prettify', soup.prettify())
h1 = soup.select_one("div#main > h1").string
print("h1 =", h1)

li_list = soup.select("div#main > ul.lecs > li")
for li in li_list:
    print("li =", li.string)
