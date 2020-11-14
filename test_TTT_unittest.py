import Tic_tac_toe.py
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
        @patch('Tic-tac-toe.get_input', return_value="x")
        def test_lowerx(self, input):
            self.assertEqual(answer(), "x")

        @patch('Tic-tac-toe.get_input', return_value="X")
        def test_upperx(self, input):
            self.assertEqual(answer(), "X")

        @patch('Tic-tac-toe.get_input', return_value="o")
        def test_lowero(self, input):
            self.assertEqual(answer(), "o")

        @patch('Tic-tac-toe.get_input', return_value="O")
        def test_uppero(self, input):
            self.assertEqual(answer(), "O")

if __name__ == '__main__':
    unittest.main()
