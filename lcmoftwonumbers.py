a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
for i in range(min(a,b),1+(a*b)):
    if i%a==0 and i%b==0:
        lcm=i
        break
print(f"LCM of {a} and {b} is {lcm}")