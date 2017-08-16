import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("Hello world !", 1)
lcd.lcd_display_string("je suis un", 2)
lcd.lcd_display_string("rover", 3)

