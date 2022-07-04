from os import system
import random


def cls():
    system('cls')


def hangman_game():
    cls()

    print("\n-------------Welcome to the Binayak's Football World-------------")
    print("Lets play Hangman but it's FOOTBALL EDITION.\n")

    name = input("What is your name?")
    name = name.capitalize()
    print("Hello " + name + ", It is time to play HangMan")
    print("Start Guessing...")
    guessed_word = []
    guesses = ""

    turns = 8  # ToDo : Change the turns that you want to give the player

    words = [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Mesut Ozil",
        "Thomas Muller",
        "Didier Drogba",
        "Wayne Rooney",
        "Mason Mount",
        "Peter Cech",
        "Antoine Griezmann",
        "Paul Pogba",
        "Maradona",
        "Virgil Van Djik",
        "Pep Guardiola",
        "Karim Benzema",
        "Jack Grealish",
        "Kiran Chemjong",
        "Bimal Gharti Magar",
        "Kevin De Bryune"
        "Ngolo Kante"
        "Sadio Mane"
        "Son Heung Min"
        "Robert Lewandowski"
        "Erling Haaland"
        "Riyad Mahrez"
        "Joshua Kimmich"
        "Andres Iniesta"
        "Luka Modric"
        "Zlatan Ibrahimovic"
        "Cesar Azpilceuta"
        "Zinedine Zidane"
        "Antonio Rudiger"
        "Alison Becker"
        "Rohit Chand"
        "Nawayug Shrestha"
    ]

    word = random.choice(words)
    word = word.upper()

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")

            elif char == " ":
                print(' / ', end=" ")

            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\nHURRAYYY " + name + " you WON!!!     ")
            break

        guess = input("\nGuess a Character : ")
        guess = guess.upper()

        if len(guess) > 1:
            break

        guesses += guess
        if (guess not in word) and (guess not in guessed_word):
            turns -= 1
            guessed_word.append(guess)
            print("\nSorry, Wrong Guess.")
        cls()

        print("\nYou have ", + turns, "more guesses")
        print("\nWrong Character's Entered : ", guessed_word)

        if turns == 0:
            print("\nGame is OVER, you LOST. The correct word was:", word)

    check = input("\nThanks for playing. Do you want to play again Y/N?")

    if check == "Y" or check == "y":
        hangman_game()


hangman_game()
