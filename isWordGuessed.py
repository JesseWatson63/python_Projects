def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    counter = 0
    letters = ''.join(sorted(lettersGuessed))
    letter_duplicate = ''
    for letter in letters:
        if letter in secretWord:
            counter += 1
            letter_duplicate = letter
    if counter == len(secretWord):
        return True
    else:
        return False
            
            
print isWordGuessed('hello', 'abcdefghijklmnopqrstuvwxyz')