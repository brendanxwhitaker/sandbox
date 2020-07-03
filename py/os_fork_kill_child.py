import os
import signal

p = os.fork()
if p == 0:
    os.kill(os.getppid(), signal.SIGKILL)
else:
    while True:
        pass
