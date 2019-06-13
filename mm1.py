import numpy as numpy
from eventlist import EventList


class MM1:
    def __init__(self, queueSize, mi):
        self.queueSize = queueSize
        self.mi = mi

        self.pkgInQ = 0
        self.eventList = EventList()
        self.__onArrival = None
        self.__onService = None
        self.__onDrop = None

        self.statPkgArrives = 0
        self.statPkgArrived = 0
        self.statPkgServiced = 0
        self.statPkgDropped = 0
        self.statServiceTime = 0

    def step2next(self):
        event = self.eventList.popEvent()

        if event is None:
            return

        if event.name == 'arrival':
            self.__arrival(event)
        if event.name == 'service':
            self.__service(event)

    def newArrival(self, delay):
        self.eventList.addEvent(delay, 'arrival')

    def __arrival(self, event):

        if self.pkgInQ == self.queueSize:
            self.statPkgDropped += 1
            if self.__onDrop is not None:
                self.__onDrop(event)
            return

        self.pkgInQ += 1
        self.statPkgArrived += 1

        if self.pkgInQ == 1:
            self.__genService()

        if self.__onArrival is not None:
            self.__onArrival(event)

    def __service(self, event):
        self.pkgInQ -= 1
        self.statPkgServiced += 1
        self.statServiceTime += event.delay

        if self.pkgInQ > 0:
            self.__genService()

        if self.__onService is not None:
            self.__onService(event)

    def __genService(self):
        self.eventList.addEvent(numpy.random.poisson(self.mi), 'service')

    def onArrival(self, func):
        self.__onArrival = func

    def onService(self, func):
        self.__onService = func

    def onDrop(self, func):
        self.__onDrop = func

    def printStatus(self):

        global time

        pkgPerSec = self.statPkgServiced / self.eventList.getTime() * 1000
        servicePrec = self.statServiceTime / self.eventList.getTime() * 100

        pkgDropRate = self.statPkgDropped / (self.statPkgArrived + self.statPkgDropped) * 100

        print(f"    statPkgArrived  = {self.statPkgArrived:14.0f}")
        print(f"    statPkgServiced = {self.statPkgServiced:14.0f}")
        print(f"    statPkgDropped  = {self.statPkgDropped:14.0f}")
        print(f"    pkgDropRate     = {pkgDropRate:14.1f} [%]")
        print(f"    pkgPerSec       = {pkgPerSec:14.3f} [s]")
        print(f"    servicePrec     = {servicePrec:14.1f} [%]")
