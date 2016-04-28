#!/usr/bin/python

import signal
import sys
import time

def interruptHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, interruptHandler)
    while True:
        print "Hello Internet Of Things"
        time.sleep(5)

# End of File
