vowel_string = 'aeiouAEIOU'
string_counter = 0
number_of_vowels = 0


while string_counter < len(s):
    
    if s[string_counter] in vowel_string:
        number_of_vowels +=1
    string_counter += 1

print 'Number of vowels: ' + str(number_of_vowels)