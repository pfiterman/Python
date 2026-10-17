import unittest
from digits import digits

class TestDigits(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(digits('ab1223cd34'),'122334')

if __name__ == "__main__":
    unittest.main()