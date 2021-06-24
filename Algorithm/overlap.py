# arr = [3,5,5,5,5,5,2,4,4,4,2]
# count = {}
# answer = []
# for i in arr:
#   try:
#     count[i] += 1
#   except:
#     count[i] = 1

# print(count)
# a = count.values()
# for i in a:
#   if i>=2:
#     answer.append(i)
# print(answer)


arr = [3,5,5,5,5,5,2,4,4,4,2]
l=list(arr)
for i in set(l):
  print(i, l.spilt(',').count(i))