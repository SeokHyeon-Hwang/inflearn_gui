import sys
import io
import urllib.request as rq


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

## urlretrieve는 대량 다운로드 시에 사용하자. 다이렉트 저장
## urlopen은 변수에 할당한다. 추가 작업이 들어갈 시 사용.

#1
'''
imgurl = 'http://blogfiles.naver.net/20150304_286/monsmonsyo_1425448212658QR1Ai_JPEG/7.jpg'
savepath = 'c:/test1.jpg'

rq.urlretrieve(imgurl, savepath)

print('다운로드 완료')
'''
#2
'''
htmlurl = 'http://google.com'
savepath2 = 'c:/index.html'

rq.urlretrieve(htmlurl, savepath2)

print('다운로드 완료2')
'''

#3
'''
imgurl = 'http://blogfiles.naver.net/20150304_286/monsmonsyo_1425448212658QR1Ai_JPEG/7.jpg'
savepath3 = 'C:/Users/hsh01/Downloads/test1.jpg'

f = rq.urlopen(imgurl).read()
savefile1 = open(savepath3, 'wb')
savefile1.write(f)
savefile1.close()

print('다운로드 완료3')
'''

#4
htmlurl = 'http://google.com'
savepath4 = 'C:/Users/hsh01/Downloads/index.html'

f2 = rq.urlopen(htmlurl).read()

with open(savepath4, 'wb') as savefile2:
    savefile2.write(f2)

print('다운로드 완료4')
