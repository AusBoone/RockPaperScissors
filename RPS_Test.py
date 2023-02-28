import unittest
from io import StringIO
from unittest.mock import patch
from RockPaperScissors import Game

"""
This test file uses the unittest module to create a TestGame class with three test methods: 
test_initial_scores, test_tie, test_win, and test_loss.
"""
class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()
        
    def test_initial_scores(self):
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
        self.assertEqual(self.game.high_score, 0)
        
    @patch('builtins.input', side_effect=['rock', 'rock'])
    def test_tie(self, mock_input):
        self.game.play()
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
        
    @patch('builtins.input', side_effect=['rock', 'scissors'])
    def test_win(self, mock_input):
        self.game.play()
        self.assertEqual(self.game.user_score, 1)
        self.assertEqual(self.game.computer_score, 0)
        
    @patch('builtins.input', side_effect=['rock', 'paper'])
    def test_loss(self, mock_input):
        self.game.play()
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 1)
        
if __name__ == '__main__':
    unittest.main()
