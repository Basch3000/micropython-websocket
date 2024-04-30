# micropython-websocket
Bare minimum to get websockets running on Raspberry Pi Pico W with Micropython.

I created this repository, because it seemed nearly impossible to get websockets running on a Raspberry Pi Pico W with MicroPython. This code is based on: https://github.com/danni/uwebsockets/

The differences between the original code and this repo:
1. logging is not a builtin module in MicroPython for the Raspberry Pi Pico W. I removed it and replaced it with a normal print.
2. usocketio was not used, so I removed it.
3. Added a main.py and boot.py
4. Added a timeout of 0.5 seconds, so read_frame does timeout, if the websocket server does not send something back
5. Added some exception handling for and in read_frame
6. Added an example irq in main.py, to handle GPIO input changes, while still looping and waiting for timeouts on the websocket-part

What this does:

It creates a WiFi-connection. Connects to the websocket-server and waits for incoming messages, while monitoring an input pin. It also prints the current milliseconds (since 1970) every half a second (and blinks the onboard LED) to verify that the timeout is working properly.

Note that this is just a working example created by a MicroPython beginner (me).
