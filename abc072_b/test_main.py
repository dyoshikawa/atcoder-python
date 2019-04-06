import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual("acdr", main.main("atcoder"))

    def test_2(self):
        self.assertEqual("aa", main.main("aaaa"))

    def test_3(self):
        self.assertEqual("z", main.main("z"))

    def test_4(self):
        self.assertEqual("fkoaaauh", main.main("fukuokayamaguchi"))


if __name__ == "__main__":
    unittest.main()
