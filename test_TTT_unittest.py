import unittest

class TestTicTacToe(unittest.TestCase):

    def test_random(self):

    def test_winner(self):

    def test_input(self):
        self.assertEqual(playerPickSymbol(first), "X")
        self.assertEqual(playerPickSymbol(first), "x")
        self.assertEqual(playerPickSymbol(first), "O")
        self.assertEqual(playerPickSymbol(first), "o")

if __name__ == '__main__':
    unittest.main()
