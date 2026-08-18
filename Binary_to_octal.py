binary = int(input("Enter your binary number: "))
Binary = []
while binary!= 0:
    Binary.append(binary%10)
    binary //= 10
Binary.reverse()
second = []
octal = []
while len(Binary)>0:
    second = Binary[-1:-4:-1]
    if len(Binary)>2:
        for i in range(0,3):
            Binary.pop()
    else:
        for i in range(0,len(Binary)):
            Binary.pop()
    temp = 0
    j=0
    for i in second:
        if i==1:
            temp = temp+ pow(2,j)
        j+=1
    octal.append(temp)
    second.clear()
    temp=0
    j=0
octal.reverse()
Octal = 0
for i in octal:
    Octal = (Octal*10) + i
print(Octal)