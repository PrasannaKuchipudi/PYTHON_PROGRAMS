num=int(input("Enter range:"))
for n in range(10,num+1):
    sum=0
    power=len(str(n))
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**power
        temp//=10
    if n==sum:
        print(n,end=" ")
        