arr = [3,2,4,4,2,5,2,5,5]
count = {}
answer = []
for i in arr:
  try:
    count[i] += 1
  except:
    count[i] = 1

print(count)
a = count.values()
for i in a:
  if i>=2:
    answer.append(i)
print(answer)