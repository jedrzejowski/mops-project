import numpy as numpy

from event import Event
from package import Package


class Host:
    def __init__(self, name, rooter=None, lam=100):
        self.__name = name
        self.__lam = lam
        self.__rooter = rooter

        self.genPkg()

    def getName(self):
        return self.__name

    def acceptPkg(self, pkg):
        pass

    def genPkg(self):
        if self.__rooter is None:
            return

        delay = numpy.random.poisson(self.__lam)

        Event(delay, "pkggen", {
            "rooter":  self.__rooter,
            "pkg": Package(1, "heja"),
            "host": self
        })
