def divisors(n):
    if type(n) is not int or n <= 0:
      	raise ValueError("n is not a positive integer")
    result = set()
    for i in range(1, n + 1):
      	if n % i is 0:
        	result.add(i)
    return result

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A function that generates the prime factors of n. For example
    >>> factors(12)
    [2,2,3]

    Params:
      n (int): The operand

    Returns:
      List (int): All the prime factors of n in ascending order.

    Raises:
      ValueError: When n is <= 1.
    '''
    if type(n) is not int or n <= 1: 
        raise ValueError(f"{n} does not have prime factors")

    for f in sorted(divisors(n)):
        if n == 1:
            break
        if is_prime(f):
            while n != 1 and n % f == 0:
                yield f
                n = n // f
