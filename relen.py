def lenRecur(aString, letter_counter = 0):
    new_string = aString
    letter_counter += 0
    if new_string:
        pos = 0
        new_string = aString[0:pos]+aString[pos+1:]
        letter_counter +=1
        return lenRecur(new_string, letter_counter)
    else:
        return letter_counter
print lenRecur('hello how are you')
        