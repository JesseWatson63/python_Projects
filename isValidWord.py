WORDLIST_FILENAME = "words.txt"

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

hand = {'a': 3, 'e': 1, 'p': 2, 'r': 2, 'u': 1, 't': 1}

print isValidWord('rapture', hand, 'acdhellorapture')