from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.ui.impl.Clickable import Clickable

class StartMenu(Scene):
    def __init__(self):
        super().__init__()

        self.background = (255, 255, 255)
        self.ui.append(Clickable(100, 100, 150, 25, background_color=(255, 0, 0), text_color=(0, 0, 0), on_click=self.start_game, text="start game"))
        
        self.game_scene = None

    def set_game_scene(self, game_scene):
        self.game_scene = game_scene

    def start_game(self, screen, events, keys, game):
        game.NetworkManager.connect_to_server("192.168.178.22", 5555)

        game.SceneManager.set_scene(self.game_scene)