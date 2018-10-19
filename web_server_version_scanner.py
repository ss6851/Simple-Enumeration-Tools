import socket
import sys

try:		
	rhost=sys.argv[1]
	rport=int(sys.argv[2])
	#print "flag 1"
	sock_obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print "flag 1.5"
	sock_obj.connect((rhost, rport))
	#print "flag 2"
	sock_obj.send("GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
	response=sock_obj.recv(256)
	print response.split("\n")[2].split(": ")[1]
	sock_obj.close()

except:
	print" [*] Usage python web_server_scanner.py <target-ip> <target-port>"