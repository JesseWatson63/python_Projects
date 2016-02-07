def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
    return_list = []
    try:
        return item / denom
    except ZeroDivisionError:
        if denom == 0:
            return denom
                
        
print FancyDivide([0, 2, 4], 0)