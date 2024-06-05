#!/usr/bin/python
from signal import signal, Signals
import time
# from pprint import pprint as pp

GOT_SIGNAL = 0
def sig_handler(sig, frame):
    print("signal", sig, frame)
    # pp(Signals(GOT_SIGNAL))
    # global GOT_SIGNAL
    # GOT_SIGNAL = sig


for sig in Signals:
    try:
        signal(sig, sig_handler)
    except (ValueError, OSError, RuntimeError) as m:
        print("Skipping ", sig)

# press some keys or issue kill

if __name__ == "__main__":
    x = 0
    while not GOT_SIGNAL:
        time.sleep(4)
        x += 1
    pp(Signals(GOT_SIGNAL))