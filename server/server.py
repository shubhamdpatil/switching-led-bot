#!/usr/bin/python

import socket 
from blink_led import *
from led_time import *

# initialize pins
init()

s = socket.socket()
port = 9988
s.bind(('10.71.71.150', port))

led_log.debug('Binding to port 9988')

print 'listening on port 9988'
s.listen(2)


while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr
	led_log.debug('New client connected ' + str(addr))

	cmd = c.recv(1024)
	print 'Received: ' + cmd
	led_log.debug('Received: ' + cmd)

	if cmd == 'on':
		turn_on_led()
		c.send('OK')
	
	elif cmd == 'off':
		turn_off_led()
		c.send('OK')
	elif cmd == 'get_time':
		time = get_total_time()
		c.send(time)

	elif cmd == 'get_state':
		state = get_state_led() == '1' and 'on' or 'off'
		c.send('current state of light is ' + (state))

	elif cmd == 'disconnect':
		break

s.close()
cleanup()

led_log.debug('Connection is closed')
print 'closing all connections and shutting server'
