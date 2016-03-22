class SetLED():
    def __init__(self, line1, line2, board):
        self.line1 = line1
        self.line2 = line2
        self.board = board
        
    @property
    def getLine1(self):
        return self.line1

    def setLine1(self, value):
        self.line1 = value

    @property
    def getLine2(self):
        return self.line2

    def setLine2(self, value):
        self.line2 = value
