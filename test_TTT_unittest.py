import Tic_tac_toe
import unittest


class TestTicTacToe(unittest.TestCase):

    def test_random(self):
        counter = 0
        for i in range(100):
            if (Tic_tac_toe.firstMove("player0", "player1") == "player1"):
                counter += 1
        print("Player 1 chosen", counter, "percent of the time.")

    def test_winner(self):
        self.assertTrue(checkWinner(['X', 'X', 'X'," "," "," "," "," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner([" ", " ", " ","X","X","X"," "," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner([' ', ' ', ' '," "," "," ","X","X","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner(['X', ' ', ' ',"X"," "," ","X"," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner([' ', 'X', ' '," ","X"," "," ","X"," "], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner([' ', ' ', 'X'," "," ","X"," "," ","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner(['X', ' ', ' '," ","X"," "," "," ","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(checkWinner([' ', ' ', 'X'," ","X"," ","X"," "," "], ['X','O'], "player0", "player1"))

    def test_input(self):
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "X")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "x")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "O")
        self.assertEqual(Tic_tac_toe.playerPickSymbol(first), "o")


if __name__ == '__main__':
    unittest.main()
