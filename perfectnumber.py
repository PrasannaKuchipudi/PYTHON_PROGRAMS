n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(f"{n} is a Pefect Number")
else:
    print(f"{n} is not a Perfect Number")