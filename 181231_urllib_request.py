"""
import urllib.request
from urllib.parse import urlparse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://www.encar.com/'

urlo = urllib.request.urlopen(url)

print(type(urlo))
print('geturl :', urlo.geturl())
print('status :', urlo.status)
print('headers :', urlo.getheaders())
print('info :', urlo.info(), '\n')
print('getcode :', urlo.getcode())
print('read :', urlo.read(10).decode('utf-8'))
print(urlparse('http://www.encar.co.kr?test=test').query)


# 02
## 내 ip 값 가져오기
api = 'https://api.ipify.org'

values = {
    'format' : 'json'
}

print('before', values)
params = urllib.parse.urlencode(values)
print('after', params)

## 요청 url 생성
url = api + '?' + params
print('요청 url =', url)

## 읽기
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)

api = 'https://www.mois.go.kr/frt/a01/frtMain.do'

values = {
    'ctxCd' : '1001'
}
params = urllib.parse.urlencode(values)

url = api + '?' + params
print('url=', url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)

# 03
import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=qvJ1FHRR1n8')
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ', ', videos[i])

    down_dir ='C:/Users/hsh01/Downloads'
videos[0].download(down_dir)

## 아나콘다 프롬프트에서 /ffmpeg가 있는 폴더에서 / ffmpeg -i "동영상파일명" mp3파일명
"""
# 04
import os
import subprocess
import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=3FsrPEUt2Dg')

vids = yt.streams.all()

# 영상 형식 리스트 확인
for i in range(len(vids)):
    print(i, ' , ', vids[i])

cnum = int(input('다운받을 화질은?(0~21 입력)'))

down_dir = 'C:/Users/hsh01/Downloads'
vids[cnum].download(down_dir) # 다운로드 수행

new_filename = input('변환 할 mp3 파일명은?')

ori_filename = vids[cnum].default_filename
subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, ori_filename),
    os.path.join(down_dir, new_filename)
])

print('동영상, mp3 다운로드 완료')
