def monotonic(lists):
    answers = []
    for sequence in lists:
        if len(sequence) < 2:
            raise ValueError
        increasing = all(i < j for i, j in zip(sequence, sequence[1:]))
        descreasing = all(i > j for i, j in zip(sequence, sequence[1:]))
        if increasing is True:
            answers.append("monotonically increasing")       
        elif descreasing is True:
            answers.append("monotonically descreasing")
        else:
            answers.append("neither")
    return answers

    

    
