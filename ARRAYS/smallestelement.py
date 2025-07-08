arr=[3,4,1,0,2,6,7,9]
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
print(min)