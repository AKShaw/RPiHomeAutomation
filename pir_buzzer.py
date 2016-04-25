import time

class PirBuzzer:
    def __init__(self, board, pir_pin, buzz_pin):
        self.board = board
        self.pir_pin = pir_pin
        self.buzz_pin = buzz_pin
        self.board.GPIO.setup(pir_pin, board.GPIO.IN)
        self.board.GPIO.setup(buzz_pin, board.GPIO.OUT)
        self.board.GPIO.add_event_detect(pir_pin, board.GPIO.FALLING, callback=self.buzz, bouncetime=300)

    def detectMotion(self):
        while True:
            if board.GPIO.input(PIR_PIN):
                print ("Motion")
            else:
                print("No motion")
            time.sleep(1)

    def buzz(self):
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)
        time.sleep(0.1)
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)
        
