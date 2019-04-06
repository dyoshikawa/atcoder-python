import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(215, main.main([29, 20, 7, 35, 120]))

    def test_2(self):
        self.assertEqual(481, main.main([101, 86, 119, 108, 57]))

    def test_3(self):
        self.assertEqual(643, main.main([123, 123, 123, 123, 123]))


if __name__ == "__main__":
    unittest.main()
