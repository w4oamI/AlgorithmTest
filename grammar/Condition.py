#-------------------------#
x = 15
if x>=10:
  print("x>=10")
if x>=0:
  print("x>=0")
if x>=30:
  print("x>=30")
#-------------------------#

#-------------------------#
a= -15
if a>=0:
  print("a>=0")
elif a>=-10:
  print("a>=-10")
else:
  print("-10>a")
#-------------------------#

#-------------------------#
num = 85

if num>=90:
  print("A")
elif num>=80:
  print("B")
elif num>=70:
  print("C")
else:
  print("F")
#-------------------------#

#-------------------------#
if True or False:
  print("yes")

a=15
if a<=15 and a>0:
  print("Yes")
#-------------------------#

#기타 연산자
#-------------------------#
#x in 리스트 = x가 있으면 참
#x not in 문자열 = x가 없으면 참
#-------------------------#

#조건문 간소화
#-------------------------#
score = 85
if score>80: result = "Success"
else: result = "Fail"
print(result)
#-------------------------#
score = 85
result = "Success" if score>80 else "Fail"

print(result)