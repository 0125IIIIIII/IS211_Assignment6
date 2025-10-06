import unittest
from conversions_stub import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestStubConversions(unittest.TestCase):
    def test_kelvin(self):
        print("Testing stub convertCelsiusToKelvin")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.0), 573.15, places=2)

    def test_fahrenheit(self):
        print("Testing stub convertCelsiusToFahrenheit")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.0), 572.0, places=2)

if __name__ == '__main__':
    unittest.main()



