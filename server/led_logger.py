#!/usr/bin/python

import logging as led_log

led_log.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename = 'led_events.log', level=led_log.DEBUG)
