number=int(input("Enter a number:"))
power=int(input("Enter power value:"))
answer=1
for i in range(power):
    answer*=number
print(answer)