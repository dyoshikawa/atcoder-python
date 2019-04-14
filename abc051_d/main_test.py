import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1, main.main(3, [(1, 2, 1), (1, 3, 1), (2, 3, 3)]))

    def test_2(self):
        self.assertEqual(0, main.main(3, [(1, 2, 1), (2, 3, 1)]))


if __name__ == "__main__":
    unittest.main()
