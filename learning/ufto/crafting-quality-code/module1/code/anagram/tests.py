import unittest
from anagram import is_anagram

class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram('listen','silent'))
        self.assertTrue(is_anagram('admirer','married'))
        self.assertFalse(is_anagram('bear','breach'))

if __name__ == "__main__":
    unittest.main()