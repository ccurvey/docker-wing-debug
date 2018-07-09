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

with open('/tmp/wing-docker-debug.log', 'r') as logfile:
    for line in logfile:
        print line,