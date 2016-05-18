import time

class PirBuzzer:
    def __init__(self, board, pir_pin, buzz_pin):
        self.board = board
        self.pir_pin = pir_pin
        self.buzz_pin = buzz_pin
        self.board.GPIO.setup(self.pir_pin, self.board.GPIO.IN)
        self.board.GPIO.setup(self.buzz_pin, self.board.GPIO.OUT)
        self.board.GPIO.add_event_detect(pir_pin, board.GPIO.FALLING, callback=self.buzz, bouncetime=300)

    def buzz(self, pin):
        print("PIR Detetced")
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)
        time.sleep(0.1)
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)
        
