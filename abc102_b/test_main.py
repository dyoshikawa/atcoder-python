import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(5, main.main("1 4 6 3"))

    def test_2(self):
        self.assertEqual(999999999, main.main("1000000000 1"))

    def test3(self):
        self.assertEqual(0, main.main("1 1 1 1 1"))


if __name__ == "__main__":
    unittest.main()
