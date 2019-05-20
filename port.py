from queue import Queue
from package import Package


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

    def hasInput(self):
        """
        :return:
        :rtype: bool
        """
        return self.__input.empty()

    def popInput(self, port):
        """
        :return:
        :rtype: Package
        """
        return self.__input.get()

    def hasOutput(self):
        """
        :return:
        :rtype: bool
        """
        return self.__output.empty()

    def popOutput(self, port):
        """
        :return:
        :rtype: Package
        """
        return self.__output.get()

    def putInInput(self, pkg):
        """
        :param pkg:
        :type pkg: Package
        :return:
        """
        self.__input.put(pkg)

    def putInOutput(self, pkg):
        self.__output.put(pkg)
