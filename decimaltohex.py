decimal=int(input("Enter decimal value:"))
hex_digits="0123456789ABCDEF"
hex=""
if decimal==0:
    hex="0"
else:
    while decimal>0:
        remainder=decimal%16
        hex=hex_digits[remainder]+hex
        decimal=decimal//16
print("HEXADECIMAL VALUE:",hex)