from reverse import reverse

def is_palindrome_v2(s):
    """ (str) -> bool
    Return True if and only if s us a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """
    # The number of chars in s
    n = len(s)

    # Compare the firs half of s to the reverse of the seconf half
    # Omit the middle characted of an odd-length string
    return s[:n // 2] == reverse(s[n - n // 2:])