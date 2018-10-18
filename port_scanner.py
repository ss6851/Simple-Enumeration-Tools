import socket 
import sys
import subprocess

subprocess.call('clear', shell=True)
try:		
	rhost = sys.argv[1]
	#rport = sys.argv[2]
	try:
		for rport in range(1,1025):
			#print "[*] Checking for port ",rport
			conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = conn.connect_ex((rhost, rport))	
			if result==0:
				print "[*] Port",rport,"/tcp is open"
			conn.close()
	except:
		print":( Unidentified error occurred."
except:
	print"[+] Usage: python port_scanner <target-ip>"