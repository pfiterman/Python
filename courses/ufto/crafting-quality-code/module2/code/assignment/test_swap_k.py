import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_list_empty_k_zero(self):
        """
        Test swap_k with empty list and k=0 (boundry)
        """
        actual_list = []
        expected_list = []
        a1.swap_k(actual_list, 0)
        self.assertEqual(actual_list, expected_list)

    def test_swap_k_list_full_k_zero(self):
        """
        Test swap_k with a list of numbers and k = 0
        """
        actual_list = [1, 2, 3, 4, 5, 6]
        expected_list = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual_list, 0)
        self.assertEqual(actual_list, expected_list)

    def test_swap_k_smallest_list(self):
        """
        Test swap_k with a list of two number and k = 1
        """
        actual_list = [1, 2]
        expected_list = [2, 1]
        a1.swap_k(actual_list, 1)
        self.assertEqual(actual_list, expected_list)  

    def test_swap_k_inbetween_odd(self):
        """
        Test swap_k with a list of odd numbers and k = 1
        """
        actual_list = [1, 2, 3]
        expected_list = [3, 2, 1]
        a1.swap_k(actual_list, 1)
        self.assertEqual(actual_list, expected_list) 

    def test_swap_k_inbetween_even(self):
        """
        Test swap_k with a list of even number and k = 2
        """
        actual_list = [1, 2, 3, 4, 5, 6]
        expected_list = [5, 6, 3, 4, 1, 2]
        a1.swap_k(actual_list, 2)
        self.assertEqual(actual_list, expected_list)

    def test_swap_k_list_full_k_max(self):
        """
        Test swap_k with a list of numbers and k = len(L)// 2
        """
        actual_list = [1, 2, 3, 4, 5, 6]
        expected_list = [4, 5, 6, 1, 2, 3]
        a1.swap_k(actual_list, 3)
        self.assertEqual(actual_list, expected_list)    

if __name__ == '__main__':
    unittest.main(exit=False)