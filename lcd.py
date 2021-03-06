from lcd1602 import LCD1602

class SetLCD():
    """This class holds the current LCD lines and sets the text ton the LCD screen"""
    def __init__(self, line1, line2, board):
        self.line1 = line1
        self.line2 = line2
        self.board = board
        self.lcd = LCD1602()
        
    @property
    def getLine1(self):
        return self.line1

    def setLine1(self, value):
        """This sets the LCD text for line 1 and stores it"""
        self.lcd.lcd_string(value, self.lcd.LCD_LINE_1)
        self.line1 = value

    @property
    def getLine2(self):
        return self.line2

    def setLine2(self, value):
        """This sets the LCD text for line 2 and stores it"""
        self.lcd.lcd_string(value, self.lcd.LCD_LINE_2)
        self.line2 = value
