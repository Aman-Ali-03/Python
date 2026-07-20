import random
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
user_score = 0
computer_score = 0
print("<----------Rock Paper Scissors---------->\n")
while True:
    user = input("Please Enter your's (Rock Paper Scissors)(Q to Quite): ")
    if user.lower() == "q":
        break;
    if computer.lower() == user.lower():
        print(f"Tie Game, Both are same {computer} and {user}")
        computer = random.choice(options)
    elif user.lower()  == "rock" and computer.lower() == "paper":
        print(f"Computer wins! your :{user}, computer :{computer}")
        computer_score += 1
        computer = random.choice(options)
    elif user.lower() == "paper" and computer.lower() == "rock":
        print(f"You win! your :{user}, computer :{computer}")
        user_score += 1
        computer = random.choice(options)
    elif user.lower() == "paper" and computer.lower() == "scissors":
        print(f"Computer wins! your :{user}, computer :{computer}")
        computer_score += 1
        computer = random.choice(options)
    elif user.lower() == "scissors" and computer.lower() == "paper":
        print(f"You win! your :{user}, computer :{computer}")
        user_score += 1
        computer = random.choice(options)
    elif user.lower() == "scissors" and computer.lower() == "rock":
        print(f"Computer wins! your :{user}, computer :{computer}")
        computer_score += 1
        computer = random.choice(options)
    elif  user.lower() == "rock" and computer.lower() == "scissors":
        print(f"You win! your :{user}, computer :{computer}")
        user_score += 1
        computer = random.choice(options)
    else:
        print("Invalid Input.")
print("<---------- Score ---------->\n")
print(f"You won {user_score} out of {computer_score+user_score} .")
print("<--------------------------->")
if user_score < computer_score:
    print("Computer wins! entire game")
elif user_score > computer_score:
    print("You win! entire game")
else:
    print("Draw game")