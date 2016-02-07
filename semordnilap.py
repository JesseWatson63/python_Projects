
def semordnilap(str1, str2):
    new_string2 = str2
    new_string1 = str1
    if len(new_string1) == len(new_string2):
        if len(new_string1) == 1 and len(new_string2):
            return True
        if new_string1[0] == new_string2[0]:
            return semordnilap(new_string1[1:], new_string2[1:])
        else:
            return False
    else:
        return False

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False
    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
    str2 = str2[::-1]
    return semordnilap(str1, str2)


print semordnilapWrapper('palindrome', 'emordnilap')