'''
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import lxml

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://finance.daum.net/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'lxml')
print(soup)

top = soup.select('ul#boxTopSearchs > li')
print(top)

for i, e in enumerate(top,1):
    print(i, e.find('a').string, '=', e.find('span').string)


# 02
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import lxml

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://finance.naver.com/sise/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'lxml')
#print(soup)
top = soup.select('#popularItemList > li')
#print(top)
print(len(top))


for i in range(len(top)):
    for e in top:
        if e.find('li') is not None:
            print(i, e.select_one('a').string, '=', e.select_one('span').string)
            i += 1
'''

# 03
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base ='https://www.inflearn.com/'
quote = rep.quote_plus('추천-강좌')
print(quote)

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'lxml')

recommand = soup.select('ul.slides')[0]
print(recommand)

#for e in recommand:
#    print(e.select_one())

for i, e in enumerate(recommand, 1):
    print(i, e.select_one('h4.block_title > a').string)
