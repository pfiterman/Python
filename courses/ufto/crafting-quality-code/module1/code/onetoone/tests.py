import unittest
from onetoone import is_one_to_one

class TestIsOneToOne(unittest.TestCase):
    def test_is_one_to_one(self):
        self.assertTrue(is_one_to_one({'a': 1, 'b': 2, 'c': 3}))
        self.assertFalse(is_one_to_one({'a': 1, 'b': 2, 'c': 1}))
        self.assertTrue(is_one_to_one({}))

if __name__ == "__main__":
    unittest.main()
