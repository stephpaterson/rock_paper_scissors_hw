import random
from models.player import Player

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    
    def computer_choice():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
        
    def computer_player():
        choice = Game.computer_choice()
        computer = Player("Computer", choice )
        return computer


    def game_result(self, game):
        result = None
        if self.player_1.choice == "scissors":
            result = self.player_1_scissors_result()
        elif self.player_1.choice == "rock":
            result = self.player_1_rock_result()
        elif self.player_1.choice == "paper":
            result = self.player_1_paper_result()
        return result


    def player_1_scissors_result(self):
            if self.player_2.choice == "rock":
                return f"{self.player_2.name}!"
            elif self.player_2.choice == "paper":
                    return f"{self.player_1.name}!"
            else:
                return None

    def player_1_rock_result(self):
            if self.player_2.choice == "scissors":
                return f"{self.player_1.name}!"
            elif self.player_2.choice == "paper":
                return f"{self.player_2.name}!"
            else:
                return None

    def player_1_paper_result(self):
            if self.player_2.choice == "scissors":
                return f"{self.player_2.name}!"
            elif self.player_2.choice == "rock":
                return f"{self.player_1.name}!"
            else:
                return None

    