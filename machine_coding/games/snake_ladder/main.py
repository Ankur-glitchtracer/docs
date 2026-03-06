from game import Game


game = Game()
try:
    num_players = int(input("Enter the number of players: "))
    if num_players <= 0:
        print("Number of players must be at least 1!")
    else:
        game.start_game(num_players)
except ValueError:
    print("Invalid input! Please enter a valid number of players.")
