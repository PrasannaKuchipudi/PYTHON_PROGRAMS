num=int(input("Enter a number:"))
temp=num
sum=0
power=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**power
    temp//=10
if num==sum:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

    