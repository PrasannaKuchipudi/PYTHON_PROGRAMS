def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def strongnumber(n):
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum+=factorial(digit)
        n=n//10
    return sum==temp
n=int(input("Enter a number:"))
if strongnumber(n):
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is not a Strong Number")