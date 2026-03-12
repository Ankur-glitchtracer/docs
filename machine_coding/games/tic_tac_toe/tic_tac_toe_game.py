from itertools import cycle


class Player:
    def __init__(self, value: str) -> None:
        self.value: str = value


class Board:
    def __init__(self, size: int) -> None:
        self.board: list[list[str]] = [[' ' for _ in range(size)] for _ in range(size)]
        self.size: int = size

    def print(self) -> None:
        for row in self.board:
            print('|' + '|'.join(row) + '|')

    def _can_play(self, x: int, y: int) -> bool:
        if(x < 1 or x > self.size or y < 1 or y > self.size):
            return False

        return self.board[x-1][y-1] == ' '

    def _patterns(self, val: str) -> bool:
        k = self.size
        # For Horizontal
        for i in range(0,k):
            flag = True
            for j in range(0,k):
                if(self.board[i][j] != val):
                    flag = False
                    break
            if(flag):
                return flag
        # For Vertical
        for j in range(0,k):
            flag = True
            for i in range(0,k):
                if(self.board[i][j] != val):
                    flag = False
                    break
            if(flag):
                return flag
        # For first diagonal
        flag = True
        for i in range(0,k):
            if(self.board[i][i] != val):
                flag = False
                break
        if(flag):
            return flag
        # For second diagonal
        flag = True
        for i in range(0,k):
            if(self.board[i][k-i-1] != val):
                flag = False
                break

        return flag

    def move(self, player: Player, x: int, y: int) -> bool:
        if(self._can_play(x,y)):
            self.board[x-1][y-1] = player.value
            return True

        print("The coordinates is either taken or is invalid")
        return False

    def check(self, player: Player) -> bool:
        val: str = player.value
        return self._patterns(val)

    def completed(self) -> bool:
        for row in self.board:
            for col in row:
                if(col == ' '):
                    return False

        return True


class Builder:
    def __init__(self, size: int) -> None:
        self.board: Board = Board(size)
        self.players: list[Player] = []
    
    def init_player(self, num_players: int) -> None:
        while num_players != 0:
            try:
                val = str(input("Enter the value for the player: "))
                if not self._check_player(val = val):
                    self.players.append(Player(val))
                    num_players = num_players - 1
                    continue

                print("Value is already assigned to another player")
            except ValueError:
                print("Enter Valid string")
    
    def _check_player(self, val: str) -> bool:
        return any(player.value == val for player in self.players)


class Game:
    def __init__(self) -> None:
        self.builder: Builder = self._init_builder()
        self.board = self.builder.board

    def _init_builder(self) -> Builder:
        while True:
            try:
                size = int(input("Enter the size of board NxN: "))
                if(size >= 3):
                    return self._init_player(Builder(size=size))
                print("Enter a valid size")

            except ValueError:
                print("Enter a valid size")

    def _init_player(self, builder: Builder) -> Builder:
        while True:
            try:
                num_players = int(input("Enter number of players playing: "))
                if(num_players >= 2):
                    builder.init_player(num_players=num_players)
                    return builder
                print("Minimum number for is game is 2")
            except ValueError:
                print("Enter a valid integer")


    def start_game(self):
        game_over = False
        for player in cycle(self.builder.players):
            game_over = self._session(player=player)
            if game_over:
                break

    def _session(self, player: Player) -> bool:
        print(f"Player {player.value}:")
        x, y = self._input()
        while not self.board.move(player, x, y):
            print(f"Player {player.value}:")
            x ,y = self._input()
        game = self.board.check(player)
        if(game):
            print(f"Player {player.value} won")
            self.board.print()
            return game
        game = self.board.completed()
        if game:
            print("Draw, board is completed")
        self.board.print()
        return game

    def _input(self) -> tuple:
        while True:
            try:
                x = int(input("Enter the x coordinate: "))
                y = int(input("Enter the y coordinate: "))
                return (x, y)
            except ValueError:
                print("Enter valid integer")


game = Game()
game.start_game()
