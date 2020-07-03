import traceback

try:
    1 + "a"
except Exception as _:
    traceback.print_exc()

try:
    with open("hello/hello/hello.txt", "r") as opefile:
        opefile.close()
except Exception as _:
    a = traceback.format_exc()
    pass
print(a)
