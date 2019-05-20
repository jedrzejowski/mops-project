from rooter import allRooters


def execute(start, step, end):
    start()

    for rooter in allRooters:
        ports = rooter.getPorts()
        for portName in rooter.getPorts():
            step(rooter=rooter, port=ports[portName])

    end()


def printState():
    for rooter in allRooters:
        print(rooter)
        ports = rooter.getPorts()
        for portName in rooter.getPorts():
            print(ports[portName], end="")
