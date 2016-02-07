def oddTuples(aTup):
    count_number = 0
    new_tup = ()
    if aTup == ():
        return ()
    for num in aTup:
        new_tup += (aTup[count_number],)
        count_number += 2
        if count_number >= len(aTup):
            return new_tup
            break
