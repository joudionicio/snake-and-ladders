import random

# Define the snakes and ladders on the board
#snakes and ladders are dictionaries where the number before the : is a key.
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

#the fuction def move just check if the player is in the snake or the ladders
def move(player, value):
    player += value
    if player in snakes:
        print("Oh no! You've landed on a snake. You're going down to", snakes[player])
        player = snakes[player]
    elif player in ladders:
        print("Yay! You've landed on a ladder. You're climbing up to", ladders[player])
        player = ladders[player]
    return player

#Aqui no mas hace que los jugadores avancen y cada vez se convoca la funcion def move para 
#ver si el jugador esta en serpiente y escaleras, el jugador se mueve a base de lo que sale en el dado 
def play_game():
    player1 = player2 = 0
    while True:
        player1 = move(player1, random.randint(1, 6))
        print("Player 1 is now on square", player1)
        if player1 >= 100:
            print("Player 1 wins!")
            break
        player2 = move(player2, random.randint(1, 6))
        print("Player 2 is now on square", player2)
        if player2 >= 100:
            print("Player 2 wins!")
            break

play_game()

