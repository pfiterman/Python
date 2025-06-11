import unittest
from startswith import count_startswith

class TestCountStartsWith(unittest.TestCase):
    def test_count_startswith(self):
        self.assertEqual(count_startswith(['rumba','salsa','samba'], 's'), 2)

if __name__ == "__main__":
    unittest.main()