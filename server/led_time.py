#!/usr/bin/python

import datetime

def get_total_time():

	log_file = open('led_events.log', 'r')
	lines = log_file.readlines()
	diff_time_array = []

	diff_time = None
	st_time = ''
	end_time = ''

	for line in lines:
		if 'HIGH' in line:
			st_time = line[0 : line.find(',')]
		elif 'LOW' in line:
			end_time = line[0 : line.find(',')]
		#	print end_time, st_time
			diff_time_array.append((datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(st_time, '%Y-%m-%d %H:%M:%S')))


	x = diff_time_array[0]
	for diff_time in diff_time_array:
		x = x + diff_time

	return str(x)


if '__main__' == __name__:
	print str(get_total_time())
