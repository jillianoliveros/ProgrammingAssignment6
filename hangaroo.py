from num1 import isWordGuessed
from num2 import getGuessedWord
from num3 import getAvailableLetters
def hangaroo(secretWord):
    mistakes = 0
    lettersGuessed=[]
    secretWord=secretWord.lower()
    secretWordList=list(secretWord)
    print("Hello! Welcome to Hangaroo!")
    while isWordGuessed(secretWord,lettersGuessed) != True:
        userGuess=input("Guess a letter: ")
        userGuess=userGuess.lower()
        if userGuess not in lettersGuessed and userGuess in secretWordList:
            lettersGuessed.append(userGuess)
            print("You made a right guess!")
            print((getGuessedWord(secretWord,lettersGuessed)),(getAvailableLetters(lettersGuessed)))
        elif userGuess not in secretWord:
            print("You made a wrong guess.")
            print((getGuessedWord(secretWord,lettersGuessed)),(getAvailableLetters(lettersGuessed)))
            lettersGuessed.append(userGuess)
            mistakes += 1
        elif userGuess in lettersGuessed:
            print("You already guessed that letter.")
            print((getGuessedWord(secretWord,lettersGuessed)),(getAvailableLetters(lettersGuessed)))
            mistakes += 1
        else:
            print("Pick you letters well!")
            print((getGuessedWord(secretWord,lettersGuessed)),(getAvailableLetters(lettersGuessed)))
        if 5 - mistakes == 0:
        	print("You ran out of guesses with",mistakes,"mistakes. The secret word was", secretWord, ".")
        	break
        else:
        	continue
    else: 
        print("You won the game with",mistakes,"mistakes. Congratulations!")
    
