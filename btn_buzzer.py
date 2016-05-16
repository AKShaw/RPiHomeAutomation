import time

class BtnBuzzer:
    def __init__(self, board, btn_pin, buzz_pin):
        self.board = board
        self.btn_pin = btn_pin
        self.buzz_pin = buzz_pin
        self.board.GPIO.setup(btn_pin, board.GPIO.IN)
        self.board.GPIO.setup(buzz_pin, board.GPIO.OUT)
        self.board.GPIO.add_event_detect(btn_pin, board.GPIO.FALLING, callback=self.buzz, bouncetime=500)

    def buzz(self, pin):
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)
        time.sleep(0.5)
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)
        
