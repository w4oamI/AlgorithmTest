def solution(arr):
  return sum(arr)/len(arr)

a = list(map(int, input().split()))
print(solution(a))