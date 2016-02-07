import random
import string
import sys
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

def playGame(wordList):
    def dealer():
        return dealHand(HAND_SIZE)
    hand = dealer()
    user_input = raw_input("Enter n to deal a new hand, r to replay last hand, or e to end game: ")
    if user_input == 'n':
        hand = dealer
        print'Hand passed to playHand: ', hand
        playHand(hand, wordList, n)
    if user_input == 'r':
        playHand(hand, wordList, n)
    if user_input == 'e':
        sys.exit()


playGame('hello')