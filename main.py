from rooter import Rooter
from package import Package
import runtime as Runtime

# Definicje Rooterów

r1 = Rooter("1")
r1a = r1.addPort("a")
r1b = r1.addPort("b")

r2 = Rooter("2")
r2a = r2.addPort("a")
r2b = r2.addPort("b")

r3 = Rooter("3")
r3a = r3.addPort("a")
r3b = r3.addPort("b")


def start(time):
    # Host 1 generuje pakiet i wysyła go do rootera 1
    r1a.putInInput(Package(1, "heja"))


def step(rooter, port):
    pass


def end(time):
    Runtime.printStatus()


Runtime.execute(start, step, end)