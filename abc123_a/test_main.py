import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual("Yay!", main.main([1, 2, 4, 8, 9, 15]))

    def test_2(self):
        self.assertEqual(":(", main.main([15, 18, 26, 35, 36, 18]))


if __name__ == "__main__":
    unittest.main()
