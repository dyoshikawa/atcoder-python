import unittest
import main


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(2, main.main("101"))

    def test_2(self):
        self.assertEqual(0, main.main("000"))


if __name__ == "__main__":
    unittest.main()
