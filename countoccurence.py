number=int(input("Enter the number:"))
digit = int(input("Enter the digit to count:"))
count=0
temp=number
while temp>0:
    if temp%10==digit:
        count+=1
    temp//=10
print(f"The digit '{digit}' occurs {count} times in the number {number}.")

