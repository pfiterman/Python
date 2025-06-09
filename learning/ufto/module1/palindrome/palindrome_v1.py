from reverse import reverse

def is_palindrome_v1(s):
    """ (str) -> bool
    Return True if and only if s us a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    return reverse(s) == s