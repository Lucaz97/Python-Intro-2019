
class Player:

    def __init__(self, nickname, le):
        self.nickname = nickname
        self.le = le

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
