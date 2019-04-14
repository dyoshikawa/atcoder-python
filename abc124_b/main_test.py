import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(3, main.main([6, 5, 6, 8]))

    def test_2(self):
        self.assertEqual(3, main.main([4, 5, 3, 5, 4]))


if __name__ == "__main__":
    unittest.main()
