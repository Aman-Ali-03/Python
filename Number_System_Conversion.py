def BtoD(Binary):
    decimal = 0
    j=0
    for i in Binary:
        if i==1:
            decimal += 2**j
        j+=1
    return decimal

def DtoB(decimal):
    binary = []
    b = 0
    while decimal != 0 and decimal != 1:
        binary.append(decimal % 2)
        decimal //= 2
    if decimal == 1:
        binary.append(1)
    binary.reverse()
    for i in binary:
        b = (b*10) + i
    return b

def BtoOH(Binary,n):
    oc = []
    while len(Binary)!=0:
        temp = Binary[-1:-n-1:-1]
        if len(Binary)<n:
            for i in range(0,len(Binary)):
                Binary.pop()
        else:
            for i in range(0,n):
                Binary.pop()
        temp.reverse()
        o = BtoD(temp)
        oc.append(o)
    if n==4:
        return converter(oc)
    sum = 0
    for i in oc:
        sum = (sum*10) + i
    return sum

def converter(Octal):
    hexa = []
    for i in Octal:
        if i==10:
            hexa.append('A')
        elif i==11:
            hexa.append('B')
        elif i==12:
            hexa.append('C')
        elif i==13:
            hexa.append('D')
        elif i==14:
            hexa.append('E')
        elif i==15:
            hexa.append('F')
        else :
            hexa.append(str(i))
    Hexadecimal = ''
    for i in hexa:
        Hexadecimal += i
    return Hexadecimal

def OtoB(decimal):
    binary = []
    b = 0
    while len(decimal)!=0:
        binary.append(DtoB(decimal[-1]))
        decimal.pop()
    binary.reverse()
    for i in binary:
        b = (b*1000) + i
    return b

print("*="*25)

print("1. Binary to Decimal.")
print("2. Decimal to Binary.")
print("3. Binary to Octal.")
print("4. Octal to Binary.")
print("5. Binary to Hexadecimal.")
print("6. Hexadecimal to Binary.")

print("*="*25)
choice = int(input("Enter your choice: "))
print("*="*25)
if choice==1:
    binary = int(input("Enter your Binary No : "))
    Binary=[]
    while binary!=0:
        Binary.append(binary%10)
        binary //= 10
    print(BtoD(Binary))
elif choice==2:
    decimal = int(input("Enter your decimal no : "))
    binary=DtoB(decimal)
    print(binary)
elif choice==3:
    binary = int(input("Enter your binary no : "))
    Binary = []
    while binary!=0:
        Binary.append(binary%10)
        binary //= 10
    print(BtoOH(Binary,3))
elif choice==4:
    octal = int(input("Enter your octal no : "))
    decimal = []
    while octal!=0:
        decimal.append(octal%10)
        octal //= 10
    decimal.reverse()
    print(OtoB(decimal))
elif choice==5:
    binary = int(input("Enter your binary number: "))
    Binary = []
    while binary!=0:
        Binary.append(binary%10)
        binary //= 10
    print(BtoOH(Binary,4))
elif choice==6:
    pass
else:
    print("Invalid choice.")