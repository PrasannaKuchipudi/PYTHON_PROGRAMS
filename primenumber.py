n=int(input("Enter a number:"))
temp=0
for i in range(2,n):
    if n%i==0:
        temp=1
        break
if temp==1:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")