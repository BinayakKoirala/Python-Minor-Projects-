print("---------------WELCOME TO FOOTBALL QUIZ----------------")

playing = input("\nHey, You wanna score some quiz goals ? ")

if playing.upper() != "YES":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("\nWhere is 2022 Fifa World Cup going to be held ? \n")
if answer.upper() == "QATAR":
    print('--------------Correct!-----------------')
    score += 1
else:
    print("--------------Incorrect!------------------")

answer = input("\nWhich football club does CFC stand for ?\n")
if answer.upper() == "CHELSEA FOOTBALL CLUB":
    print('--------------Correct!-----------------')
    score += 1
else:
    print("--------------Incorrect!------------------")

answer = input("\nWhich country has won most number of worldcup ?\n")
if answer.upper() == "BRAZIL":
    print('--------------Correct!-----------------')
    score += 1
else:
    print("--------------Incorrect!------------------")

answer = input("\nWho is the most expensive player till now ?\n")
if answer.upper() == "MBAPPE":
    print('--------------Correct!-----------------')
    score += 1
else:
    print("--------------Incorrect!------------------")


answer = input("\nWho is known as the GOAT of football ?\n")
if answer.upper() == "MESSI":
    print('--------------Correct!-----------------')
    score += 1
else:
    print("--------------Incorrect!------------------")

print("\nYou got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

print("\n-----Thanks for playing the game. Keep Scoring------")
