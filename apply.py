def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
    
def absolute(arg):
    return abs(arg)
    
def inc(arg):
    return arg + 1

def square(arg):
    return arg * arg
    
li = [1, -4, 8, -9]
print applyToEach(li, absolute)