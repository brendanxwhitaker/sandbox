import sys
from typing import Any
import pssh
from pssh.clients import ParallelSSHClient


class HostName(str):
    """ Allows different PSSH configurations on the same host. """

    def __eq__(self, other: Any) -> bool:
        return self is other

    def __hash__(self) -> int:
        return id(self)


hostname = HostName("localhost")
client = ParallelSSHClient([hostname])
output = client.run_command("lssdf")
print("retry delay:", pssh.constants.RETRY_DELAY)
print(output)
out = output[hostname]
print(out)
print(dir(out))
print("Exception:", out.exception)
print("Exit code:", out.exit_code)
for line in out.stdout:
    print(line)
print("Client dir:", dir(client))
print("Client hosts:", client.hosts)
for host in client.hosts:
    print("Type of host:", type(host))
