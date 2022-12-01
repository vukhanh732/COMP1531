from list_exercises import reverse_list, minimum, sum_list

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1
    assert minimum([10, 3, 2, 1]) == 1
    assert minimum([2, 2, 2, 2]) == 2

def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
    assert sum_list([1, 2, 3, 4, 5, 6, 7]) == 28

def test_negative():
    assert minimum([1, -2, -3, -4, -10]) == -10
    assert sum_list([1, -1]) == 0
    