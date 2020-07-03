import random
from abc import abstractmethod
from typing import List, Any, Tuple

import pytest
import hypothesis.strategies as st
from hypothesis import given


class SM:
    def __init__(self):
        self.start_state = 0
        self.state = 0

    def start(self):
        self.state = self.start_state

    def step(self, inp: Any) -> Any:
        s, o = self.get_next_values(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs: List[Any]) -> List[Any]:
        self.start()
        return [self.step(inp) for inp in inputs]

    @abstractmethod
    def get_next_values(self, state: int, inp: Any) -> Tuple[int, Any]:
        raise NotImplementedError


class Ninja(SM):
    def __init__(self):
        super().__init__()
        self.start_state = 1

    def get_next_values(self, state: int, inp: str) -> Tuple[int, bool]:
        print("State: %d | Input: %s" % (state, inp))
        if state == 1:
            if inp == "n":
                return 2, False
            return 1, False

        if state == 2:
            if inp == "i":
                return 3, False
            return 1, False

        if state == 3:
            if inp == "n":
                return 4, False
            return 1, False

        if state == 4:
            if inp == "j":
                return 5, False
            return 1, False

        if state == 5:
            if inp == "a":
                return 6, True
            return 1, False

        if state == 6:
            return 6, True

        raise ValueError("Invalid state.")


class Samurai(SM):
    def __init__(self):
        super().__init__()
        self.start_state = 1

    def get_next_values(self, state: int, inp: str) -> Tuple[int, bool]:
        # print("State: %d | Input: %s" % (state, inp))
        if state == 1:
            if inp == "n":
                return 2, False
            return 1, False

        if state == 2:
            if inp == "n":
                return 2, False
            if inp == "i":
                return 3, False
            return 1, False

        if state == 3:
            if inp == "n":
                return 4, False
            return 1, False

        if state == 4:
            if inp == "n":
                return 2, False
            if inp == "i":
                return 3, False
            if inp == "j":
                return 5, False
            return 1, False

        if state == 5:
            if inp == "n":
                return 2, False
            if inp == "a":
                return 6, True
            return 1, False

        if state == 6:
            return 6, True

        raise ValueError("Invalid state.")


@pytest.mark.skip
@given(st.from_regex(r"[ninja123]+", fullmatch=True), st.booleans())
def test_ninja(s: str, use_ninja: bool) -> None:
    if use_ninja:
        k = random.randint(0, len(s) - 1)
        s = s[:k] + "ninja" + s[k:]
    if "ninja" in s:
        print(s)
    ninja = Ninja()
    outs: List[bool] = ninja.transduce(list(s))
    print(outs)
    assert ("ninja" in s) == any(outs)


@given(st.from_regex(r"[ninja123]+", fullmatch=True), st.booleans())
def test_samurai(s: str, use_ninja: bool) -> None:
    if use_ninja:
        k = random.randint(0, len(s) - 1)
        s = s[:k] + "ninja" + s[k:]
    if "ninja" in s:
        print(s)
    ninja = Samurai()
    outs: List[bool] = ninja.transduce(list(s))
    print(outs)
    assert ("ninja" in s) == any(outs)
