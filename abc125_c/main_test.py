import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(2, main.main(3, [7, 6, 8]))

    def test_2(self):
        self.assertEqual(6, main.main(3, [12, 15, 18]))


if __name__ == "__main__":
    unittest.main()
