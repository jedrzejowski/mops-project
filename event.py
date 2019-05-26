import math

events = []
time = 0


class Event:
    def __init__(self, delay, name, params):
        global events
        self.when = delay + time
        self.name = name
        self.params = params

        global events
        events.append(self)

    @staticmethod
    def popEvent():
        """
        :return:
        :rtype: Event
        """

        global time
        global events

        target = None
        when = math.inf

        if len(events) == 0:
            return None

        # Znalezienie najwcześniejszego eventu
        for event in events:
            if event.when < when:
                target = event
                when = event.when

        events.remove(target)
        time = when

        return target
