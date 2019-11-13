import string 
def getAvailableLetters(lettersGuessed):
    result=[]
    alphabet=string.ascii_lowercase
    for letter in alphabet:
        if letter not in lettersGuessed:
            result.append(letter)
    ans1 ="".join(result)
    return ans1
            
