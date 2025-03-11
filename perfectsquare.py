def squareroot(n):
    if n<0:
        return False
    square=int(n**0.5)
    return square*square==n
n=int(input("Enter a number:"))
if squareroot(n):
    print(f"{n} is Perfect Square number")
else:
    print(f"{n} is not a Perfect Square number")