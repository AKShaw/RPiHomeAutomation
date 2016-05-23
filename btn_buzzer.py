import time

class BtnBuzzer:
    """This class gets the button state and turns the buzzer on and off"""
    def __init__(self, board, btn_pin, buzz_pin):
        """Set the pins and board to properties"""
        self.board = board
        self.btn_pin = btn_pin
        self.buzz_pin = buzz_pin
        self.setup()
        print("Pins set up")

    def setup(self):
        """Setup the GPIO pins for the buzzer and button"""
        self.board.GPIO.setup(self.btn_pin, self.board.GPIO.IN, pull_up_down=self.board.GPIO.PUD_UP)
        self.board.GPIO.setup(self.buzz_pin, self.board.GPIO.OUT)

    def buzz_on(self):
        """Outputs high on the buzzer, making it buzz"""
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)

    def buzz_off(self):
        """Outputs low on the buzzer, turning it off"""
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)

    def getBtn(self):
        """This method returns 1 or 0 for the button state"""
        return self.board.GPIO.input(self.btn_pin)
        
