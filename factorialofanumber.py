num=int(input("Enter a number:"))
f=1
if num<1:
    print("Not Possible")
else:
    for i in range(1,num+1):
        f=f*i
    print("Factorial of a number:",f)
