from i2c import lcddriver
from time import *

if __name__ == "__main__":
    lcd = lcddriver.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Hello world !", 1)
    lcd.lcd_display_string("je suis un", 2)
    lcd.lcd_display_string("rover", 3)
