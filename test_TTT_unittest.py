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

    def test_input(self):
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "X")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "x")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "O")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "o")


if __name__ == '__main__':
    unittest.main()
