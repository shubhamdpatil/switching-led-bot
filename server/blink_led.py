#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from led_logger import *

# initialisation
LED_PIN = 18


def init():
	led_log.info('Pins initialized')
	print 'Initializing pins'

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(LED_PIN, GPIO.OUT)

	led_log.debug('setting GPIO pin ' + str(LED_PIN) + ' to OUT')


def get_state_led():
	GPIO.setup(LED_PIN, GPIO.IN)
	state = GPIO.input(LED_PIN)
	GPIO.setup(LED_PIN, GPIO.OUT)

	led_log.debug('current state of light is ' + str(state))

	return state


def turn_on_led():
	if get_state_led() == 1:
		print 'LED already on'
		return

	GPIO.output(LED_PIN, GPIO.HIGH)

	led_log.debug('setting GPIO pin ' + str(LED_PIN) + ' to HIGH')
	print 'LED turned on'


def turn_off_led():
	if get_state_led() == 0:
		print 'LED is off skipping'
		return

	GPIO.output(LED_PIN, GPIO.LOW)

	led_log.debug('setting GPIO pin ' + str(LED_PIN) + ' to LOW')
	print 'LED turned off'


def cleanup():
	GPIO.cleanup()
	print 'Resetting pins'

	led_log.info('Resseting pins for cleanup')


def main():
	init()
	print get_state_led()
	turn_on_led()
	sleep(2)
	turn_off_led()
	sleep(2)
	turn_on_led()
	sleep(2)
	turn_off_led()
	sleep(2)
	cleanup()


if __name__ == '__main__':
	main()
