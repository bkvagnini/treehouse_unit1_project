## Unit 1 - Python Tech Degree
# Put this in a Github repo (by itself), with a README.

import random
def main():
    print('Welcome to my guessing game...')

    randomNumber = random.randint(1,20)
    found = False
    numGuesses = 0
    userGuess = 0
    print("Guess a number between 1 and 20: ")
    while not found:

        try:
            userGuess = int(input("What's your guess? "))
            #print(type(userGuess))
            #print(type(randomNumber))
        except ValueError as e:
            print ("Please supply an integer")
            #print (e)

        if userGuess == randomNumber:
            print ("You guessed correctly!")
            found = True
            numGuesses = numGuesses + 1
            print(numGuesses)
        elif userGuess > randomNumber:
            print ("Guess lower...")
            numGuesses = numGuesses + 1
            print(numGuesses)
        else:
            print ("Guess higher...")
            numGuesses = numGuesses + 1
            print(numGuesses)

    print("you got it in", numGuesses,"guesses!")
    print("Thanks for playing my game!")

#-----------------#
### Exceeds expectations:
#As a player of the game, my guess should be within the number range.
# If my guess is outside the guessing range I should be told to try again.


#As a player of the game, after I guess correctly I should be prompted if I would like to play again.

#As a player of the game, at the start of each game I should be shown the current high score
#(least amount of points) so that I know what I am supposed to beat.

#Every time a player decides to play again, the random number to
#guess is updated so players are guessing something new each time.
if __name__== "__main__":
    main()
