from machine import Pin
import uwebsockets.client
import os, time
import neopixel

# ONBOARD LED
led = Pin("LED", Pin.OUT)

# Input PIN (PIR in this case)
p0 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# pin 20
#n = neopixel.NeoPixel(Pin(20), 1)
#n[0] = (0, 0, 0)
#n.write()

websocket = uwebsockets.client.connect("ws://" + WEBSOCKET_HOST + ":" + str(WEBSOCKET_PORT) + "/")
websocket.settimeout(0.5) 
mesg = 'Say hello to the websocket server here.'
websocket.send(mesg + "\r\n")

def callback(p):
	print('pin change', p)

p0.irq(trigger=Pin.IRQ_RISING, handler=callback)

def blink():
	led.toggle()

def current_milli_time():
	return round(time.time() * 1000)

while True:
	# time.sleep(0.5)
	print(current_milli_time())
	blink()
	resp = websocket.recv()
	if(resp):
		print("Websocket message: " + resp)
	

