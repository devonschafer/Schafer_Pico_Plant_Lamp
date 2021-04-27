from machine import Pin, PWM, I2C, ADC
from time import sleep_ms, ticks_ms
import time
from esp8266_i2c_lcd import I2cLcd
from ButtonClass import Button
#from temp_class import overtemp
#from time_class import timer
#import utime

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def light():
    #65025
    #50000 max for 3.1 volts
    #18000 max for 2.1 volts
    
    pwm0 = PWM(Pin(3))
    pwm1 = PWM(Pin(4))
    pwm2 = PWM(Pin(2))
    #pwm freq
    pwm0.freq(240)
    pwm1.freq(240)
    pwm2.freq(240)
    #max brightness
    white_max = 50000
    red_max = 18000
    blue_max = 50000
    
    title = ''
    
    setting = '0'
    
    h_on = '0'
    
    total_h = 60
    
    h_off = total_h - int(h_on)
    
    start = time.time()
    
    brightness = {'RED':'0',
            'BLUE':'0',
            'WHITE':'0'}
    
    def display():
        lcd.clear()
        lcd.putstr('%s' % title)
        lcd.move_to(11, 0)
        lcd.putstr('%s' % setting)
    
    def lights_on():
        pwm0.duty_u16(int(brightness['BLUE']))
        pwm1.duty_u16(int(brightness['WHITE']))
        pwm2.duty_u16(int(brightness['RED']))
    
    def lights_off():
        pwm0.duty_u16(0)
        pwm1.duty_u16(0)
        pwm2.duty_u16(0)
        
    def schedule():
        on_time = int(h_on)
        check_sec = time.time() - start
        #check_min = check_sec / 60
        #check_hr = check_min / 60
        if int(h_on) != 0:
            lights_on()
            time.sleep(on_time)
            lights_off()
            time.sleep(int(h_off))
            
    while True:
        
        if Button.button1.value() == 1:
            title = 'BLUE'
            setting = brightness['BLUE']
            display()
        if title == 'BLUE':
            if Button.button7.value() == 1:
                if title == 'BLUE':
                    setting = int(brightness['BLUE']) + round((blue_max / 10))
                    brightness['BLUE'] = int(setting)
                    if int(setting) > blue_max:
                        setting = 0
                        brightness['BLUE'] = int(setting)
                    sleep_ms(500)
                display()
        
        if Button.button2.value() == 1:
            title = 'RED'
            setting = brightness['RED']
            display()
        if title == 'RED':
            if Button.button7.value() == 1:
                if title == 'RED':
                    setting = int(brightness['RED']) + round((red_max / 10))
                    brightness['RED'] = int(setting)
                    if int(setting) > red_max:
                        setting = 0
                        brightness['RED'] = int(setting)
                    sleep_ms(500)
                display()
                
        if Button.button3.value() == 1:
            title = 'WHITE'
            setting = brightness['WHITE']
            display()
        if title == 'WHITE':
            if Button.button7.value() == 1:
                if title == 'WHITE':
                    setting = int(brightness['WHITE']) + round((white_max / 10))
                    brightness['WHITE'] = int(setting)
                    if int(setting) > white_max:
                        setting = 0
                        brightness['WHITE'] = int(setting)
                    sleep_ms(500)
                display()
            
        if Button.button4.value() == 1:
            title = 'Time On'
            setting = h_on
            display()
        if title == 'Time On':
            if Button.button7.value() == 1:
                setting = int(h_on) + 1
                h_on = int(setting)
                if int(setting) > total_h:
                    setting = 0
                    h_on = int(setting)
                sleep_ms(500)
                display()
                
        if Button.button5.value() == 1:
            title = 'Schedule'
            setting = 'S Off'
            display()
        if title == 'Schedule':
            if Button.button7.value() == 1:
                title = 'Schedule'
                setting = 'S On'
                sleep_ms(500)
                display()
                schedule()
                
        if Button.button6.value() == 1:
            title = 'Manual'
            setting = 'M On'
            lights_on()
            display()
        if title == 'Manual':
            if Button.button7.value() == 1:
                title = 'Manual'
                setting = 'M Off'
                lights_off()
                sleep_ms(500)
                display()
            
        
        
while True:
    light()
    
    
    
    