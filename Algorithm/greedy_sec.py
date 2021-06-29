n,k=map(int,input().split())
result = 0

while True:
  target = (n//k) * k
  result += (n- target)
  if n<k:
    break
  result += 1
  n//=k

print(n)
result += (n-1)
print(result)