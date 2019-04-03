# coding:utf-8

import unittest
import main


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual("Even", main.main("3 4"))

    def test_2(self):
        self.assertEqual("Odd", main.main("1 21"))


if __name__ == "__main__":
    unittest.main()
