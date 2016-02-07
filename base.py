def iterPower(base, exp):
    result = 1
    st = "hello world" if exp == 0 else 'not hello world'
    print st
    if exp == 0:
        result = 1
    else:
        while exp > 0:
            result *= base
            exp -= 1
    return result
    
print iterPower(-9.22, 9)
