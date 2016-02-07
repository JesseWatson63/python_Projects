def recurPowerNew(base, exp):
    if exp == 0:
        base = 1
        return base
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        print 'even'
        return (base * base) *  recurPowerNew(base, (exp/2))
    elif exp % 2 != 0:
        print 'odd'
        return base * recurPowerNew(base, exp-1)

print recurPowerNew(7.42, 10)

