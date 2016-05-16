import time

class BtnBuzzer:
    def __init__(self, board, btn_pin, buzz_pin):
        self.board = board
        self.btn_pin = btn_pin
        self.buzz_pin = buzz_pin
        self.setup()
        print("Pins set up")

    def setup(self):
        self.board.GPIO.setup(self.btn_pin, self.board.GPIO.IN, pull_up_down=self.board.GPIO.PUD_UP)
        self.board.GPIO.setup(self.buzz_pin, self.board.GPIO.OUT)

    def buzz_on(self):
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)

    def buzz_off(self):
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)

    def getBtn(self):
        return self.board.GPIO.input(self.btn_pin)
        
