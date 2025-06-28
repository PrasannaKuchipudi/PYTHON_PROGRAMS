n=int(input("Enter a number:"))
s=str(n)
l=[]
for i in s:
    if i=='0':
        l.append('1')
    else:
        l.append(i)
g=""
for k in l:
    g+=k
print(f"Converted number is:{g}")
