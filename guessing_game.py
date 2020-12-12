## Unit 1 - Python Tech Degree 
# Put this in a Github repo (by itself), with a README.

import random
def main():
    
### Meets expectations:

#As a player of the game, I should see a some kind of text header, welcome or game intro message.
    print('Welcome to my guessing game...')

#A random number should be chosen that is within the range.
    randomNumber = random.randint(1,20)
    found = False
    numGuesses = 0 
    print("Guess a number between 1 and 20: ")
    while not found:
#As a player of the game, I should be continuously prompted for a guess until I get it right.
        userGuess= int(input("What's your guess? "))
        
#Make sure your script runs without errors. 
#Catch exceptions and report errors to the user in a meaningful way.
        #try:
         #   if type(userGuess) != int:
        #except:
        #print("Please supply an integer") 
#As a player of the game, after an incorrect guess I should be told if my answer is 
#higher or lower than the answer, so that I can narrow down my guesses.
  
        if userGuess == randomNumber:
            print ("You guessed correctly!")
            found = True
            numGuesses = numGuesses + 1
            print(numGuesses)
        # give the user a hint
        elif userGuess > randomNumber:
            print ("Guess lower...")
            numGuesses = numGuesses + 1
            print(numGuesses)
        else:
            print ("Guess higher...")
            numGuesses = numGuesses + 1
            print(numGuesses)

#As a player of the game, after the game ends I should be shown my number of attempts at guessing.
    print("you got it in", numGuesses,"guesses!") 


#When the game ends, an ending message is shown to the player.
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