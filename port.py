from queue import Queue

class Port:
    def __init__(self, name):
        self.__name = name
        self.__input = Queue()
        self.__output = Queue()

    def __str__(self):
        i = self.__input.qsize()
        o = self.__output.qsize()
        return f"Port(name={self.__name}, inlen={i}, outlen={o})"

    def getName(self):
        return self.__name

    def popInputTo(self, port):
        pkg = self.__input.get()
        port.putInOutput(pkg)
        pass

    def popOutputTo(self, port):
        pkg = self.__output.get()
        port.putInInput(pkg)
        pass

    def putInInput(self, pkg):
        self.__input.put(pkg)

    def putInOutput(self, pkg):
        self.__output.put(pkg)
