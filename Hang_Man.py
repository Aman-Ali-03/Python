import random
from Hello import word
gess_word = random.choice(word)
hanger = {
    0:("     ",
       "     ",
       "     "),
    1:("  o  ",
       "     ",
       "     "),
    2:("  o  ",
       "  |  ",
       "     "),
    3:("  o  ",
       " /|  ",
       "     "),
    4:("  o  ",
       " /|\\  ",
       "     "),
    5:("  o  ",
       " /|\\ ",
       " /   "),
    6:("  o  ",
       " /|\\ ",
       " / \\  "),
}

def display(a):
    print("*******")
    for x in hanger[a]:
        print(x)
    print("*******")

def hinte(hint):
    print(" ".join(hint))

def answer():
    print(gess_word)
def  main():
    gessing_Chance = 0
    guessed_letters = set()
    hint = ["_"] * len(gess_word)
    gessing = True
    while gessing:
        display(gessing_Chance)
        hinte(hint)
        guesses = input("Enter the letter: ").lower()

        if not guesses.isalpha() or len(guesses) != 1:
            print("Invalid input")
            continue
        if guesses in guessed_letters:
            print("You already guessed this letter")
            continue
        if guesses not in gess_word:
            print("Wronge guess.")
            gessing_Chance += 1

        if guesses in gess_word:
            for i in range(len(gess_word)):
                if gess_word[i] == guesses:
                    hint[i] = guesses

        if gessing_Chance == 6:
            display(6)
            print("**************************")
            print("You lose")
            print("**************************")
            print("The correct answer is :")
            answer();
            print("***************************")
            gessing = False

        if "_" not in hint:
            print("**************************")
            print("You won the game.")
            print("You guessed the right word.")
            print(f"Its {gess_word}")
            print("**************************")
            gessing = False

if __name__ == "__main__":
    main()