from rooter import allRooters


def execute(start, step, end):
    global time

    for time in range(0, 1000):

        print(f"Start of {time}")

        start(time)

        iters = []

        # Interujemy po wszystkich portach
        for rooter in allRooters:

            ports = rooter.getPorts()

            for portName in rooter.getPorts():

                port = ports[portName]

                outpkg = None
                inpkg = None

                if port.hasInput():
                    inpkg = port.popInput()
                if port.hasOutput():
                    outpkg = port.popOutput()

                iters.append([rooter, port, inpkg, outpkg])

        for i in iters:
            step(i[0], i[1], i[2], i[3])

        end(time)


def printStatus():
    for rooter in allRooters:
        print(rooter)
        ports = rooter.getPorts()
        for portName in rooter.getPorts():
            print("    ", end="")
            print(ports[portName])
