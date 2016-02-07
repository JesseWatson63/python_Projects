x = 100
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
answer = False
high_low_question = "\n\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "

raw_input("\n\nPlease think of a number between 0 and 100!")

while answer == False:
    print("\n\nIs your number " + str(int(ans)) + "?")
    user_hl_answer = raw_input(high_low_question)
    if user_hl_answer == 'l':
        num_guesses += 1
        low = ans
    elif user_hl_answer == 'h':
        high = ans
        num_guesses += 1
    elif user_hl_answer == 'c':
        print'\n\nGame over. Your secret number was: ' + str(int(ans))
        break
    else:
        print'I did not understand.'
        
    ans = (high + low)/2.0
