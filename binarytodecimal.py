binary=input("Enter binary value:")
decimal=0
power=0
for digit in reversed(binary):
    decimal+=int(digit)*(2**power)
    power+=1
print("Decimal value:",decimal)