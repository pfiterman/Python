import unittest
from celsiusconverter import convert_to_celsius, weather_info

class TestConvertToCelsius(unittest.TestCase):
    def test_positive_fahrenheit(self):
        """
        Test positive fahrenheit to celsius        
        """
        self.assertAlmostEqual(convert_to_celsius(32),0)
        self.assertAlmostEqual(convert_to_celsius(212),100)
        self.assertAlmostEqual(convert_to_celsius(98.6), 37, places=1)

    def test_negative_fahrenheit(self):
        """
        Test positive fahrenheit to celsius
        """
        self.assertAlmostEqual(convert_to_celsius(-40), -40)
        self.assertAlmostEqual(convert_to_celsius(-22), -30, places=0)

    def test_zero(self):
        """
        Test zero fahrenheit
        """
        self.assertAlmostEqual(convert_to_celsius(0), -17.77778, places=5)

    def test_type_error(self):
        """
        Test invalid type input
        """
        with self.assertRaises(TypeError):
            convert_to_celsius("not a number")

class TestWeatherInfo(unittest.TestCase):
    def test_basics(self):
        """
        Test basic weather info results
        """
        self.assertEqual(weather_info(50), "10.0 is above freezing temperature")
        self.assertEqual(weather_info(23), "-5.0 is freezing temperature")

if __name__ == "__main__":
    unittest.main()