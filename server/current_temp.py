#!/usr/bin/python

import requests

API_KEY = '5f18a65a9736c54298ad235cefb65eef'

def get_response(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY
	response = requests.get(url)
	return response.json()

def get_data_from_response(city):
	return_response = {}
	resp = get_response(city)['main']
	return_response['temp'] 	= float(resp['temp']) / 10
	return_response['temp_max'] 	= float(resp['temp_max']) / 10
	return_response['temp_min'] 	= float(resp['temp_min']) / 10
	return_response['humidity'] 	= resp['humidity']
	return return_response


def main():
	print get_data_from_response('pune')
	print get_data_from_response('mumbai')

if __name__ == '__main__':
	main()
