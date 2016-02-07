import random
import string
import sys
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"
def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


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


def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,
    print


def dealHand(n):
    hand={}
    numVowels = n / 3
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand


def updateHand(hand, word):
    h = hand.copy()
    for letter in word:
        if h[letter] >= 0:
            h[letter] -= 1
    return h


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


def calculateHandlen(hand):
    hand_count = 0
    for letter in hand:
        if hand[letter] != 0:
            hand_count += hand[letter]
    return hand_count


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
        print 'Hand passed to playHand:', hand_string
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            print 'Goodbye! Total score: ', score
            break
        else:
            if isValidWord(word, hand, wordList) == False:
                print'Invalid word, please try again. \n'
            else:
                score += getWordScore(word, n)
                print '"'+ word+ '"', 'earned ', getWordScore(word, n), 'points. Total:', score, 'points\n'
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand

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

def playGame(wordList):
    word = wordList
    store_hand = {}
    hand = ''
    def word_loader():
        hand = dealHand(HAND_SIZE)
        store_hand.clear()
        store_hand.update(hand)
        return hand
    while True:
        user_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_input == 'n':
            hand = word_loader()
            while True:
                comp_or_player = raw_input("Enter u to have yourself play, c to have the computer play:")
                if comp_or_player == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                elif comp_or_player == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif user_input == 'r':
            if store_hand == {}:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                comp_or_player = raw_input("Enter u to have yourself play, c to have the computer play:")
                while True:
                    if comp_or_player == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    elif comp_or_player == 'u':
                        playHand(store_hand, wordList, HAND_SIZE)
                        break
                    else:
                        print 'Invalid command.'
        elif user_input == 'e':
            break
        else:
            print 'Invalid command.'

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
