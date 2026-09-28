from Hello import word
main_character = {
    0:(" _____  ",
       " |   |  ",
       " |      ",
       " |      ",
       " |      ",
       "--------"),
    1:(" _____  ",
       " |   |  ",
       " |   O  ",
       " |      ",
       " |      ",
       "--------"),
    2:(" _____  ",
       " |   |  ",
       " |   O  ",
       " |   I  ",
       " |      ",
       "--------"),
    3: (" _____  ",
       " |   |  ",
       " |   O  ",
       " |  /I  ",
       " |      ",
       "--------"),
    4: (" _____  ",
       " |   |  ",
       " |   O  ",
       " |  /I\\ ",
       " |      ",
       "--------"),
    5: (" _____  ",
       " |   |  ",
       " |   O  ",
       " |  /I\\ ",
       " |  /   ",
       "--------"),
    6: (" _____  ",
       " |   |  ",
       " |   O  ",
       " |  /I\\ ",
       " |  / \\ ",
       "--------"),
}
import random
guess_word = random.choice(word)
def printer(num):
    for i in main_character[num]:
        print(i)
def unknown(word):
    print(" ".join(word))
def main():
    wrong = 0
    guest = ''
    word = ["_"]*len(guess_word)
    while True:
        printer(wrong)
        unknown(word)
        user_guess = input("Enter your letter: ")
        if len(user_guess)>1:
            print("Invalid input.")
        if user_guess in word:
            print("You already guess this letter.")
        if user_guess in guess_word:
            for i in range(len(guess_word)):
                if user_guess == guess_word[i]:
                    word[i] = user_guess
        if user_guess not in guess_word:
            print("Wronge Guess.")
            wrong += 1
        if wrong >=6:
            printer(wrong)
            print("You losse.")
            print(f"The Right answer is {guess_word}")
            break
        if "_" not in word:
            print("You Won The Game")
            print(f"You guess the right word its {guess_word}")
            break
if __name__=="__main__":
    main()