from collections import Counter # for character frequency counting

def is_anagram(s1, s2):
    """ (str, str) => bool
    Return True if s1 and s2 are anagrams

    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('admirer','married')
    True
    >>> is_anagram('bear','breach')
    False    
    """

    if len(s1) != len(s2): # check length
        return False
    else:
        if Counter(s1) == Counter(s2): # compare charecters counts
            return True
        else:
            return False

