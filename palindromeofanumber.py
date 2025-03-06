number=int(input("Enter a number:"))
reverse=0
temp=number
while temp > 0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if number==reverse:
    print(f"{number} is a Palindrome Number".format(number))
else:
    print(f"{number} is not a Palindrome Number".format(number))
