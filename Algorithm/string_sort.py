# s = input()
# ch=[]
# value = 0

# for x in s:
#   if x.isalpha():
#     ch.append(x)
#   else:
#     value += int(x)

# ch.sort()

# if value != 0:
#   ch.append(str(value))
# print(''.join(ch))

s=input()
ch=[]
value =0

for i in s:
  if i.isalpha():
    ch.append(i)
  else:
    value+=int(i)

ch.sort()

if value!=0:
  ch.append(str(value))
print(','.join(ch))