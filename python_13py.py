from machine import pin
import time


BUTTON_PIN = 0
LED_PIN = 4
PRESSD_VAULE = 0 # 
ON_VAULE = 1
OFF_VAULE = 0

button= pin(BUTTON_PIN, pin.IN pin PULL_up)
led= pin(LED_PIN, Pin.OUT value=OFF_VALUE)

while True:
    if button.value() == PRESSED_VALUE:
        led.value(ON_VALUE)
    else:
        led.value(OFF_VALUE)
    time.sleep(0.05)