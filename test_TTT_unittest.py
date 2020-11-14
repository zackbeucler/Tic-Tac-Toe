import Tic_tac_toe
import unittest
<<<<<<< HEAD
from unittest.mock import patch
=======
import unittest.mock

>>>>>>> cfa7395b52c7c8dfb5f144e0c21167c6bbd6e232

class TestTicTacToe(unittest.TestCase):

    def test_random(self):
        """This test case ensures that the program actually selects the player who goes 
        first at random"""

        counter = 0
        for i in range(100):
            if (Tic_tac_toe.firstMove("player0", "player1") == "player1"):
                counter += 1
        print("Player 1 chosen", counter, "percent of the time.")

    def test_winner(self):
<<<<<<< HEAD
        """This test case ensures that the program correctly identifies when there is a winner"""

        self.assertTrue(Tic_tac_toe.checkWinner(['X', 'X', 'X'," "," "," "," "," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner([" ", " ", " ","X","X","X"," "," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner([' ', ' ', ' '," "," "," ","X","X","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(['X', ' ', ' ',"X"," "," ","X"," "," "], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner([' ', 'X', ' '," ","X"," "," ","X"," "], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner([' ', ' ', 'X'," "," ","X"," "," ","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(['X', ' ', ' '," ","X"," "," "," ","X"], ['X','O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner([' ', ' ', 'X'," ","X"," ","X"," "," "], ['X','O'], "player0", "player1"))
=======
        self.assertTrue(Tic_tac_toe.checkWinner(
            ['X', 'X', 'X', " ", " ", " ", " ", " ", " "], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            [" ", " ", " ", "X", "X", "X", " ", " ", " "], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            [' ', ' ', ' ', " ", " ", " ", "X", "X", "X"], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            ['X', ' ', ' ', "X", " ", " ", "X", " ", " "], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            [' ', 'X', ' ', " ", "X", " ", " ", "X", " "], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            [' ', ' ', 'X', " ", " ", "X", " ", " ", "X"], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            ['X', ' ', ' ', " ", "X", " ", " ", " ", "X"], ['X', 'O'], "player0", "player1"))
        self.assertTrue(Tic_tac_toe.checkWinner(
            [' ', ' ', 'X', " ", "X", " ", "X", " ", " "], ['X', 'O'], "player0", "player1"))
>>>>>>> cfa7395b52c7c8dfb5f144e0c21167c6bbd6e232


    @patch('Tic_tac_toe.playerPickSymbol', return_value="X")
    def test_upperx(self, input):
        """This test case ensures that the program correctly assigns a player the symbol 'X'
        if the player chooses"""

        self.assertEqual(Tic_tac_toe.answer(), "X")

    @patch('Tic_tac_toe.playerPickSymbol', return_value="o")
    def test_lowero(self, input):
        """This test case ensures that the program correctly assigns a player the symbol 'o'
        if the player chooses"""

        self.assertEqual(Tic_tac_toe.answer(), "o")

    @patch('Tic_tac_toe.playerPickSymbol', return_value="O")
    def test_uppero(self, input):
        """This test case ensures that the program correctly assigns a player the symbol 'O'
        if the player chooses"""

        self.assertEqual(Tic_tac_toe.answer(), "O")

    @patch('Tic_tac_toe.playerPickSymbol', return_value="x")
    def test_lowerx(self, input):
        """This test case ensures that the program correctly assigns a player the symbol 'x'
        if the player chooses"""
        
        self.assertEqual(Tic_tac_toe.answer(), "x")


if __name__ == '__main__':
    unittest.main()
