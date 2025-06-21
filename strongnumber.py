def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num=int(input("Enter a number:"))
temp=num
sum=0
while num>0:
    digit=num%10
    sum+=factorial(digit)
    num=num//10
if sum==temp:
    print(f"{temp} is a Strong Number")
else:
    print(f"{temp} is not a Strong Number")
