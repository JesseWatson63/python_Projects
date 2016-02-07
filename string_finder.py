def isIn(char, aStr):
    
    high = len(aStr)
    low = 0
    middle_number = high / 2
    new_string = sorted(aStr)
    # print len(aStr)
    # print middle_number
    # print new_string[middle_number]
    if not aStr or not char:
        return False
    if char == aStr[middle_number] or char == aStr[0]:
        return True
    elif char != aStr[middle_number] and len(aStr) <=2:
        return False
    elif char > new_string[middle_number]:
        return isIn(char, new_string[middle_number: high])
    elif char < new_string[middle_number]:
        return isIn(char, new_string[low: middle_number])

print isIn("b", '')