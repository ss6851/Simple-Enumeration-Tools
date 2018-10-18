import socket 
import sys
import subprocess
subprocess.call('clear', shell=True)
try:		
	rhost = sys.argv[1]
	file_contents = open(sys.argv[2],"r").readlines()
	count =0
	print"-"*60
	print"\n[+] Checking which directories exist on the web server\n"
	print"-"*60,"\n"
	for i in file_contents:
		data="GET ",i.split("\n")[0]," HTTP/1.1\r\n\r\n"
		http_request=''.join(data)
		#print http_request
		sock_obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_obj.connect((rhost, 80))
		sock_obj.send(http_request)
		#print "flag1"
		response=sock_obj.recv(1024)
		if int(response.split("\n")[0].split(" ")[1]) ==200:
			print i
			count+=1
		sock_obj.close
	if count==0:
		print":( Sorry no files were found on the web server."
except:
	print"[+] Usage: python dir_buster.py <target-ip> <wordlist>"