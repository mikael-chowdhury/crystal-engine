class Manager:
    def __init__(self, game) -> None:
        self.id = len(game.managers)
        self.game = game

        self.game.managers.append(self)
        
        pass

    def update_manager(self):
        self.game.managers[self.id] = self

    def loop(self):
        pass