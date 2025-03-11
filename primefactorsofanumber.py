def primefactors(n):
    factors=[ ]
    while n%2==0:
        factors.append(2)
        n//=2
    for i in range(3,int(0.5**2),2):
        while n%i==0:
            factors.append(i)
            n//=i
    if n>1:
        factors.append(n)
    return factors
n=int(input("Enter a number:"))
print("Prime factors are:",primefactors(n))