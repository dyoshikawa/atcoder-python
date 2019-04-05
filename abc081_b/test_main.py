import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(2, main.main(["3", "8 12 40"]))

    def test_2(self):
        self.assertEqual(0, main.main(["4", "5 6 8 10"]))


if __name__ == "__main__":
    unittest.main()
