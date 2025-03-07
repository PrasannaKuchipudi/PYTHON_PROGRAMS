n = int(input("Enter a number:"))
sum=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**b)
    n=n//10
if sum==sum1:
    print(f"{sum} is a Armstrong Number".format(sum))
else:
    print(f"{sum} is not a Armstrong Number".format(sum))

