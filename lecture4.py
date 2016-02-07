vowel_string = 'aeiouAEIOU'
string_conter = 0
number_of_vowels = 0
s = 'hello how are you doing today?'
while True:
    if vowel_string[string_counter] == s:
        number_of_vowels +=1
        string_counter += 1
    elif string_counter == s:
        break
print 'Number of vowels: ' + str(number_of_vowels
        