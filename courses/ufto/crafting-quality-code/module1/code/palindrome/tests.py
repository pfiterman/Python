import unittest
from palindrome_v1 import is_palindrome_v1, reverse
from palindrome_v2 import is_palindrome_v2
from palindrome_v3 import is_palindrome_v3
from palindrome_a1 import is_palindrome_a1
from palindrome_a2 import is_palindrome_a2
from palindrome_a3 import is_palindrome_a3

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

class TestIsPalindromeA1(unittest.TestCase):
    def test_is_palindrome_a1(self):
        self.assertTrue(is_palindrome_a1(''))
        self.assertTrue(is_palindrome_a1('n'))
        self.assertFalse(is_palindrome_a1('no'))
        self.assertTrue(is_palindrome_a1('oo'))
        self.assertFalse(is_palindrome_a1('noo'))
        self.assertTrue(is_palindrome_a1('noon'))
        self.assertTrue(is_palindrome_a1('madam'))
        self.assertTrue(is_palindrome_a1('racecar'))
        self.assertFalse(is_palindrome_a1('dented'))                         
        self.assertTrue(is_palindrome_a1('step on no pets'))
        self.assertFalse(is_palindrome_a1('Was it a car or a cat I saw'))
        self.assertTrue(is_palindrome_a1('12321'))
        self.assertFalse(is_palindrome_a1('123456'))

class TestIsPalindromeA2(unittest.TestCase):
    def test_is_palindrome_a2(self):
        #self.assertTrue(is_palindrome_a2(''))
        self.assertTrue(is_palindrome_a2('n'))
        self.assertFalse(is_palindrome_a2('no'))
        self.assertTrue(is_palindrome_a2('oo'))
        self.assertFalse(is_palindrome_a2('noo'))
        self.assertTrue(is_palindrome_a2('noon'))
        self.assertTrue(is_palindrome_a2('madam'))
        self.assertTrue(is_palindrome_a2('racecar'))
        self.assertFalse(is_palindrome_a2('dented'))                         
        self.assertTrue(is_palindrome_a2('step on no pets'))
        self.assertFalse(is_palindrome_a2('Was it a car or a cat I saw'))
        self.assertTrue(is_palindrome_a2('12321'))
        self.assertFalse(is_palindrome_a2('123456'))

class TestIsPalindromeA3(unittest.TestCase):
    def test_is_palindrome_a3(self):
        self.assertTrue(is_palindrome_a3(''))
        self.assertTrue(is_palindrome_a3('n'))
        self.assertFalse(is_palindrome_a3('no'))
        self.assertTrue(is_palindrome_a3('oo'))
        self.assertFalse(is_palindrome_a3('noo'))
        self.assertTrue(is_palindrome_a3('noon'))
        self.assertTrue(is_palindrome_a3('madam'))
        self.assertTrue(is_palindrome_a3('racecar'))
        self.assertFalse(is_palindrome_a3('dented'))                         
        self.assertTrue(is_palindrome_a3('step on no pets'))
        self.assertFalse(is_palindrome_a3('Was it a car or a cat I saw'))
        self.assertTrue(is_palindrome_a3('12321'))
        self.assertFalse(is_palindrome_a3('123456'))

if __name__ == "__main__":
    unittest.main()