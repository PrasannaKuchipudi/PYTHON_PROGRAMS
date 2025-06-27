def find_gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
n1=int(input("Enter numerator of first fraction:"))
d1=int(input("Enter denominator of first fraction:"))
n2=int(input("Enter numerator of second fraction:"))
d2=int(input("Enter denominator of second fraction:"))
numerator=(n1*d2)+(n2*d1)
denominator=d1*d2
gcd=find_gcd(numerator,denominator)
simplified_num=numerator//gcd
simplified_den=denominator//gcd
print(f"The simplified sum of the fraction is:{simplified_num}/{simplified_den}")

    