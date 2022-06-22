import crystal_engine.client as client
from crystal_engine.client.prefabs.Player import Player
from crystal_engine.client.ui.impl.Clickable import Clickable
from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.util.Loopable import Loopable 

game = client.Game((800, 800))


game_scene = Scene()

game_loop = Loopable()

def loop_game(*args):
    for connection in game.NetworkManager.connections:
        if connection is not None:
            p = Player.from_object(connection.player)
            p.draw(game.screen)

game_loop.loop = loop_game

game_scene.add_to_loop(game_loop)

def click_chad():
    game.NetworkManager.connect_to_server("192.168.178.22", 5555)

    game.SceneManager.set_scene(game_scene)

scene1 = Scene()
scene1.background = (255, 255, 255)
scene1.ui.append(Clickable(100, 100, 150, 25, background_color=(255, 0, 0), text_color=(0, 0, 0), on_click=lambda: click_chad(), text="get out of scene"))

game.SceneManager.set_scene(scene1)

player = Player(100, 100)
player.create(game, game_scene)

while game.running:
    events, keys = game.loop()

    game.end_loop()