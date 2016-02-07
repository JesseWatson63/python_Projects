def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret_word_list = []
    counter = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            secret_word_list.append(letter)
        else:
            secret_word_list.append(' _ ')
    return ''.join(secret_word_list)



print getGuessedWord('hello', 'abdkdkdl;s')