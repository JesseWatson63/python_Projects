# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The playser has to guess the original word.

import random

# create a sequence of words to choose form
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# Pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print """
        Welcome to Word Jumble!

        Unscrambel the letters to make a word.
        (Press the enter key at the prompt to quit.)
    """
print "The jumble is: ", jumble

guess = raw_input("\nYour guess: ")
while guess != correct and guess != "":
    print "Sorry, that's not it."
    guess = raw_input("Your guess: ")

if guess == correct:
    print "Tha's it! You guessed it!\n"

print "Thanks for playing."

raw_input("\n\nPress the enter button to exit.")
