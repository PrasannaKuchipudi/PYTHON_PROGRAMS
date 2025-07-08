arr=[8,2,3,4,1,0,9,4,5]
if len(arr)<2:
    print("Arry needs at least 2 elements to sort halves.")
else:
    n=len(arr)
    mid=n//2
    first_half=sorted(arr[:mid])
    second_half=sorted(arr[mid:],reverse=True)
    result=first_half+second_half
    print("Original array:",arr)
    print("First half sorted ascending:",first_half)
    print("Second half sorted descending:",second_half)
    print("Final array:",result)