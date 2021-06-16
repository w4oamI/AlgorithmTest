# s = "apple1 APPLE2"

# for i in s:
#   if i.islower():
#     print(i.upper(),end="")
#   elif i.isupper():
#     print(i.lower(),end="")
#   else:
#     print(i,end="")

s = "APPLE apple"

for i in s:
  if i.islower():
    print(i.upper(),end='')
  elif i.isupper():
    print(i.lower(),end='')
  else:
    print(i,end='')