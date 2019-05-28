import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5000))
print "Waiting for connection.."


while 1:
	s.listen(1)
	conn, addr = s.accept()
	data = conn.recv(1024)
	print data
	if str(data)=='-1':
		break
	elif ('date' in data or 'time' in data):
		conn.sendall(str(datetime.datetime.now())) 
	elif ('birth' in data or 'birthday' in data or 'created' in data):
		conn.sendall("I was born on 7/12/2018.")
	elif ('favorite' in data and 'music' in data ):
		conn.sendall("I like electronic music.")
	elif ('favorite' in data and 'drink' in data ):
		conn.sendall("I like coffee.")
	elif ('where' in data and 'from' in data ):
		conn.sendall("I exist in the cloud.")
	elif ('world' in data and 'end' in data and 'when' in data ):
		conn.sendall('When unix time overflows. January 19, 2038')
	elif ("how" in data and "you" in data ):
		conn.sendall("I'm doing fine. How about you?")
	else:
		conn.sendall("I don't know the answer to this question...Yet.")
	
conn.close()
