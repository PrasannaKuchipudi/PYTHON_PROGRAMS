num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
for i in range(1,num2):
    if num1%i==0 and num2%i==0:
        hcf=i
print("HCF of",num1,"and",num2,"is",hcf)