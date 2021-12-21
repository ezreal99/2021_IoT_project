import Adafruit_DHT
from lcd import drivers
import datetime
import time

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 4

i=1

try:
    while True:
        display.lcd_display_string('* * * * * * * * ', i)
        display.lcd_display_string(' * * * * * * * *', i)
        display.lcd_display_string('* * * * * * * * ', i+1)
        display.lcd_display_string(' * * * * * * * *', i+1)
        time.sleep(0.01)
finally:
    print("Cleaning up!")
    display.lcd_clear()