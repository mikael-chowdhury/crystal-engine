import crystal_engine.client as client
from crystal_engine.client.prefabs.Player import Player
from scenes.GameScene import GameScene

from scenes.StartMenu import StartMenu 

game = client.Game((800, 800))


start_menu = StartMenu()
game_scene = GameScene()

start_menu.set_game_scene(game_scene)

game.SceneManager.set_scene(start_menu)

player = Player(100, 100)
player.create(game, game_scene)

while game.running:
    events, keys = game.loop()

    game.end_loop()