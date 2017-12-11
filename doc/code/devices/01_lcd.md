# LCD screen

A LCD screen is used on the rover to display informations like the status of
the GPS and various captors. The screen is composed of 4 lines and is 24
characters wide.

The driver for the LCD screen is written in Python3 and uses I2C to
communicate with the device.

**The prototype of the main function is:**

```python
lcd_display_string(string, line)
```

With:

* string: is the string to display (with a maximum length of 20)
* line: the line where to display the string (0 to 3)
