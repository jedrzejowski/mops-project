from rooter import allRooters


def execute(start, step, end):
    for rooter in allRooters:

        ports = rooter.getPorts()
        for portName in rooter.getPorts():
            step(rooter=rooter, port=ports[portName])
