import unittest
from palindrome_v1 import is_palindrome_v1, reverse
from palindrome_v2 import is_palindrome_v2
from palindrome_v3 import is_palindrome_v3
from palindrome_v4 import is_palindrome_v4

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('hello'),'olleh')

class TestIsPalindromeV1(unittest.TestCase):
    def test_is_palindrome_v1(self):
        self.assertTrue(is_palindrome_v1('noon'))
        self.assertTrue(is_palindrome_v1('racecar'))
        self.assertFalse(is_palindrome_v1('dented'))

class TestIsPalindromeV2(unittest.TestCase):
    def test_is_palindrome_v2(self):
        self.assertTrue(is_palindrome_v2('noon'))
        self.assertTrue(is_palindrome_v2('racecar'))
        self.assertFalse(is_palindrome_v2('dented'))

class TestIsPalindromeV3(unittest.TestCase):
    def test_is_palindrome_v3(self):
        self.assertTrue(is_palindrome_v3('noon'))
        self.assertTrue(is_palindrome_v3('racecar'))
        self.assertFalse(is_palindrome_v3('dented'))

class TestIsPalindromeV4(unittest.TestCase):
    def test_is_palindrome_v4(self):
        self.assertFalse(is_palindrome_v4('n'))
        # self.assertFalse(is_palindrome_v4('no'))
        # self.assertFalse(is_palindrome_v4('noo'))
        # self.assertTrue(is_palindrome_v4('noon'))
        # self.assertTrue(is_palindrome_v4('racecar'))
        # self.assertFalse(is_palindrome_v4('dented'))

if __name__ == "__main__":
    unittest.main()