from player import Player


class Board:
    # Constructor
    def __init__(self: Board):
        self.snake = {
            99: 13,
            78: 21,
            81: 6,
            45: 34,
        }
        self.ladder = {
            5: 22,
            14: 45,
            60: 76,
            77: 91,
            44: 66,
        }

    def check_position(self, player: Player) -> None:
        """Check if the player's current position is a snake or ladder and update accordingly."""
        if player.position in self.snake:
            print(f"Oops! {player.name} landed on a snake!")
            player.position = self.snake[player.position]
            print(f"{player.name} slides down to position {player.position}")

        elif player.position in self.ladder:
            print(f"Yay! {player.name} landed on a ladder!")
            player.position = self.ladder[player.position]
            print(f"{player.name} climbs up to position {player.position}")

        else:
            print(f"{player.name} is on square {player.position}")
