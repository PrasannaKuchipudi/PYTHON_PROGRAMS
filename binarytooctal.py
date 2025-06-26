binary=input("Enter binary number:")
while len(binary)%3!=0:
    binary='0'+binary
octal=''
for i in range(0,len(binary),3):
    group=binary[i:i+3]
    digit=0
    digit+=int(group[0])*4
    digit+=int(group[1])*2
    digit+=int(group[2])*1
    octal+=str(digit)
print("Octal:",octal)