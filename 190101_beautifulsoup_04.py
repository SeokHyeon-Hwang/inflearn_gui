
'''
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep # 쿼리문 만드는데 사용
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#sys.stdout.reconfigure(encoding='utf-8')

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('사자')
url = base + quote

res = req.urlopen(url)
savepath = 'C:/Users/hsh01/Downloads/image/'
try :
    if not(os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print('Failed to create directory!')
        raise

soup = BeautifulSoup(res, 'html.parser')

li_list = soup.select('div.img_area._item > a.thumb._thumb > img')
for i, div in enumerate(li_list, 1):
    print('div =', div['data-source'])
    fullfilename = os.path.join(savepath, savepath+str(i)+'.jpg')
    print(fullfilename)
    req.urlretrieve(div['data-source'], fullfilename)
    print(i)
'''

# 02
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stedrr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savepath = 'c:/Users/hsh01/Downloads/image/'

base = 'https://www.inflearn.com/'
quote = rep.quote_plus('추천-강좌')
url = base+quote
#print(url)

res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')

recommand = soup.select('ul.slides')[0]

try:
    if not(os.path.isdir(savepath)):
        os.makedirs(os.path.join(savepath))
except OSError as e:
    if e.errno != error.EEXIST:
        print('Failed to create directory!')
        raise

for i, e in enumerate(recommand, 1):
    with open(savepath+'title_'+str(i)+'.txt', 'wt') as f:
        f.write(e.select_one('h4.block_title > a').string)
    fullfilename = os.path.join(savepath, savepath+'img_'+str(i)+'.png')
    req.urlretrieve(e.select_one('div.block_media > a > img')['src'], fullfilename)

print('강좌 정보 텍스트 출력 및 이미지 다운 완료')
