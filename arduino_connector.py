import serial.tools.list_ports
import warnings
from psychopy import visual, core, event, clock
import random

ser=None


def connect_to_arduino():
    global ser
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description  # may need tweaking to match new arduinos
    ]
    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) > 1:
        warnings.warn('Multiple Arduinos found - using the first')

    ser = serial.Serial(arduino_ports[0], 9600, timeout=0)

def vibrate(duration):
    milliseconds_duration = duration * 1000
    timer = core.Clock()
    timer.add(duration)
    while timer.getTime() < 0:
        is_vibrating_now = random.randint(0, 1)
        ser.write(bytes([is_vibrating_now]))
        core.wait(0.2)
        ser.flush()
    ser.write(bytes([0]))
    ser.flush()
