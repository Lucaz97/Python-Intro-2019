from Modules.Board import Board
from Modules.Player import Player

gameBoard = Board()
players = []
print("Insert player 1 nickname: ")
players.append(Player(input(), 'X'))
print("Insert player 2 nickname: ")
players.append(Player(input(), 'O'))

playing = True
turn = 0
while playing:
    gameBoard.draw()
    print(players[turn%2].getNickname())
    # * -> estrattore di tupla, *(a,b,c) => a, b, c
    gameBoard.makeMove(*players[turn%2].pickMove(gameBoard.getFreeCells()))
    ### equals to
    ### freeCells = gameBoard.getFreeCells()
    ### move, letter = players[turn%2].pickMove(freeCells)
    ### gameBoard.makeMove(move, letter)
    if(gameBoard.isWinner(players[turn%2].getLetter())):
        print(players[turn%2].getNickname(), "wins")
        break
    elif gameBoard.isBoardFull():
        print("It's a draw.")
        break
    turn += 1
