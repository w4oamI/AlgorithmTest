#더하기 함수
#----------------------------#
def add(a,b):
  return a+b
print(add(1,4))
#----------------------------#
def add(a,b):
  return print(a+b)
add(1,4)
#----------------------------#


#더하기와 빼기 함수
#----------------------------#
def add(a,b):
  return a+b

def sub(a,b):
  return a-b

result = add(3,7)
print(result)

result = sub(3,7)
print(result)
#----------------------------#


#global키워드
#----------------------------#
a = 0

def func():
  global a
  a+=1
for i in range(10):
  func()

print(a)
#----------------------------#
a=10

def func():

  print(a+20)

func()
#----------------------------#


#패킹: 여러개의 변수가 한꺼번에 반환
#언패킹: 반환값을 특정 변수에 담는것
#--------------------------------#
def oper(a,b):
  add = a+b
  sub = a-b
  mul = a*b
  div = a//b
  return add,sub,mul,div

a,b,c,d=oper(7,3)
print(a,b,c,d)
#--------------------------------#

#람다식
#--------------------------------#
def add(a,b):
  return a+b
print(add(1,4))
#람다식으로 변경
print((lambda a,b: a+b)(1,4))
#--------------------------------#

#--------------------------------#
array = [('홍길동',50),('이순신',32), ('장보고',74)]

def my_key(x):
  return x[1]  #두번째 원소를 기준으로 정렬
print(sorted(array, key=my_key))
#위의 코드를 람다식으로 표현
print(sorted(array, key=lambda x:x[1]))
#--------------------------------#

#여러개 리스트에 적용
#--------------------------------#
a = [1,2,3,4,5]
b = [6,7,8,9,10]

result = map(lambda a,b: a+b, a, b)
print(list(result))
#--------------------------------#