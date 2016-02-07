# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
letters_guesse = ''
number_of_guesses = 8
available_letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def getGuessedWord(secretWord, lettersGuessed):
    # FILL IN YOUR CODE HERE...
    secret_word_list = []
    printable_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            secret_word_list.append(letter)
            printable_word = ''.join(secret_word_list)
        elif letter not in lettersGuessed:
            secret_word_list.append(' _ ')
    return ''.join(secret_word_list)



def isWordGuessed(secretWord, lettersGuessed):
    # FILL IN YOUR CODE HERE...
    word_guessed_counter = 0
    letters = ''.join(sorted(lettersGuessed))
    for letter in letters:
        if letter in secretWord:
             word_guessed_counter += 1
    print secretWord, lettersGuessed
    if  word_guessed_counter == len(secretWord):
        return True
    else:
        return False


def getAvailableLetters(lettersGuessed):
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining_letters = []
    for letter in alphabet:
        if letter not in lettersGuessed:
            remaining_letters.append(letter)
    return ''.join(remaining_letters)


def display_correct_or_not(letter, word):
    if letter in word:
        return 'Good guess: '
    else:
        return 'Oops! That letter is not in my word:'
 
 
 
 
 
 
        
def hangman(secretWord):
    number_of_guesses = 8
    letters_guessed = []
    temp_letter = ''
    print"Welcome to the game, Hangman!"
    print 'I am thikning of a word that is', len(secretWord), 'letters long'
    print '-----------'
    
    while number_of_guesses >= 0:
        if number_of_guesses == 0:
            print 'Sorry, you ran out of guesses. The word was ', secretWord
            break
        print'You have', number_of_guesses, 'guesses left'
        
        print 'Available letters:', getAvailableLetters(letters_guessed)
        
        temp_letter = raw_input('Please guess a letter: ')
        temp_letter = temp_letter.lower()
        if temp_letter in letters_guessed:
            print"Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters_guessed)
            print '-----------'
        else:
            letters_guessed.append(temp_letter)

            print display_correct_or_not(temp_letter, secretWord), getGuessedWord(secretWord, letters_guessed)
            print '-----------'
            if display_correct_or_not(temp_letter, secretWord) == 'Oops! That letter is not in my word:':
                number_of_guesses -= 1
        if '_' not in getGuessedWord(secretWord, letters_guessed):
            print 'Congratulations, you won!'
            break

hangman(chooseWord(wordlist))