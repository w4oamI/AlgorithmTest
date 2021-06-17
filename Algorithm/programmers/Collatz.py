def solution(num):
  answer = 0
    if num == 1:
        return 0
    
    for i in range(500):
        num= num /2 if num % 2==0 else (num*3)+1
        answer += 1
        if num == 1:
            return i+1
    return -1

a = int(input())
print(a)