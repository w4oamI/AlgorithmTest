def sele(a):
  size=len(a)
  for i in range(1, size):
    key = a[i]
    j=i-1
    while j>=0 and a[j] > key:
      a[j+1] = a[j]
      j-=1
    a[j+1]=key

d = [2,4,5,1,3]
sele(d)
print(d)