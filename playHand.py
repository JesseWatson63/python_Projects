def isValidWord(word, hand, wordList):
    h = hand.copy()
    counter = 0
    if word in wordList:
        for letter in word:
            if letter in h:
                counter += 1
                if h[letter] != 0:
                    h[letter] -= 1
                else:
                    return False
    if counter == len(word):
        return True
    else:
        return False

def getWordScore(word, n):
    return_score = 0
    SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    for letter in word:
        return_score += SCRABBLE_LETTER_VALUES[letter]

    return_score *= len(word)
    if len(word) == n:
        return_score += 50
    return return_score

def updateHand(hand, word):
    h = hand.copy()
    for letter in word:
        if h[letter] >= 0:
            h[letter] -= 1
    return h

def playHand(hand, wordList, n):
    score = 0
    while n > 0:
        hand_string = ''
        for letter in hand:
            if hand[letter] != 0:
                hand_string += letter + ' '
        if hand_string == '':
            print 'Run out of letters. Total score:', score, 'points.'
            break
        # Display the hand
        print 'Current Hand:', hand_string

        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == '.':
            print 'Goodbye! Total score: ', score
            break
            # End the game (break out of the loop)
        else:
        # Otherwise (the input is not a single period):
            if isValidWord(word, hand, wordList) == False:
            # If the word is not valid:
                print'Invalid word, please try again. \n'
                # Reject invalid word (print a message followed by a blank line)
            else:
            # Otherwise (the word is valid):
                score += getWordScore(word, n)
                print '"'+ word+ '"', 'earned ', getWordScore(word, n), 'points. Total:', score, 'points\n'
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand



    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

WORDLIST_FILENAME = "words.txt"
playHand({'a': 1, 'c': 1, 'r': 2, 't': 1, 'o': 1}, 'carrot', 6)