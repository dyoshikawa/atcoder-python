import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(4, main.main(1, 2, 3, 4))

    def test_2(self):
        self.assertEqual(87058, main.main(13, 1, 4, 3000))


if __name__ == "__main__":
    unittest.main()
