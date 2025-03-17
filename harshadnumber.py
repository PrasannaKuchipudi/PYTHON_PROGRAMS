num = int(input("Enter a number:"))
num1=str(num)
sum=0
for digit in num1:
    sum=sum+int(digit)
if num%sum==0:
    print(num,"is a Harshad Number")
else:
    print(num,"is not a Harshad Number")
