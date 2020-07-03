import sys
import signal


def handler(sig, frame):
    print("You pressed Ctrl+C.")
    sys.exit(0)


signal.signal(signal.SIGINT, handler)
signal.pause()
