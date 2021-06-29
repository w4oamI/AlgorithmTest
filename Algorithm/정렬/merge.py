def merge(a):
  n=len(a)
  if n<=1:
    return
  
  mid = n//2
  g1 = a[:mid]
  g2 = a[mid:]
  merge(g1)
  merge(g2)

  i1 = 0
  i2 = 0
  ia = 0

  while i1 < len(g1) and i2 < len(g2):
    if g1[i1] > g1[i2]:
      a[ia] = g1[i1]
      i1 += 1
      ia += 1
d = [6,8,3,9,10,1,2,4,7,5]
merge(d)
print(d)