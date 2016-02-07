def radiationExposure(start, stop, step):
    return_amount = 0.0
    new_start = start

    def f(x):
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)

    while(new_start < stop):
        return_amount += step * f(new_start)
        new_start += step
        print
    return return_amount

print radiationExposure(0, 5, 1)