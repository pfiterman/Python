def is_palindrome_a3(s):
    """ (str) -> bool
    Return True if and only if s us a palindrome.

    >>> is_palindrome_a3('noon')
    True
    >>> is_palindrome_a3('racecar')
    True
    >>> is_palindrome_a3('dented')
    False
    """
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False
    return True