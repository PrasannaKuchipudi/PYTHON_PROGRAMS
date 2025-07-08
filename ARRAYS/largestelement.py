arr=[1,7,8,4,9,4,3]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)