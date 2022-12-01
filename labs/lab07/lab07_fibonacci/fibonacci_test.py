import pytest
from fibonacci import fibonacci


def test():
    nums = list(fibonacci(10))
    assert nums == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
