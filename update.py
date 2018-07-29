import os
import sys
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

print G+"updating TSUNAMI"

print N+"update started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(2)

os.system("cd ..")
os.system("rm -fr TSUNAMI")

time.sleep(1)
print "-----  0%"
time.sleep(1)
print "#----  20%"
time.sleep(1)
print "##---  40%"
time.sleep(2)
print "###--  60%"
time.sleep(2)
print "###--   80%"
time.sleep(2.5)
print "#####  100%"

os.system("git clone https://github.com/unkn0wnh4ckr/TSUNAMI")

print G+"update complete"
print "exiting.."
time.sleep(3)
print "---  0%"
time.sleep(1)
print "#--  10%"
time.sleep(1)
print "##-  50%"
time.sleep(2)
print "###  100%"
time.sleep(0.5)
sys.exit()
