from rooter import allRooters


def execute(start, step, end):
    global time

    for time in range(0, 1000):

        start(time)

        # for rooter in allRooters:
        #     ports = rooter.getPorts()
        #     for portName in rooter.getPorts():
        #         step(rooter=rooter, port=ports[portName])

        step()

        end(time)


def printStatus():
    for rooter in allRooters:
        print(rooter)
        ports = rooter.getPorts()
        for portName in rooter.getPorts():
            print("    ", end="")
            print(ports[portName])
