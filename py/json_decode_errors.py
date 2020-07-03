import json

try:
    buf = json.loads('{"hello": 1}')
    assert False
except (json.decoder.JSONDecodeError, ValueError):
    pass

print(type(buf["hello"]))
