import time
import RPi.GPIO as io
io.setmode(io.BOARD)

pir_pin = 3
led_pin = 5

io.setup(pir_pin, io.IN)         # activate input
io.setup(led_pin, io.OUT)

def toggle_pin:
	if io.

try:
	led_off = True
	while True:
		if led_off:
			io.output(led_pin, 1)
		else:
			io.output(led_pin, 0)

		if io.input(pir_pin):
			led_off = False
		else:
			led_off = True
		
		time.sleep(0.1)
		

finally:

	io.cleanup()
