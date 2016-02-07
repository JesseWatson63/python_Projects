MBq = 10
print_value = 0
counter = 0

while MBq > 0:
    print_value = MBq / 2
    # raw_input('press')
    MBq -= print_value
    print print_value
    print counter
    counter +=1
    if counter == 365:
        counter = 0
        print MBq
        print 'year'