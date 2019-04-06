import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual("Yes", main.main(11))

    def test_2(self):
        self.assertEqual("Yes", main.main(40))

    def test3(self):
        self.assertEqual("No", main.main(3))


if __name__ == "__main__":
    unittest.main()
