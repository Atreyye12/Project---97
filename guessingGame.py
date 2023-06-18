import random
print("NUMBER GUESSING GAME")
number = random.randint(1,9)
chances = 0
print("Guess a number: ")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations you won")
    elif guess < number:
        print("You guess was too low", guess)
    else:
        print("Your guess was too high", guess)
    chances += 1

if not chances < 5: 
    print("You lost the game", number)

