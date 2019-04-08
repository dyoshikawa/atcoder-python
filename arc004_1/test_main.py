import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(3.605551, main.main(["1 1", "2 4", "4 3"]))


if __name__ == "__main__":
    unittest.main()
