arr=[10,9,8,5,1,3,2,5,60]
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
print("Largest element:",max)
print("Smallest element:",min)