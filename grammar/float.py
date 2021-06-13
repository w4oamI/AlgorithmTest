a= 1000.
a=-7.5
print(a)

#양의 실수
a = 17.7
print(a)

#음의 실수
a = -17.7
print(a)

#소수부가 0일때 0을 생략
a = 17.
print(a)

#정수부가 0일때 0을 생략
a = -.17
print(a)

#실수를 정수화
a = int(17.5)
print(a)


#round()함수 이용
print("round()함수 이용X")
#----------------------#
#실수 덧셈으로 조건문 힘들다.
a = 0.3 + 0.6
print(a)

if a==0.9:
  print(True)
else:
  print(False)
#False가 나온다.
#그렇기 때문에 round()함수를 사용.
print("round()함수 이용")
a = 0.3+0.6
print(a)
print(round(a,1))

if round(a,1)==0.9:
  print(True)
else:
  print(False)
#----------------------#