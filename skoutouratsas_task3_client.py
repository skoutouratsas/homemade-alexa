import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))
question=raw_input('Ask Alexa anything!(-1 to shut alexa down) :')

s.sendall(str(question))

data = s.recv(1024)

s.close()
print  "Alexa :" + repr(data)
