def sum_of_divisors(n):
    total=0
    for i in range(1,n+1):
        if n%i==0:
            total=total+i
    return total
num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
sum1=sum_of_divisors(num1)
sum2=sum_of_divisors(num2)
if sum1/num1==sum2/num2:
    print(num1,"and",num2,"are Friendly pairs.")
else:
    print(num1,"and",num2,"are not Friendly pairs")
