from client.util.Loopable import Loopable

class Scene(Loopable):
    def __init__(self) -> None:
        super().__init__()

        self.entities = []
        self.ui = []

    def loop(self, screen, *args):
        super().loop(self, screen, *args)

        for loopable in self.entities + self.ui:
            loopable.loop(screen, *args)