#client example
import socket

def socketConnection( response_data ): 
#	print 'in socket: ' + str(response_data)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	host = '10.71.71.150'
    	client_socket.connect((host, 9988))

    	if 'on' in response_data and 'Light' in response_data:
        	data = 'on'

    	elif 'off' in response_data and 'light' in response_data:  
        	data = 'off'

   	elif 'get_time' in response_data:
		data = 'get_time'

	elif 'current state of light is' in response_data:
		data = 'current state of light'

   	elif 'disconnect' in response_data:
        	data = 'disconnect'
   	else:
		return
 
        if ( data == 'q' or data == 'Q'):
        	client_socket.close()
        else:
		client_socket.send(data)
		print "RECIEVED: " , client_socket.recv(1024)
		client_socket.close()
