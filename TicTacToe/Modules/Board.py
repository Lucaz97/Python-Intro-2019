
class Board:

    # inizializzatore, viene eseguito quando faccio Board()
    def __init__(self):
        self.cells = [' ']*9

    # stampo la griglia
    def draw(self):
        print('   |   |')
        print(' ' + self.cells[6] + ' | ' + self.cells[7] + ' | ' + self.cells[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.cells[3] + ' | ' + self.cells[4] + ' | ' + self.cells[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.cells[0] + ' | ' + self.cells[1] + ' | ' + self.cells[2])
        print('   |   |')

    def isCellFree(self, i):
        return self.cells[i] == ' '

    def getFreeCells(self):
        # i metodi di una classe si chiamano con oggetto.metodo()
        # siccome qui sono già dentro un metodo, lo sto applicando a un oggetto
        # voglio chiamare il metodo isCellFree sullo stesso oggetto su cui è stato
        # è stato chiamato il metodo in cui sono, uso quindi self.isCellFree
        # self è l'oggetto su sui sto operando
        return [i for i in range(9) if self.isCellFree(i)]

    def isWinner(self, le):
        return ((self.cells[6] == le and self.cells[7] == le and self.cells[8] == le) or # across the top
        (self.cells[3] == le and self.cells[4] == le and self.cells[5] == le) or # across the middle
        (self.cells[0] == le and self.cells[1] == le and self.cells[2] == le) or # across the self.cellsttom
        (self.cells[6] == le and self.cells[3] == le and self.cells[0] == le) or # down the left side
        (self.cells[7] == le and self.cells[4] == le and self.cells[1] == le) or # down the middle
        (self.cells[8] == le and self.cells[5] == le and self.cells[2] == le) or # down the right side
        (self.cells[6] == le and self.cells[4] == le and self.cells[2] == le) or # diagonal
        (self.cells[8] == le and self.cells[4] == le and self.cells[0] == le)) # diagonal

    def isBoardFull(self):
        for i in range(9):
            if self.isCellFree(i) == True:
                return False
        return True

    def makeMove(self, i, le):
        self.cells[i] = le
