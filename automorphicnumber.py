num=int(input("Enter a number:"))
square=num*num
temp=num
flag=True
while temp>0:
    if temp%10!=square%10:
        flag=False
        break
    temp//=10
    square//=10
if flag:
    print(f"{num} is a automorphic number")
else:
    print(f"{num} is not a automorphic number")


