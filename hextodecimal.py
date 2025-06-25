hex=input("Enter hex value:").upper()
decimal=0
power=0
hex_digits="0123456789ABCDEF"
for digit in reversed(hex):
    if digit not in hex_digits:
        print("Error")
        break
    value=hex_digits.index(digit)
    decimal+=value*(16**power)
    power+=1
print("Decimal value:",decimal)