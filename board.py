import RPi.GPIO
from time import sleep

class Board:
    
    def __init__(self):
        self.GPIO = RPi.GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.mode = self.GPIO.getmode()
        self.rpi_version = self.GPIO.VERSION

    def print_gpio_details(self):
        if self.mode == 11:
            mode = 'BCM'
        elif self.mode == 10:
            mode = 'BOARD'
        else:
            mode = 'Error'
        print('Board is set to mode ' + mode)
        print('RPi version is ' + str(self.rpi_version))

    def clean_up(self):
        self.GPIO.cleanup()

if __name__ == "__main__":

    # main program
    rpi = Board()
    rpi.print_gpio_details()

    
