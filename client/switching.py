import os.path
import sys
import json

from socketPython import socketConnection 

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '279ed4bd0cfe4dce996d1517cde6c995'

def main():
    while 1:
	ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'de'  # optional, default value equal 'en'
        request.query = raw_input('YOU: ')
	if 'how' in request.query and 'long' in request.query and 'light' in request.query:
		socketConnection('get_time')
		continue

        if ( request.query == 'bye' or request.query == 'BYE'):
             print "Bye! see you again."
             break;
        else:
             response = request.getresponse()
             str1 = json.loads(response.read())

	     res = str1['result']['fulfillment']
	     #print res
	     try:
		 socketConnection(res["speech"])
		 print 'nibblot says: ' + res["speech"]
	     except:
		 print 'Sorry i didn\'t understand'

                        


if __name__ == '__main__':
    main()
