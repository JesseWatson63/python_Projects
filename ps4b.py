def updateHand(hand, word):
    h = hand.copy()
    for letter in word:
        if h[letter] >= 0:
            h[letter] -= 1
    return h
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

def compChooseWord(hand, wordList, n):
    best_score = 0
    best_word = None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > best_score:
                best_score = score
                best_word = word
    return best_word

def compPlayHand(hand, wordList, n):
    def string_hand(hand):
        string_hand = ''
        for letter in hand.keys():
            for i in range(hand[letter]):
                string_hand += letter + ' '
        return string_hand
    score = 0
    this_hand = hand.copy()
    while compChooseWord(this_hand, wordList, n):
        print "Current Hand: " + string_hand(this_hand)
        computer_word = compChooseWord(this_hand, wordList, n)
        word_score = getWordScore(computer_word, n)
        score += word_score
        print '"' + computer_word + '"', "earned", word_score, "points. Total: ", score, "poins\n"
        this_hand = updateHand(this_hand, computer_word)
    if sum(this_hand.values()) != 0:
        print 'Current Hand:', string_hand(this_hand)
    print 'Total score: ', score, ' points'



compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, 'apples', 6)
