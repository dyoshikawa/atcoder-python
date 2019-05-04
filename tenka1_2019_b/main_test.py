import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual('*rr*r', main.main("error", 2))

    def test_2(self):
        self.assertEqual('e*e*e*', main.main("eleven", 5))


if __name__ == "__main__":
    unittest.main()
