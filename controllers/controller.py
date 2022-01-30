from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<input_1>/<input_2>')
def game_render(input_1, input_2):
    player_1 = Player('player one', input_1)
    player_2 = Player('player two', input_2)
    game = Game(player_1, player_2)
    result = game.game_result(game)
    return render_template('game_result.html', input_1=input_1, player_1=player_1.name, input_2=input_2, player_2=player_2.name, result=result)

@app.route('/play')
def play():
    return render_template('play_computer.html')

@app.route('/play', methods=['POST'])
def play_computer():
    player_1 = Player(request.form['player_name'], request.form['choice'])
    player_2 = Game.computer_player()
    game = Game(player_1, player_2)
    result = game.game_result(game)
    return render_template('game_result.html', input_1=player_1.choice, player_1=player_1.name, input_2=player_2.choice, player_2=player_2.name, result=result)