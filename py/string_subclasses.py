from typing import Any, Tuple, Dict


class HostName(str):
    """ Allows different PSSH configurations on the same host. """

    def __new__(cls, value: str, *args: Tuple[Any, ...], **kwargs: Dict[str, Any]):
        return super().__new__(cls, value)

    def __init__(self, value: str, idx: int):
        super().__init__()
        self.idx = idx

    def __eq__(self, other: Any) -> bool:
        return self is other

    def __hash__(self) -> int:
        return id(self)


a = HostName("aaaaaaaaaaaa", 1)
print(a)
