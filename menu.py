menu = {
    "Pizza": 200,
    "Pasta": 100,
    "Pop corn": 80,
    "Noodles":130,
    "Dosa": 90,
    "Coca Cola": 100,
    "Soda":40,
    "Namkeen":35,
    "Chai": 15
}
order = []
total = 0
print("<---------- Menu ---------->")
for k,v in menu.items():
    print(f"{k:10} :{v:.1f} INR")
print("----------------------------")

while True:
    food = input("Enter food (q for Quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        order.append(food)
print("<------- Your Order ---------->")
for price in order:
    total += menu.get(price)
    print(f"{price}",end=" ")
print("\n")
print(f"Your total bill: {total} INR")