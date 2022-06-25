import random
print("-------------WELCOME TO GUESSING GAME BUDDIES--------------")

top_of_range = input("Type a range for the number from 0 to : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("Huhhooooo!!! You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!\n")
    else:
        print("You were below the number!\n")

print("\nCongratulations!!You got it in", guesses, "guesses.")
