from queue import Queue
from package import Package


class Port:
    def __init__(self, name):
        self.__name = name
        self.__input = []
        self.__output = []

    def __str__(self):
        i = len(self.__input)
        o = len(self.__output)
        return f"Port(name={self.__name}, inlen={i}, outlen={o})"

    def getName(self):
        return self.__name

    def hasInput(self):
        """
        :return:
        :rtype: bool
        """
        return len(self.__input) > 0

    def popInput(self):
        """
        :return:
        :rtype: Package
        """
        return self.__input.pop(0)

    def hasOutput(self):
        """
        :return:
        :rtype: bool
        """
        return len(self.__output) > 0

    def popOutput(self):
        """
        :return:
        :rtype: Package
        """
        return self.__output.pop(0)

    def putInInput(self, pkg):
        """
        :param pkg:
        :type pkg: Package
        :return:
        """
        self.__input.append(pkg)

    def putInOutput(self, pkg):
        self.__output.append(pkg)
