def gcd(a, b):
    """Returns the Greatest Common Divisor of the two integers
    passed as arguments.

    Args:
      a: an integer
      b: another integer

    Returns: Greatest Common Divisor of a and b

    >>> gcd(48, 64)
    16
    >>> gcd(44, 19)
    1
    """
    if b == 0:
        return b
    return gcd(b, a%b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
