def fibonacci(n):
    fibs=set()
    a,b=0,1
    while a<=n:
        fibs.add(a)
        a,b=b,a+b
    return fibs
def non_fibonacci(n):
    fibs=fibonacci(n)
    for i in range(1,n+1):
        if i not in fibs:
            print(i,end=' ')
n=int(input("Enter range:"))
print("Not fibonacci series upto n {}".format(n))
non_fibonacci(n)
