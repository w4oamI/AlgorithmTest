arr = ["a","array",'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

arr = set(arr)
arr = list(arr)
arr.sort(reverse=True)
print(arr)