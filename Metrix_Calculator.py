met1 = []
met2 = []
met3 = []
result = []
print("*"*30)
print("1.Add your metrixes: ")
print("2.Subtrack your metrixes: ")
print("3.Multiply your metrixes: ")
print("4.Divide your metrixes: ")
print("*"*30)
choice = int(input("Enter your choice: "))
print("*"*30)

if choice==1:

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
elif choice==2:
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
            met1[i].insert(j, int(input("Enter element: ")))
    print("*" * 30)
    print("Enter the second metrix: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met2[i].insert(j, int(input("Enter element: ")))

    for i in range(row):
        for j in range(column):
            result[i].append(met1[i][j] - met2[i][j])
    print("*" * 30)
    print("Subtraction first-second metrixes: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            print(f"{result[i][j]:4}", end=" ")
        print()
    print("*" * 30)
elif choice==3:
    column = int(input("Enter no. of column: "))
    row = int(input("Enter no. of row: "))
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met1.append([])
            met2.append([])
            met3.append([])
            result.append([])
    print("Enter the first metrix: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met1[i].insert(j, int(input("Enter element: ")))
    print("*" * 30)
    print("Enter the second metrix: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met2[i].insert(j, int(input("Enter element: ")))
    # Correct the operation in there loop
    for i in range(row):
        for j in range(column):
            temp = 0
            met3[i].append(0)

            for k in range(row):
                temp = (met1[i][k]*met2[k][j])+temp
                met3[i].insert(j,temp)
            temp=0

    print("Multiplication of your metrixes: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            print(f"{met3[i][j]:4}", end=" ")
        print()
    print("*" * 30)
elif choice==4:
    column = int(input("Enter no. of column: "))
    row = int(input("Enter no. of row: "))
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met1.append([])
            result.append([])
    print("Enter the metrix: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            met1[i].insert(j, int(input("Enter element: ")))

    print("*" * 30)
    dev = int(input("Enter device number: "))
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            result[i].insert(j,met1[i][j]//dev)
    print("*"*30)
    print("result Metrix: ")
    print("*" * 30)
    for i in range(row):
        for j in range(column):
            print(f"{result[i][j]:4}", end=" ")
        print()
    print("*" * 30)
else:
    print("*"*30)
    print("Wrong Input")
    print("*" * 30)
    print("Re-Run Your Program.")