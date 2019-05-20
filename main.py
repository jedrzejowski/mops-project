from rooter import Rooter
from package import Package
import runtime as Runtime

# Definicje Rooterów

r1 = Rooter("R1")
r1.addPort("a")
r1.addPort("b")
r1.addPort("c")

r2 = Rooter("R2")
r2.addPort("a")
r2.addPort("b")
r2.addPort("c")

r3 = Rooter("R3")
r3.addPort("a")
r3.addPort("b")
r3.addPort("c")


def start(time):
    # Host 1 generuje pakiet i wysyła go do rootera 1
    r1.getPort("a").putInInput(Package(1, "heja"))

    r1.getPort("c").putInInput(Package(2, "heja"))

    r2.getPort("c").putInInput(Package(3, "heja"))


def step(rooter, port, inpkg, outpkg):
    """

    :param rooter:
    :param port:
    :param inpkg:
    :param outpkg:
    :return:
    :type rooter: Rooter
    :type port: Port
    :type inpkg: Package
    :type outpkg: Package
    """

    id = rooter.getName() + ":" + port.getName()

    # Rooter 1
    if "R1:a" == id:

        if inpkg is not None:
            if inpkg.getHeader() == 1:
                r1.getPort("b").putInOutput(inpkg)

        if outpkg is not None:
            pass

    if "R1:b" == id:

        if inpkg is not None:
            pass

        if outpkg is not None:
            r2.getPort("a").putInInput(outpkg)

    if "R1:c" == id:

        if inpkg is not None:
            if inpkg.getHeader() == 2:
                r1.getPort("b").putInOutput(inpkg)

        if outpkg is not None:
            pass

    # Rooter 2
    if "R2:a" == id:

        if inpkg is not None:
            if inpkg.getHeader() == 1:
                r2.getPort("b").putInOutput(inpkg)
            if inpkg.getHeader() == 2:
                r2.getPort("c").putInOutput(inpkg)

        if outpkg is not None:
            pass

    if "R2:b" == id:

        if inpkg is not None:
            pass

        if outpkg is not None:
            r3.getPort("a").putInInput(outpkg)

    if "R2:c" == id:

        if inpkg is not None:
            if inpkg.getHeader() == 1:
                r2.getPort("b").putInOutput(inpkg)
            if inpkg.getHeader() == 3:
                r2.getPort("b").putInOutput(inpkg)

        if outpkg is not None:
            pass

    # Rooter 3
    if "R3:a" == id:

        if inpkg is not None:
            if inpkg.getHeader() == 3:
                r3.getPort("c").putInOutput(inpkg)
            if inpkg.getHeader() == 1:
                r3.getPort("b").putInOutput(inpkg)

        if outpkg is not None:
            pass

    if "R3:b" == id:

        if inpkg is not None:
            pass

        if outpkg is not None:
            pass

    if "R3:c" == id:

        if inpkg is not None:
            pass

        if outpkg is not None:
            pass


def end(time):
    Runtime.printStatus()


Runtime.execute(start, step, end)

print("end")
