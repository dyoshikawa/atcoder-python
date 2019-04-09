import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(84, main.main(20, 2, 5))

    def test_2(self):
        self.assertEqual(13, main.main(10, 1, 2))

    def test_3(self):
        self.assertEqual(4554, main.main(100, 4, 16))


if __name__ == "__main__":
    unittest.main()
