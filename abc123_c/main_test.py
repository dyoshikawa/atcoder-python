import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(7, main.main(5, 3, 2, 4, 3, 5))

    def test_2(self):
        self.assertEqual(5, main.main(10, 123, 123, 123, 123, 123))


if __name__ == "__main__":
    unittest.main()
