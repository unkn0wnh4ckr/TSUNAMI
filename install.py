#TSUNAMI INSTALL

# Color
W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'
LB = '\033[1;36m'





import os
import sys

print """

 __     __   __     ______     ______   ______     __         __        
/\ \   /\ "-.\ \   /\  ___\   /\__  _\ /\  __ \   /\ \       /\ \       
\ \ \  \ \ \-.  \  \ \___  \  \/_/\ \/ \ \  __ \  \ \ \____  \ \ \____  
 \ \_\  \ \_\\"\_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/   \/_/ \/_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_____/ 
                                                                        
"""

print G+"installing requirments..."

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

os.system("pip install socket")
os.system("pip install socks")
os.system("pip install time")
os.system("pip install random")
os.system("pip install datetime")
os.system("pip install subprocess")

from datetime import datetime
import time

print G+"install complete"
print Y+"EXITING INSTALLER.."
time.sleep(1)
print "---  0%"
time.sleep(1)
print "#--  10%"
time.sleep(1)
print "##-  50%"
time.sleep(2)
print "###  100%"
time.sleep(0.5)
sys.exit()
