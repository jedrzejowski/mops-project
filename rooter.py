from port import Port
from package import Package

allRooters = []


class Rooter:
    def __init__(self, name):
        self.__ports = {}
        self.__name = name

        allRooters.append(self)

    def __str__(self):
        return f"Rooter({self.__name})"

    def getName(self):
        return self.__name

    def addPort(self, name):
        port = Port(name)
        self.__ports[name] = port
        return port

    def getPort(self, name):
        """

        :param name:
        :type name: str
        :return:
        :rtype: Port
        """
        return self.__ports[name]

    def getPorts(self):
        return self.__ports
