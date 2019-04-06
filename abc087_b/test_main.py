import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(2, main.main([2, 2, 2, 100]))

    def test_2(self):
        self.assertEqual(0, main.main([5, 1, 0, 150]))

    def test3(self):
        self.assertEqual(213, main.main([30, 40, 50, 6000]))


if __name__ == "__main__":
    unittest.main()
