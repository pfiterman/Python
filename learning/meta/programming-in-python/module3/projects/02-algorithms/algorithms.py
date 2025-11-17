# Algorithm for a Palindrome

str = "racecar"

def isPalindrome(s):
    startIndex = 0
    endIndex = len(s) - 1

    while startIndex < endIndex:
        if s[startIndex] != s[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1

    return True

def isPalindrome2(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True

print(isPalindrome("racecar"))