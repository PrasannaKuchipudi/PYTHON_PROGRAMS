octal=input("Enter octal value:")
decimal=0
power=0
for i in reversed(octal):
    decimal+=int(i)*(8**power)
    power+=1
print("Decimal value",decimal)
