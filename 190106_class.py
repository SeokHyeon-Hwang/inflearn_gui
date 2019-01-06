'''
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class userinfo:

    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('---------------')
        print('name :' + self.name)
        print('phone :' + self.phone)
        print('---------------')



user1 = userinfo()
user2 = userinfo()
user1.set_info('kim', '010-1111-2222')
user2.set_info('lee', '010-3333-4444')
user1.print_info()
print(type(user1))
print(id(user1))
print(type(user2))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)


# 02 __init__ 사용, 객체 초기화

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class userinfo:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('---------------')
        print('name :' + self.name)
        print('phone :' + self.phone)
        print('---------------')

    def __del__(self):
        print('delete')


user1 = userinfo('kim', '010-1111-2222')
user2 = userinfo('lee', '010-3333-4444')

print(user1.__dict__)
print(user2.__dict__)



# 03

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class selftest:
    def func1():
        print('function1 called!')

    def func2(self):
        print(id(self))
        print('punction2 called.')

f = selftest() # 호출방법2: 인스턴스를 생성해서 self를 매개변수로 호출하는 방법
print(dir(f))

#f.func1() # error: arguments 를 안받게 되어 있는데 하나가 넘어왔다.

f.func2()
print(id(f))  # 메모리 주소

print(selftest.func1()) # 호출방법 1:직접 호출은 가능
print(selftest.__dict__)



# 04

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        warehouse.stock_num +=1

    def __del__(self):
        warehouse.stock_num -=1

u1 = warehouse('p1')
u2 = warehouse('p2')

print(u1.name)
print(u2.name)
print(u1.__dict__)
print(dir(u2))
print(u2.__dict__)
print(u1.stock_num)
print(u2.stock_num)

'''

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

class nametest:
    total = 0 # 클래스 변수

print(dir())
print('before : ', nametest.__dict__)
nametest.total = 1
print('after : ', nametest.__dict__)
n1 = nametest()
n2 = nametest()
print(id(n1), ' vs ', id(n2))
print(dir())
print(n1.__dict__)
print(n2.__dict__)

n1.total = 77
print(n1.__dict__)
print(n2.__dict__)

#print(n1.test)
