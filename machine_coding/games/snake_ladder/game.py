from player import Player
from board import Board


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
