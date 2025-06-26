import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_one_passenger(self):
        """ Test minimum number of buses when there is no passengers """       
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual,expected)

    def test_num_buses_one_passenger(self):
        """ Test minimum number of buses when there is just one passenger """       
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual,expected)
    
    def test_num_buses_greater_than_one_and_less_than_max_capacity(self):
        """ Test minimum number of buses when number of passengers is greater than 1 and less than max capacity """       
        actual = a1.num_buses(30)
        expected = 1
        self.assertEqual(actual,expected)
        
    def test_num_buses_when_max_capacity(self):
        """ Test minimum number of buses when there are exactly the max capacity (50 passengers) """       
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual,expected)

    def test_num_buses_when_one_passeger_up_to_max_capacity(self):
        """ Test minimum number of buses when there is just one passenger up to max capacity (51 pasengers) """       
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual,expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)