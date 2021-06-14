#------------------------------#
def prime(x):
  for i in range(2,x-1):
    if x%i==0:
      return False
    return True
print(prime(7))
print(prime(4))
#------------------------------#


#위를 개선
#------------------------------#
import math
def prim(x):
  for i in range(2,int(math.sqrt(x)) +1):
    if x%i == 0:
      return False
    return True
print(prim(7))
print(prim(4))
#------------------------------#


#에라토스테네스의 체
#-------------------------------#
import math
n=1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
  if array[i] == True:
    j =2
    while i*j <= n:
      array[i*j] = False
      j+=1
for i in range(2,n+1):
  if array[i]:
    print(i,end='')