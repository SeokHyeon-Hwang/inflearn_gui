'''
import sys
import io
import requests as rq

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = rq.Session() # 세션을 연다.
#r = s.get('https://naver.com') # put, delete, get, post
#print('1', r.text)

#r = s.get('http://httpbin.org/cookies', cookies = {'from':'myname'})
#print(r.text)

url = 'http://httpbin.org/get' # http request test 사이트
headers = {'user-agent' : 'mypythonapp_1.0.0'}

#r = s.get(url, headers = headers)
#print(r.text)

s.close() # 세션을 닫는다. 자원 낭비를 막는다.


# close 사용하지 않고 with 문 사용한다면
with rq.Session() as s:
    r = s.get('https://naver.com')
    print(r.text)



# 02

import sys
import io
import requests as rq

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# response 상태 코드
s = rq.Session()
#r = s.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.ok)

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
#print(r.text)
#print(r.json())
#print(r.json().keys())
#print(r.json().values())
#print(r.encoding)
#print(r.content)
print(r.raw)

'''

import sys
import io
import requests as rq
import json as js

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = rq.Session()

r = s.get('http://httpbin.org/stream/20', stream = True)
#print(r.text)
#print(r.encoding)
#print(r.json())

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = js.loads(line) # dict
    for e in b.keys():
        print('key:', e, 'value:', b[e])
