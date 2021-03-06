import time

class PhotoResistor():
    """This class gets the current light le el from the LDR"""
    def __init__(self, pin, board):
        self.pin = pin
        self.board = board

    def getLux(self):
        """This method works out the time taken for a capacitor to discharge which gives a lux level"""
        reading = 0
        self.board.GPIO.setup(self.pin, self.board.GPIO.OUT)
        self.board.GPIO.output(self.pin, self.board.GPIO.LOW)
        time.sleep(0.1)
 
        self.board.GPIO.setup(self.pin, self.board.GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (self.board.GPIO.input(self.pin) == self.board.GPIO.LOW):
                reading += 1
        return reading
        
