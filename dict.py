def biggest(aDict):
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
animals = {'a': [0, 8, 18, 8, 14, 18, 7], 'c': [3, 12, 5, 16, 3, 6], 'b': [12, 15, 20, 2]}        
        
        
print biggest(animals)