from eventlist import EventList


class MM1:
    def __init__(self, queueSize):
        self.pkgInQ = 0
        self.eventList = EventList()
        self.__onArrival = None
        self.__onService = None
        self.__onDrop = None
        self.queueSize = queueSize

        self.statPkgArrived = 0
        self.statPkgServiced = 0
        self.statPkgDropped = 0
        self.statBytesSum = 0

    def step2next(self):
        event = self.eventList.popEvent()

        if event is None:
            return

        if event.name == 'arrival':
            self.__arrival(event)
        if event.name == 'service':
            self.__service(event)

    def newArrival(self, delay, size):
        self.eventList.addEvent(delay, 'arrival', {
            "size": size
        })

    def __arrival(self, event):

        if self.pkgInQ == self.queueSize:
            self.statPkgDropped += 1
            if self.__onDrop is not None:
                self.__onDrop(event)
            return

        self.pkgInQ += 1
        self.statPkgArrived += 1

        if self.pkgInQ == 1:
            self.eventList.addEvent(50, 'service', event.params)

        if self.__onArrival is not None:
            self.__onArrival(event)

    def __service(self, event):
        self.pkgInQ -= 1
        self.statPkgServiced += 1
        self.statBytesSum += event.params["size"]
        print(event.params["size"])

        if self.pkgInQ > 0:
            self.eventList.addEvent(50, 'service', event.params)

        if self.__onService is not None:
            self.__onService(event)

    def onArrival(self, func):
        self.__onArrival = func

    def onService(self, func):
        self.__onService = func

    def onDrop(self, func):
        self.__onDrop = func

    def printStatus(self):

        pkgPerSec = self.statPkgServiced / self.eventList.time * 1000
        # bytePerSec = self.statPkgServiced / self.eventList.time * 1000

        print(f"    statPkgArrived  = {self.statPkgArrived}")
        print(f"    statPkgServiced = {self.statPkgServiced}")
        print(f"    statPkgDropped  = {self.statPkgDropped}")
        print(f"    pkgPerSec       = {pkgPerSec:.3f}")
        # print(f"    bytePerSec      = {bytePerSec:.3f}")
