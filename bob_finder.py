vowel_string = 'bob'
index_value = 0
number_of_bobs = 0
# Give a value for s and it will find bob.
for bob in s:
    if s[index_value:index_value+3].find(vowel_string) == 0:
        number_of_bobs += 1
    index_value += 1
    
print 'Number of times bob occurs is: ' + str(number_of_bobs)