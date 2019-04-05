import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(4, main.main("7"))

    def test_2(self):
        self.assertEqual(32, main.main("32"))

    def test_3(self):
        self.assertEqual(1, main.main("1"))

    def test_4(self):
        self.assertEqual(64, main.main("100"))


if __name__ == "__main__":
    unittest.main()
