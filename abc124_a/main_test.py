import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(9, main.main(5, 3))

    def test_2(self):
        self.assertEqual(7, main.main(3, 4))


if __name__ == "__main__":
    unittest.main()
