'''
import sys
import io
import requests as rq
import json as js

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#r = rq.get('https://api.github.com/events')
#r.raise_for_status() # 에러 발생시 무슨 에러인지 띄워줌
#print(r.text)

jar = rq.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain = 'httpbin.org', path='/cookies')

#r = rq.get('http://httpbin.org/cookies', cookies = jar)
#r.raise_for_status()
#print(r.text)

#r = rq.get('https://github.com', timeout=3)
#print(r.text)

#r = rq.post('http://httpbin.org/post', data = {'name':'kim'}, cookies=jar)
#print(r.text)

payload1 = {'key1' : 'value1', 'key2' : 'value2'} # dict
payload2 = (('key1', 'value1'), ('key2', 'value2')) # tuple
payload3 = {'some' : 'nice'}

r = rq.post('http://httpbin.org/post', data=payload1) # form
print(r.text)

r = rq.post('http://httpbin.org/post', data=js.dumps(payload3)) # json
print(r.text)



# 02

import sys
import io
import requests as rq
import json as js

# Rest : post, get, put:update, replace (fetch : update, modify), delete

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1 = {'key1' : 'value1', 'key2': 'value2'} # dict
payload2 = (('key1', 'value1'), ('key2', 'value2')) # tuple
payload3 = {'some':'nice'}

#r = rq.put('http://httpbin.org/user/delete', data=payload1)
#print(r.text)

#r = rq.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
#print(r.text)

r = rq.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

'''

### ifixit
import sys
import io
import requests as rq
import json as js

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r = rq.get('https://www.ifixit.com/api/2.0/doc/store/user/cart')
print(r.text)
