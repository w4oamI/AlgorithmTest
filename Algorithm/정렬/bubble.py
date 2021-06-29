

def bubble_a(arry):
  for i in range(len(arry) -1,0,-1):
    for j in range(i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [4,3,5,1,2]
bubble_a(arr)
print(arr)