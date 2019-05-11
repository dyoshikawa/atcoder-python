import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual([2, 0, 3], main.main(
            8, 3, "ACACTACG", [(3, 7), (2, 3), (1, 8)]))


if __name__ == "__main__":
    unittest.main()
