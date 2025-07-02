import unittest
from vowels import collect_vowels, count_vowels

class TestVowels(unittest.TestCase):
    def test_collect_vowels(self):
        self.assertEqual(collect_vowels("Fappy Anniversary!"),"aAiea")
        self.assertEqual(collect_vowels("xyz"),"")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Happy Anniversary!"), 5)
        self.assertEqual(count_vowels("xyz"),0)

if __name__ == "__main__":
    unittest.main()