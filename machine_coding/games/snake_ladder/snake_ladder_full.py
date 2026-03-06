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


class Game:
    # Constructor
    def __init__(self: Game):
        self.players: list[Player] = []
        self.board = Board()

    def start_game(self: Game, num_players: int) -> None:
        self._initialize_players(num_players)

        # Game loop
        game_over: bool = False
        while not game_over:
            for player in self.players:
                game_over = self._play_turn(player)
                if game_over:
                    break

            print("\nCurrent positions of all players:")
            for p in self.players:
                print(f"{p.name}: {p.position}")

    def check_winner(self: Game, player: Player) -> bool:
        # Check if player reached position 100
        return player.position == 100

    def _initialize_players(self: Game, num_players: int) -> None:
        # Initialize players
        for _ in range(num_players):
            name = input("Enter your name: ")
            self.players.append(Player(name))

    def _play_turn(self: Game, player: Player) -> bool:
        print(f"\n{player.name}'s turn:")
        steps = player.roll_dice()
        print(f"{player.name} rolled a {steps}")

        if steps + player.position > 100:
            print(f"{player.name} can't move, roll too high. Try again next turn!")
            input("Press Enter to continue to the next turn...")
            return False

        player.move(steps)

        self.board.check_position(player)

        # Check if player won
        if self.check_winner(player):
            print(f"\nCongratulations {player.name}, you won the game!")
            return True

        input("Press Enter to continue to the next turn...")
        return False


game = Game()
try:
    num_players = int(input("Enter the number of players: "))
    if num_players <= 0:
        print("Number of players must be at least 1!")
    else:
        game.start_game(num_players)
except ValueError:
    print("Invalid input! Please enter a valid number of players.")
