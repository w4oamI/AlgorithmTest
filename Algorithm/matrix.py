n = int(input())
x,y = 1,1
plans = input().split()

#     λ, μ, λ¨, λΆ
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move = ['R','L','D','U']

for plan in plans:
  for i in range(len(move)):
    if plan == move[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  
  x,y=nx,ny

print(x,y)