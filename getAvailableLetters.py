def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining_letters = []
    for letter in alphabet:
        if letter not in lettersGuessed:
            remaining_letters.append(letter)
    return ''.join(remaining_letters)
print getAvailableLetters('ahndloem')