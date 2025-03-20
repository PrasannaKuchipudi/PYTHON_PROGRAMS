number=int(input("Enter Binary Number:"))
Binary=number
Decimal=0
Base=1
while number>0:
    remainder = number%10
    Decimal=Decimal+remainder*Base
    number=number//10
    Base=Base*2
print("Decimal number of",Binary,"is",Decimal)
