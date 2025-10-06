import unittest
from conversions import *
from conversions_refactored import convert, ConversionNotPossible

class TestWorkingConversions(unittest.TestCase):
    def test_kelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15, places=2)

    def test_fahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.0), 572.0, places=2)

    def test_distance(self):
        self.assertAlmostEqual(convertMilesToMeters(1), 1609.34)

    def test_refactored(self):
        self.assertAlmostEqual(convert('celsius', 'kelvin', 300.0), 573.15)
        self.assertEqual(convert('meters', 'meters', 100), 100.0)
        with self.assertRaises(ConversionNotPossible):
            convert('celsius', 'meters', 100)

if __name__ == '__main__':
    unittest.main()



