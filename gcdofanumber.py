num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
num3=int(input("Enter num3 value:"))
for i in range(1,num3):
    if num1%i==num2%i==num3%i==0:
        gcd=i
print("HCF of",num1,",",num2,"and",num3,"is",gcd)