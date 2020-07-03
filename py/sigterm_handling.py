from time import sleep
import signal
import multiprocessing as mp


_SIGTERM = None


def sigterm_handler(signum, frame):
    global _SIGTERM
    _SIGTERM.set()


def func(sigterm):
    print(f"Start job: {mp.current_process().name}")
    while True:
        sleep(3)
        print("Hardworking!")
        if sigterm.is_set():
            print("Will stop by signal")
            break
    print("End job")


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    mp.set_start_method("spawn")
    _SIGTERM = mp.Event()
    processes = [mp.Process(target=func, args=(_SIGTERM,)) for x in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]
