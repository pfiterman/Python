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

if __name__ == "__main__":
    print("In version 1, the module name is ", __name__)

    word = input("Enter a word: ")
    if is_palindrome_v1(word):
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")