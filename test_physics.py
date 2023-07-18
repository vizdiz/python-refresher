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
                [0.05 * np.cos(np.pi / 10), 0.05 * np.sin(np.pi / 10)],
            )
        )
        self.assertTrue(
            np.allclose(
                calculate_auv_acceleration(10, np.pi / 8),
                [0.10 * np.cos(np.pi / 8), 0.10 * np.sin(np.pi / 8)],
            )
        )
        self.assertTrue(
            np.allclose(
                calculate_auv_acceleration(20, np.pi / 6),
                [0.20 * np.cos(np.pi / 6), 0.20 * np.sin(np.pi / 6)],
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
                [math.sqrt(2) - 2.0 * math.sqrt(6), -2.0 * math.sqrt(2) - math.sqrt(6)],
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

    def test_simulate_auv2_motion(self):
        T = np.array([1.0, 9.0, 2.0, 1.0])
        alpha = np.pi / 6
        L = 1.0
        l = 0.5
        inertia = 100
        mass = 100
        dt = 0.1

        t = np.arange(0, 0.4, 0.1)
        x = [0.0, 0.0006062177826491072, 0.0018183593196756554, 0.003635835779289311]
        y = [0.0, -0.00045, -0.001350395830221758, -0.002701978574589373]
        a = [
            [0.06062178, -0.045],
            [0.06062178, -0.045],
            [0.06062178, -0.045],
            [0.06059238, -0.04503958],
        ]
        v = [
            [0.0, 0.0],
            [0.00606218, -0.0045],
            [0.01212142, -0.00900396],
            [0.01817476, -0.01351583],
        ]
        omega = [
            0.0,
            -0.006531088913245536,
            -0.013062177826491071,
            -0.019593266739736607,
        ]
        theta = [
            0.0,
            -0.0006531088913245536,
            -0.0019593266739736607,
            -0.003918653347947321,
        ]

        t_e, x_e, y_e, theta_e, v_e, omega_e, a_e = simulate_auv2_motion(
            T, alpha, L, l, mass, inertia, dt, 4 * dt, 0, 0, 0
        )

        print(a)
        print(a_e)

        self.assertTrue(np.allclose(t, t_e, atol=1e-5))
        self.assertTrue(np.allclose(x, x_e, atol=1e-5))
        self.assertTrue(np.allclose(y, y_e, atol=1e-5))
        self.assertTrue(np.allclose(a, a_e, atol=1e-3))
        self.assertTrue(np.allclose(v, v_e, atol=1e-3))
        self.assertTrue(np.allclose(omega, omega_e, atol=1e-5))
        self.assertTrue(np.allclose(theta, theta_e, atol=1e-5))

        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40, 60, 80]),
            np.pi / 3,
            3.0,
            2.0,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100]),
            np.pi / 3,
            -3.0,
            2.0,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100.0]),
            np.pi / 3,
            3.0,
            -2.0,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100.0]),
            np.pi / 3,
            3.0,
            2.0,
            -1.0,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100.0]),
            np.pi / 3,
            3.0,
            2.0,
            1.0,
            -1.0,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100.0]),
            np.pi / 3,
            3.0,
            2.0,
            1.0,
            1.0,
            -0.3,
        )
        self.assertRaises(
            ValueError,
            simulate_auv2_motion,
            np.array([40.0, 60.0, 80.0, 100.0]),
            np.pi / 3,
            3.0,
            2.0,
            1.0,
            1.0,
            0.3,
            -10.0,
        )


if __name__ == "__main__":
    unittest.main()
