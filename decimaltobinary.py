decimal=int(input("Enter decimal value:"))
binary=""
if decimal==0:
    binary="0"
else:
    while decimal>0:
        remainder=decimal%2
        binary=str(remainder)+binary
        decimal=decimal//2
print("Binary value:",binary)