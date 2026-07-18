def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b
def floor(a,b):
    return a//b

a = float(input("Enter your first number: "))
b = float(input("Enter your second value: "))

print("Add: ",add(a,b))
print("Subtract: ",sub(a,b))
print("Multiply: ",mul(a,b))
print("Division: ",div(a,b))
print("Power(a^b): ",pow(a,b))
print("Flood Divide: ",floor(a,b))