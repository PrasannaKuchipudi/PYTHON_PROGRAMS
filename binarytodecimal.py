binary=input("Enter binary value:")
decimal=0
power=0
for digit in reversed(binary):
    if digit=='1':
        decimal+=2**power
    elif digit!='0':
        print("Invalid binary number")
        break
    power+=1
print("Decimal value:",decimal)