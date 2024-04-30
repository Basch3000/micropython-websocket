# boot.py -- run on boot-up
import network

SSID = "--YOUR SSID HERE--"
SSID_PASSWORD = "--YOUR WIFI PASSWORD HERE--"

WEBSOCKET_HOST = "--YOUR WEBSOCKET SERVER HOSTNAME OR IP HERE--"
WEBSOCKET_PORT = 1337

def do_connect():
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print("Connecting to '" + SSID + "'...")
		sta_if.active(True)
		sta_if.connect(SSID, SSID_PASSWORD)
		while not sta_if.isconnected():
			pass
	print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to '" + SSID + "'...")
do_connect()
