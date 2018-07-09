import logging
LOGGER = logging.getLogger()

import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
print("IP Address = ", get_ip_address())

import wingdbstub
# set your breakpoint on the next line
print("Stop at this breakpoint!")

######################################################################
## If you are having troubles with getting breakpoints to work, you can
## get a lot of information by uncommenting these next lines **AND**
## uncommenting the section labeled "BREAKDPOINT-DEBUGGING" in the
## wingdbstub.py file that is included with this project.
##with open('/tmp/wing-docker-debug.log', 'r') as logfile:
##    for line in logfile:
##        print line,