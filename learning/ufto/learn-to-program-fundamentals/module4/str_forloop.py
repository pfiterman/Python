s = "Hi there!"

for char in s:
    print(char)

def count_vowels(s):
    """ (str) -> int
    Return the number of vowels in s. Do not treat the letter y as a vowel.

    >>> count_vowels("Happy Anniversary!")
    5
    >>> count_vowels("xyz")
    0
    """
    num_vowels = 0
    for char in s:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels

print(count_vowels("Happy Anniversary!")) # 5
print(count_vowels("xyz")) # 0


def collect_vowels(s):
    """ (str) -> str
        Return the vowels from s. Do not treat the letter y as a vowel

        >>> collect_vowels("Happy Anniversary!")
        "aAiea"
        >>> collect_vowels("")
        0
    """
    vowels = ""
    for char in s:
        if char in "aeiouAEIOU":
            vowels = vowels + char
    return vowels

print(collect_vowels("Happy Anniversary!")) #  "aAiea"
print(collect_vowels("")) # ""