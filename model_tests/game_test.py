
import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Jade", "scissors")
        self.player_2 = Player("Charlie", "rock")
        self.game = Game(self.player_1, self.player_2)

    def test_player_has_name(self):
        self.assertEqual("Jade", self.player_1.name)

    def test_scissors_beats_rock(self):
        result = self.game.player_1_scissors_result()
        self.assertEqual("Player 1 wins!", result)

    def test_scissors_doesnt_beat_paper(self):
        self.player_1 = Player("Jade", "scissors")
        self.player_2 = Player("Charlie", "paper")
        self.game = Game(self.player_1, self.player_2)
        result = self.game.player_1_scissors_result()
        self.assertEqual("Player 2 wins!", result)

    def test_scissors_doesnt_beat_scissors(self):
        self.player_1 = Player("Jade", "scissors")
        self.player_2 = Player("Charlie", "scissors")
        self.game = Game(self.player_1, self.player_2)
        result = self.game.player_1_scissors_result()
        self.assertEqual(None, result)

    def test_rock_doesnt_beat_paper(self):
        self.player_1 = Player("Jade", "rock")
        self.player_2 = Player("Charlie", "paper")
        self.game = Game(self.player_1, self.player_2)

        result = self.game.player_1_rock_result()
        self.assertEqual("Player 2 wins!", result)
    
    def test_game_result_rock(self):
        self.player_1 = Player("Jade", "rock")
        self.player_2 = Player("Charlie", "paper")
        self.game = Game(self.player_1, self.player_2)
        result = self.game.game_result()
        self.assertEqual("Player 2 wins!", result )

    def test_game_result_paper(self):
        self.player_1 = Player("Jade", "paper")
        self.player_2 = Player("Charlie", "rock")
        self.game = Game(self.player_1, self.player_2)
        result = self.game.game_result()
        self.assertEqual("Player 1 wins!", result )

    def test_game_result_scissors(self):
        self.player_1 = Player("Jade", "scissors")
        self.player_2 = Player("Charlie", "rock")
        self.game = Game(self.player_1, self.player_2)
        result = self.game.game_result()
        self.assertEqual("Player 1 wins!", result )