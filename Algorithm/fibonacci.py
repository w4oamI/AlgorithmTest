def fibo(n):
  if n<=1:
    return n
  else:
    return (fibo(n-1) + fibo(n-2))

print(fibo(7))

a, b = 1, 1
for i in range(2):
  print(a,end=' ')
  a,b = b, a+b