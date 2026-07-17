import random
random = random.randint(1,100)
guess = -1
score = 0
print("<----------------------------------->")
print("       Welcome to Number Guess")
print("<----------------------------------->")
print("Guess the number b/w 1 to 100.\n")
while guess != random:
    guess = int(input("Guess the number: "))
    if guess.isdigit():
        if guess > 100 or guess < 1:
            print("Invalid range of number.")
            print("Please a number between 1 and 100")
        else :
            if guess < random:
                print("You guessed too low.")
                score += 1
            elif guess > random:
                print("You guessed too high.")
                score += 1
            else :
                print("You guessed too strong")
                score += 1
    else :
        print("Invalid input")
        print("Please a number between 1 and 100")

print(f"You guessed {score} times.")