from random import randint


class Player:
    # Constructor
    def __init__(self: Player, name: str, position: int = 0):
        self.name = name
        self.position = position

    def roll_dice(self) -> int:
        return randint(1, 6)

    def move(self, steps: int) -> None:
        self.position += steps
