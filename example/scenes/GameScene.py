from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.util.Loopable import Loopable

from crystal_engine.client.prefabs.Player import Player

class GameScene(Scene):
    def __init__(self) -> None:
        super().__init__()

        game_loop = Loopable()

        game_loop.loop = self.loop_game

        self.add_to_loop(game_loop)

    def loop_game(self, screen, events, keys, game, *args):
        for connection in game.NetworkManager.connections:
            if connection is not None:
                p = Player.from_object(connection.player)
                p.draw(game.screen)
