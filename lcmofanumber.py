num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
num3=int(input("Enter num3 value:"))
for i in range(max(num1,num2,num3),num1*num2*num3):
    if i%num1==i%num2==i%num3==0:
        lcm=i
        break
print("LCM of",num1,",",num2,"and",num3,"is",lcm)