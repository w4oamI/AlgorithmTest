#--------------------------------------#
#데이터 갯수 입력
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
#--------------------------------------#

n=int(input())
data = list(map(int, input().split()))
print(data)

#--------------------------------------#
a,b,c = map(int, input().split())
print(a,b,c)
#--------------------------------------#


#input을 사용하지 않고 빠르게 입력받기
#rstrip()은 입력후 엔터(줄바꿈)를 치기
# 때문에 줄바꿈을 없애기 위해 사용한다.
#--------------------------------------#
import sys
data = sys.stdin.readline().rstrip()
print(data)
#--------------------------------------#


#print문 사용
#문자열과 정수는 같이 사용할 수 없다.
#--------------------------------------#
a=1
b=2
print(a,b)
print(7,end=" ")
print(8,end=" ")

answer = 7
print("정답은" + str(answer)+ "입니다.")
#--------------------------------------#


#f-string
#--------------------------------------#
answer = 7
print(f"정답은 {answer} 입니다.")
#--------------------------------------#