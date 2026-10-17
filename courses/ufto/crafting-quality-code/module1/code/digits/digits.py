def digits(s):
    """ (str) -> str of digits
    
    Return a string of digits

    >>> digits('ab1223cd34')
    122334
    """
    digits = ""

    for i in range(len(s)):
        if s[i].isdigit():
            digits = digits + s[i]
    
    return digits