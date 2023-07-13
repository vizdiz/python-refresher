import unittest
from physics import *


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertAlmostEqual(calculate_buoyancy(1, 10), 98.1)
        self.assertAlmostEqual(calculate_buoyancy(5, 20), 981)
        self.assertAlmostEqual(calculate_buoyancy(2, 5), 98.1)

    def test_will_it_float(self):
        self.assertEqual(will_it_float(0.42, 48.2), True)
        self.assertEqual(will_it_float(0.99, 998.9), False)
        self.assertEqual(will_it_float(0.3, 299.9), True)

    def test_calculate_pressure(self):
        self.assertAlmostEqual(calculate_pressure(-1), 9810)
        self.assertAlmostEqual(calculate_pressure(2), 19620)
        self.assertAlmostEqual(calculate_pressure(-3), 29430)


if __name__ == "__main__":
    unittest.main()
