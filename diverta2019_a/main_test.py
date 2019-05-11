import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(2, main.main(3, 2))

    def test_2(self):
        self.assertEqual(11, main.main(13, 3))


if __name__ == "__main__":
    unittest.main()
