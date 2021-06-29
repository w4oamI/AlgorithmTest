# a = ["a/a/a.zxc","v/d/a_5v.z","c/b_a5.asd","n/a/c/a_1v.axc"]
# list(a)
# # print(a)
# for i in a:
#   a = i.split('/')
#   # print(a[-1:])

#   b = (a[-1:])
#   # print(b)
#   print()
  # c= list(b.split('.'))
  # print(c)
  # word = str(c[0:])
  # print(c[1:])



a = ["a/a/a.zxc","v/d/a_5v.z","c/b_a5.asd","n/a/c/a_1v.axc"]
# list(a)

for i in a:
  a=i.split('/')
  b=a[-1:]
  word = ''.join(b).split('.')
  print(word)
  