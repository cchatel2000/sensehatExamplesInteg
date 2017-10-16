#!/usr/bin/python
import sys

from evdev import InputDevice, list_devices, ecodes
from select import select

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
    sys.exit()

def getKey():
    ry,w,x = select([dev.fd], [], [], 0)

    # if there is something to be read from dev
    if ry:
       for event in dev.read():
         if event.type == ecodes.EV_KEY:
            if event.value == 1:  # key down
                if event.code == ecodes.KEY_ENTER:
                    print "Touche enter"
                    return 1
	        elif event.code == ecodes.KEY_DOWN:
		    return 2
                elif event.code == ecodes.KEY_UP:
                    return 3
                elif event.code == ecodes.KEY_LEFT:
                    return 4
                elif event.code == ecodes.KEY_RIGHT:
                    return 5
    return 0

