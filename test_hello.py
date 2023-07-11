import unittest
import numpy as np
import math
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(0, 1), 1)
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(hello.sub(1, 0), 1)
        self.assertEqual(hello.sub(3, 1), 2)
        self.assertEqual(hello.sub(5, -2), 7)
    
    def test_mul(self):
        self.assertEqual(hello.mul(1, 0), 0)
        self.assertEqual(hello.mul(1, 1), 1)
        self.assertEqual(hello.mul(4, 2), 8)

    def test_div(self):
        self.assertEqual(hello.div(0, 1), 0)
        self.assertEqual(hello.div(1, 1), 1)
        self.assertEqual(hello.div(4, 2), 2)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(1), 1)
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)
    
    def test_log(self):
        self.assertEqual(hello.log(np.e), 1)
        self.assertEqual(hello.log(np.e ** 2), 2)
        self.assertEqual(hello.log(np.e ** 3), 3)
    
    def test_exp(self):
        self.assertEqual(hello.exp(1), np.e)
        self.assertEqual(hello.exp(2), 7.38905609893065)
        self.assertEqual(hello.exp(3), 20.085536923187668)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(math.pi / 2), 1)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(math.pi), -1)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(math.pi / 4), 0.9999999999999999)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot(math.pi / 4), 1.0000000000000002)


if __name__ == "__main__":
    unittest.main()
