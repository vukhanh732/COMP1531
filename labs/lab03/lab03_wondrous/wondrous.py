def wondrous(start):
    '''
    Returns the wondrous sequence for a given number.
    '''
    current = start
    sequence = [current]
    if current < 1:
        raise Exception(f"Invalid number")
    while current > 1:
        if (current % 2 == 0):
            current //= 2
        else:
            current = (current * 3) + 1
        sequence.append(current)
        

    return sequence

