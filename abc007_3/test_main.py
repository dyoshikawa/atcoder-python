import unittest
import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(11, main.main(
            [
                [
                    "7 8",
                    "2 2",
                    "4 5"
                ],
                [
                    "########",
                    "#......#",
                    "#.######",
                    "#..#...#",
                    "#..##..#",
                    "##.....#",
                    "########",
                ]
            ]))


if __name__ == "__main__":
    unittest.main()
