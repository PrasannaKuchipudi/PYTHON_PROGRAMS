def CountDigit(n):
    digit=0
    while n!=0:
        n//=10
        digit+=1
    return digit
n=123456
print("No.of digits:",CountDigit(n))
