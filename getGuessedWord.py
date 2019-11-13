def getGuessedWord(secretWord,lettersGuessed):
    char=[]
    for letter in secretWord:      
        if letter in lettersGuessed:    
            char.append(letter)
        else:
            char.append(" _ ")
    ans="".join(char)
    return ans
    
