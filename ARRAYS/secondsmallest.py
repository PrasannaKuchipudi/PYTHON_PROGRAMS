arr=[22,88,11,44,66,99,33,55]
if len(arr)<2:
    print("Array must have atleast two elements")
else:
    if arr[0]<arr[1]:
        smallest=arr[0]
        second_smallest=arr[1]
    else:
        smallest=arr[1]
        second_smallest=arr[0]
    for i in range(2,len(arr)):
        num=arr[i]
        if num<smallest:
            second_smallest=smallest
            smallest=num
        elif smallest<num<second_smallest:
            second_smallest=num
    if smallest==second_smallest:
        print("NO SECOND SMALLEST ELEMENT")
    else:
        print("Second smallest element is:",second_smallest)