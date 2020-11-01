# NUMBER GUESSING GAME!!!
# randomly generate a number between 1 and 100 and let the player
# try to guess what the number is. Let them know if they are higher
# or lower than the generated number until they get it right!
# import random
import random
# set the random number for the player to guess and the amount of guesses
# the player has taken
guesses = 0
randomNumber = random.randint(1, 100)

# Start the game!
print("####### RANDOM NUMBER GUESSING GAME #######")
print("####### GUESS A NUMBER BETWEEN 1 AND 100 #######")
print("####### YOU HAVE 7 GUESSES TO GET IT RIGHT! #######")
while guesses < 5:
    guess = input()
    guess = int(guess)
    guesses += 1

    if guess < randomNumber:
        print("Too Low! Try Again...")
    elif guess > randomNumber:
        print("Too High! Try Again...")
    else:
        break

if guess == randomNumber:
    print(" YOU'VE GUESSED THE NUMBER! ")

if guess != randomNumber:
    randomNumber = str(randomNumber)
    print("You've taken too long to guess. The nunber was: " + randomNumber)
