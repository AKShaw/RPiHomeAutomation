class PirBuzzer:
    def __init__(self, board, pir_pin, buzz_pin):
        self.board = board
        self.buzz_pin = buzz_pin
        board.GPIO.setup(pir_pin, board.GPIO.IN)
        board.GPIO.setup(buzz_pin, board.GPIO.OUT)
        board.GPIO.add_event_detect(pir_pin, board.GPIO.FALLING, callback=self.buzz, bouncetime=300)

    def detectMotion(self):
        while True:
            if board.GPIO.input(PIR_PIN):
                print ("Motion")
            else:
                print("No motion")
            time.sleep(1)

    def buzz(self):
        board.GPIO.output(self.buzz_pin, board.GPIO.HIGH)
        time.sleep(0.1)
        board.GPIO.output(self.buzz_pin, board.GPIO.LOW)
        
