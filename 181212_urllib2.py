import sys
import io
import urllib.request as rq
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = 'http://www.encar.com'

mem = rq.urlopen(url)

#print('geturl', mem.geturl())
#print('status', mem.status) # 200: 정상, 404:없는 페이지, 403:요청 거절, 500:서버 에러
#print('headers', mem.getheaders())
#print('info', mem.info()) # headers
#print('code', mem.getcode()) # 200
#print('read', mem.read().decode('utf-8')) # read()안에 숫자 넣으면 그 바이트 만큼 데이터 가져옴
print(urlparse('http://www.encar.com'))
