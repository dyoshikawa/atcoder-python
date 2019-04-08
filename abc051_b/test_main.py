import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(6, main.main("2 2"))

    def test_2(self):
        self.assertEqual(1, main.main("5 15"))


if __name__ == "__main__":
    unittest.main()
