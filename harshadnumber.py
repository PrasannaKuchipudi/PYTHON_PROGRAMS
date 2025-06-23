num=int(input("Enter a number:"))
temp=num
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
if temp%sum==0:
    print(f"{temp} is a Harshad Number")
else:
    print(f"{temp} is not a Harshad Number")
