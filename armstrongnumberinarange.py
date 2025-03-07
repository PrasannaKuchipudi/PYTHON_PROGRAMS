start=int(input("Enter a number"))
end=int(input("Enter a number"))
for i in range(start,end+1):
    temp=i
    b=len(str(i))
    sum1=0
    while temp >0:
        r=temp%10
        sum1=sum1+(r**b)
        temp=temp//10
    if sum1==i:
        print(i,end=" ")

