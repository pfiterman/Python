def is_palindrome_v4(s):
    """ (str) -> bool
    Return True if and only if s us a palindrome.

    >>> is_palindrome_v4('noon')
    True
    >>> is_palindrome_v4('racecar')
    True
    >>> is_palindrome_v4('dented')
    False
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

