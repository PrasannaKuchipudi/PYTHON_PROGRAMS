a = int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>=b and a>=c:
    print(f"{a} is greatest value".format(a))
elif b>=a and b>=c:
    print(f"{b} is greatest value".format(b))
else:
    print(f"{c} is gratest value".format(c))