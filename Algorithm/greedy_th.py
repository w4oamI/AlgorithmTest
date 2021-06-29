data = input()

result=int(data[0])
print("변환전", result)
# result = 0
for i in range(1,len(data)):
  num=int(data[i])
  if num <=1 or result <= 1:
    result += num
  else:
    result *= num

print("두번째", result)