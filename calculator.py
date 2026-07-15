num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operater = input("Enter your operater: ")
if operater == "+":
    c=num1+num2
    print(f"Addition of {num1} and {num2} is : {c}")
elif operater == "-":
    c=num1-num2
    print(f"Subtraction of {num1} and {num2} is : {c}")
elif operater == "*":
    c=num1*num2
    print(f"Multiplication of {num1} and {num2} is : {c}")
elif operater == "/":
    c=num1/num2
    print(f"Division of {num1} and {num2} is : {c}")
else :
    print(f"{operater} is not valid.")