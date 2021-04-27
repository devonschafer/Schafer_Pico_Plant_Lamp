# Schafer_Pico_Plant_Lamp
DIY red, white, and blue plant lamp for indoor plants using the Raspberry Pi Pico

When loading the files to the Pico. Put ButtonClass.py, esp8266_i2c_lcd.py, lcd_api.py into a folder called lib.
These are classes that will be called later by main.py
Then add main.py into the main space of the pico.

Parts I used:
QPass 16X2 LCD 1602A driver
Raspberry Pi Pico
On/Off Switch
7: momentary button switches
680uf aluminum electrolytic capacitor
micro female usb connector
3: 24 ohm 1/4W resistor (SMD)
3: transistors (collector to base 40v, emitter to base 5v, maximum DC collector current 1.5A ( part no. MMSS8050-H-TP ))

You do not have to use the same exact parts I used of course.
