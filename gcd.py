def gcdIter(a, b):
    if a > b:
        c = a
        a = b
        b = c
    return_number = 0
    for number in range(1, b):
        if (a % number == 0) and (b % number == 0):
            new_number = number
            if new_number > return_number:
                return_number = new_number
    return return_number

print gcdIter(7, 84)