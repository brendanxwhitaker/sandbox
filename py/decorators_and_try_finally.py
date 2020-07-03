import os
import sys
from typing import Callable


def marthastewart(
    printable: str,
) -> Callable[[Callable[[int], int]], Callable[[int], int]]:
    def decorator(fn: Callable[[int], int]) -> Callable[[int], int]:
        def decorated(n: int) -> int:
            print(printable)
            return fn(n)

        return decorated

    return decorator


@marthastewart("General Kenobi!")
def add_one(n: int) -> int:
    return n + 1


def white():
    try:
        return True
    finally:
        return False


def yellow():
    try:
        sys.exit()
    finally:
        return False


def orange():
    try:
        raise SystemExit
    finally:
        return False


def red():
    try:
        os.system("kill %d" % os.getpid())
    finally:
        return False


class Class:
    a = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    @classmethod
    def test(cls):
        print(cls.a)


if __name__ == "__main__":
    mc = Class()
    print(dir(mc))
    pass
