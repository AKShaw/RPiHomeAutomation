import time

class PirBuzzer:
    """This class is responsible for listening for an input from the PIR sensor and buzzing the buzzer"""
    def __init__(self, board, pir_pin, buzz_pin):
        self.board = board
        self.pir_pin = pir_pin
        self.buzz_pin = buzz_pin
        self.board.GPIO.setup(self.pir_pin, self.board.GPIO.IN)
        self.board.GPIO.setup(self.buzz_pin, self.board.GPIO.OUT)
        """This line creates an event that detects the PIR pin. When the PIR detects movement, it triggers this which calls the buzzer method"""
        self.board.GPIO.add_event_detect(pir_pin, board.GPIO.FALLING, callback=self.buzz, bouncetime=300)

    def buzz(self, pin):
        """This method sets the buzzer on for 0.1 second before turning it off"""
        print("PIR Detetced")
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.HIGH)
        time.sleep(0.1)
        self.board.GPIO.output(self.buzz_pin, self.board.GPIO.LOW)
        
