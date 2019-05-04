import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1, main.main("#.#"))

    def test_2(self):
        self.assertEqual(2, main.main("#.##."))

    def test_3(self):
        self.assertEqual(0, main.main("........."))

    def test_4(self):
        self.assertEqual(2, main.main("#.#..###"))

    def test_5(self):
        self.assertEqual(2, main.main("##...."))

    def test_6(self):
        self.assertEqual(2, main.main("##....#"))

    def test_7(self):
        self.assertEqual(2, main.main("##....#####"))

    def test_8(self):
        self.assertEqual(0, main.main("."))

    def test_9(self):
        self.assertEqual(1, main.main("#######."))

    def test_10(self):
        self.assertEqual(0, main.main("#"))

    def test_11(self):
        self.assertEqual(1, main.main("##############.###########"))

    def test_12(self):
        self.assertEqual(6, main.main("######......"))


if __name__ == "__main__":
    unittest.main()
