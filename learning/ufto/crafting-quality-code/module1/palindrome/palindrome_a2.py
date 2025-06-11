def is_palindrome_a2(s):
    """ (str) -> bool
    Return True if and only if s us a palindrome.

    >>> is_palindrome_a2('noon')
    True
    >>> is_palindrome_a2('racecar')
    True
    >>> is_palindrome_a2('dented')
    False
    """
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True