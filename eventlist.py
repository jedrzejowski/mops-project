import math

from event import Event

time = 0

class EventList:
    def __init__(self):
        self.events = []

    def addEvent(self, delay, name):
        global time
        self.events.append(Event(time, delay, name))

    def popEvent(self):
        """
        :return:
        :rtype: Event
        """

        target = None
        when = math.inf

        if len(self.events) == 0:
            return None

        # Znalezienie najwcześniejszego eventu
        for event in self.events:
            if event.when < when:
                target = event
                when = event.when

        self.events.remove(target)

        global time
        time = when

        return target

    def nextTime(self):
        when = math.inf

        if len(self.events) == 0:
            return when

        # Znalezienie najwcześniejszego eventu
        for event in self.events:
            if event.when < when:
                when = event.when

        return when

    def getTime(self):
        global time
        return time
