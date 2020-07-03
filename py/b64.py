import base64
import pickle

a = [1, 2, 3, 4, 5]
g = pickle.dumps(a)
print(g)
b = base64.b64encode(g)
print(b)
print(b.decode())
c = b.decode()
with open("b64.pkl", "w") as bfile:
    bfile.write(c)
with open("b64.pkl", "r") as bfile:
    d = bfile.read()
e = d.encode()
f = base64.b64decode(e)
g = pickle.loads(f)
print(g)
