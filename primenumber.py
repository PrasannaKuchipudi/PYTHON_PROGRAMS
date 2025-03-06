number=2
temp=0
if number<2:
    temp=1
else:
   for i in range(2,number):
       if number%i==0:
           temp=1
           break
if temp==1:
    print(f"{number} is not a prime number".format(number))
else:
    print(f"{number} is  a prime number".format(number))