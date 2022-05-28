import client

game = client.Game((800, 800))

while game.running:
    events, pressed_keys = game.loop()