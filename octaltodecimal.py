number=int(input("Enter a value:"))
octal=number
decimal=0
base=1
while number:
    last=number%10
    number=number//10
    decimal=decimal+last*base
    base=base*8
print("Decimal number of octal",octal,"is",decimal)