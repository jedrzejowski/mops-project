from rooter import Rooter
from package import Package
import runtime as Runtime

# Definicje Rooterów

r1 = Rooter("1")
r2 = Rooter("2")
r3 = Rooter("3")

r1.addPort("a")
r1.addPort("b")
r2.addPort("a")
r2.addPort("b")
r3.addPort("a")
r3.addPort("b")


def start():
    pass


def step(rooter, port):
    print(rooter)
    print(port)


def end():
    pass


Runtime.execute(start, step, end)
