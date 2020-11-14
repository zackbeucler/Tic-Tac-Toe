import Tic_tac_toe
import unittest


class TestTicTacToe(unittest.TestCase):

    def test_random(self):
        for i in range(100):
            counter = 0
            if (Tic_tac_toe.firstMove("player0", "player1") == "player1"):
                counter += 1

        self.assertEqual(counter, 50)

    def test_winner(self):
        print()

    def test_input(self):
        print()


if __name__ == '__main__':
    unittest.main()
