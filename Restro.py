
foods = []
prices = []
total_bill = 0

while True:
    food = input("Enter your food (q to quite) :")
    if food.lower() == "q":
        break;
    else :
        price = float(input(f"Enter {food} price: INR"))
        foods.append(food)
        prices.append(price)

print("<------Your-Order------>")
for food in foods:
    print(food, end=" ")

for price in prices:
    total_bill += price
print()
print(f"Your total bill is {total_bill} INR")