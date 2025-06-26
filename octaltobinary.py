octal=input("Enter octal number:")
binary=""
oct_to_bin={'0':'000','1':'001','2':"010",'3':"011",'4':'100','5':'101','6':'110','7':'111'}
for digit in octal:
    binary+=oct_to_bin[digit]
binary=binary.lstrip('0') or '0'
print("Binary Number:",binary)