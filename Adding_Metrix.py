met1 = []
met2 = []
result = []

column = int(input("Enter no. of column: "))
row = int(input("Enter no. of row: "))
print("*" * 30)
for i in range(row):
    for j in range(column):
        met1.append([])
        met2.append([])
        result.append([])
print("Enter the first metrix: ")
print("*" * 30)
for i in range(row):
    for j in range(column):
        met1[i].insert(j,int(input("Enter element: ")))
print("*" * 30)
print("Enter the second metrix: ")
print("*" * 30)
for i in range(row):
    for j in range(column):
        met2[i].insert(j,int(input("Enter element: ")))

for i in range(row):
    for j in range(column):
        result[i].append(met1[i][j]+met2[i][j])
print("*" * 30)
print("Addition of your metrixes: ")
print("*" * 30)
for i in range(row):
    for j in range(column):
        print(f"{result[i][j]:4}", end=" ")
    print()
print("*" * 30)