from rooter import Rooter
from package import Package
import runtime as Runtime

# Definicje Rooterów

r1 = Rooter("1")
r1a = r1.addPort("a")
r1b = r1.addPort("b")
r1c = r1.addPort("c")

r2 = Rooter("2")
r2a = r2.addPort("a")
r2b = r2.addPort("b")

r3 = Rooter("3")
r3a = r3.addPort("a")
r3b = r3.addPort("b")
r3c = r1.addPort("c")


def pipeOut2In(port1, port2):
    if port1.hasOutput():
        pkg = port1.popInput()
        port2.putInInput(pkg)


def start(time):
    # Host 1 generuje pakiet i wysyła go do rootera 1
    r1a.putInInput(Package(1, "heja"))

    r1c.putInInput(Package(2, "heja"))

    r2a.putInInput(Package(3, "heja"))


def step():
    # Rooter 1

    if r1a.hasInput():
        pkg = r1a.popInput()
        if pkg.getHeader() == 1:
            r1b.putInOutput(pkg)

    if r1c.hasInput():
        pkg = r1c.popInput()
        if pkg.getHeader() == 2:
            r1b.putInOutput(pkg)

    pipeOut2In(r1b, r2a)

    # Rooter 2

    if r2a.hasInput():
        pkg = r2a.popInput()
        if pkg.getHeader() == 1:
            r2b.putInOutput(pkg)

    if r2b.hasOutput():
        pkg = r2b.popInput()
        r3a.putInInput(pkg)

    # Rooter 3


def end(time):
    Runtime.printStatus()


Runtime.execute(start, step, end)
