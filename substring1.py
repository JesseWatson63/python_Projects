alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = 'abcshfdgflmno'
save_string_current = ''
save_string_high = ''
slice_one = 0
slice_two = 2

def string_test(string):
    if string in alphabet:
        return True
       
for letter in s:
    if string_test(s[slice_one: slice_two]):
        save_string_current = s[slice_one: slice_two]
        slice_two += 1
        if len(save_string_current) > len(save_string_high):
            save_string_high = save_string_current
            save_string_current = ''
    else:
        slice_one += 1
        slice_two += 1

        
print 'Longest substring in alphabetical order is: ' + save_string_high
