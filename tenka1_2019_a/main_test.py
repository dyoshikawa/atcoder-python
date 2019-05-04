import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual('Yes', main.main(3, 8, 5))

    def test_2(self):
        self.assertEqual('No', main.main(7, 3, 1))


if __name__ == "__main__":
    unittest.main()
