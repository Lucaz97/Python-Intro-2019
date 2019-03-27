
class Player:

    # inizializzatore, viene eseguito quando faccio Board()
    def __init__(self, nickname, le):
        self.nickname = nickname
        self.le = le

    # getters, è buona pratica accedere agli attributi di una classe indirettamente
    def getNickname(self):
        return self.nickname

    def getLetter(self):
        return self.le

    def pickMove(self, freeCells):
        move = ''
        while move not in freeCells:
            print("Insert your next move")
            move = int(input())
        return (move, self.le)
