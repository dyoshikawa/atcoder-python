import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(11, main.main(5, 3, [2, 5, -4, 10, 3]))


if __name__ == "__main__":
    unittest.main()
