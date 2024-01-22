import machine 
import time 

led= machine.Pin('LED', machine.Pin.OUT)

While (True):
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(.5)
    