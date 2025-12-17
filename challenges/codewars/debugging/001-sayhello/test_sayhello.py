import unittest
from sayhello import say_hello

class TestSayHello(unittest.TestCase):
    def test_regular_name(self):
        """
        Test with a normal string      
        """
        self.assertEqual(say_hello("Pablo"), "Hello, Pablo")

    def test_empty_string(self):
        """
        Test with an empty string              
        """
        self.assertEqual(say_hello(""), "Hello, ")

    def test_special_characters(self):
        """
        Test with special characters in the name
        """
        self.assertEqual(say_hello("!@#$%^&*()"), "Hello, !@#$%^&*()")

    def test_numeric_name(self):
        """
        Test with numeric input converted to string
        """
        self.assertEqual(say_hello(str(123)), "Hello, 123")

if __name__ == "__main__":
    unittest.main()