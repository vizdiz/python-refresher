import unittest
import math
import numpy as np
from physics import *


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertAlmostEqual(calculate_buoyancy(1, 10), 98.1)
        self.assertAlmostEqual(calculate_buoyancy(5, 20), 981)
        self.assertRaises(ValueError, calculate_buoyancy, -2, 5)

    def test_will_it_float(self):
        self.assertEqual(will_it_float(0.42, 48.2), True)
        self.assertEqual(will_it_float(0.99, 998.9), False)
        self.assertRaises(ValueError, will_it_float, -0.19, 991.0)

    def test_calculate_pressure(self):
        self.assertAlmostEqual(calculate_pressure(-1), 111135)
        self.assertAlmostEqual(calculate_pressure(2), 120945)
        self.assertAlmostEqual(calculate_pressure(-3), 130755)

    def test_calculate_acceleration(self):
        self.assertAlmostEqual(calculate_acceleration(102.0, 51.0), 2.0)
        self.assertAlmostEqual(calculate_acceleration(57.0, 19.0), 3.0)
        self.assertRaises(ValueError, calculate_acceleration, 68.0, -9.0)

    def test_calculate_acceleration(self):
        self.assertAlmostEqual(calculate_angular_acceleration(102.0, 51.0), 2.0)
        self.assertAlmostEqual(calculate_angular_acceleration(57.0, 19.0), 3.0)
        self.assertRaises(ValueError, calculate_angular_acceleration, 68.0, -9.0)

    def test_calculate_torque(self):
        self.assertAlmostEqual(calculate_torque(20.0, 45.0, math.sqrt(2)), 20.0)
        self.assertAlmostEqual(calculate_torque(10.0, 30.0, 5.0), 25.0)
        self.assertRaises(ValueError, calculate_torque, 5.0, 60.0, -math.sqrt(3))

    def test_calculate_moment_of_inertia(self):
        self.assertAlmostEqual(calculate_moment_of_inertia(2.0, 6.0), 72.0)
        self.assertRaises(ValueError, calculate_moment_of_inertia, 68.0, -9.0)
        self.assertRaises(ValueError, calculate_moment_of_inertia, -68.0, 9.0)

    def test_calculate_auv_acceleration(self):
        self.assertTrue(
            np.allclose(
                calculate_auv_acceleration(5, np.pi / 10),
                np.array([0.05 * np.cos(np.pi / 10), 0.05 * np.sin(np.pi / 10)]),
            )
        )
        self.assertTrue(
            np.allclose(
                calculate_auv_acceleration(10, np.pi / 8),
                np.array([0.10 * np.cos(np.pi / 8), 0.10 * np.sin(np.pi / 8)]),
            )
        )
        self.assertTrue(
            np.allclose(
                calculate_auv_acceleration(20, np.pi / 6),
                np.array([0.20 * np.cos(np.pi / 6), 0.20 * np.sin(np.pi / 6)]),
            )
        )
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, 31.0)
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, -30.0, -1.0)
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, 31.0, 1.0, -8.0)
        self.assertRaises(
            ValueError, calculate_auv_acceleration, 1.0, 31.0, 1.0, 8.0, -1.5
        )

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(
            calculate_auv_angular_acceleration(5.0, np.pi / 10),
            2.5 * np.sin(np.pi / 10),
        )
        self.assertAlmostEqual(
            calculate_auv_angular_acceleration(10.0, np.pi / 9), 5.0 * np.sin(np.pi / 9)
        )
        self.assertAlmostEqual(
            calculate_auv_angular_acceleration(20.0, np.pi / 6),
            10.0 * np.sin(np.pi / 6),
        )
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, 31.0)
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, -30.0, -1.0)
        self.assertRaises(ValueError, calculate_auv_acceleration, 1.0, 31.0, 1.0, -8.0)

    def test_calculate_auv2_acceleration(self):
        T = np.array([2.0, 4.0, 8.0, 6.0])
        T_error = np.array([1.0])
        self.assertTrue(
            np.allclose(
                calculate_auv2_acceleration(T, np.pi / 4, np.pi / 6, 1.0),
                np.array(
                    [
                        math.sqrt(2) - 2.0 * math.sqrt(6),
                        -2.0 * math.sqrt(2) - math.sqrt(6),
                    ]
                ),
            )
        )
        self.assertRaises(
            ValueError, calculate_auv2_acceleration, T, np.pi / 4, np.pi / 6, 0.0
        )
        self.assertRaises(
            ValueError, calculate_auv2_acceleration, T_error, np.pi / 4, np.pi / 6
        )

    def test_calculate_auv2_angular_acceleration(self):
        T = np.array([2.0, 4.0, 10.0, 6.0])
        T_error = np.array([1.0])
        self.assertAlmostEqual(
            calculate_auv2_angular_acceleration(T, np.pi / 4, 2.0, 3.0, 1.0),
            5.0 * math.sqrt(2),
        )
        self.assertRaises(
            ValueError, calculate_auv2_angular_acceleration, T, np.pi / 4, -1.0, 3.0
        )
        self.assertRaises(
            ValueError, calculate_auv2_angular_acceleration, T, np.pi / 4, 1.0, -3.0
        )
        self.assertRaises(
            ValueError,
            calculate_auv2_angular_acceleration,
            T,
            np.pi / 4,
            1.0,
            3.0,
            -98.0,
        )
        self.assertRaises(
            ValueError,
            calculate_auv2_angular_acceleration,
            T_error,
            np.pi / 4,
            1.0,
            2.0,
        )


if __name__ == "__main__":
    unittest.main()
