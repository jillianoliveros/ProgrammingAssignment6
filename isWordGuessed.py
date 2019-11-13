def isWordGuessed (secretWord,lettersGuessed):
    secretWordList=list(secretWord)
    if secretWordList==lettersGuessed:
        ans=True
    else:
        ans=False
    return ans
        
    
