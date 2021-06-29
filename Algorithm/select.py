def sele(a):
  n=len(a)
  print(n)  # 5
  for i in range(0, n-1):
    min_index = i
    for j in range(i+1, n):
      if a[min_index]>a[j]:
        min_index = j
    a[i], a[min_index] = a[min_index], a[i]
    print(a)

d = [2,4,5,1,3]
sele(d)
d.sort(reverse=True)
print(d)