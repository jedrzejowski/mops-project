import time

from rooter import Rooter
from host import Host
from event import Event

# Definicje Rooterów
r1 = Rooter("R1")
r2 = Rooter("R2")
r3 = Rooter("R3")

# Definicja Hostów
h1 = Host("H1", r1)
h2 = Host("H2")

# definicja połączeń
r1.addPort("a", r2)
r2.addPort("a", r3)
r3.addPort("a", h2)


def rooter1Rooting(pkg):
    r1.getPort("a").putPkg(pkg)
    return


def rooter2Rooting(pkg):
    r2.getPort("a").putPkg(pkg)
    return


def rooter3Rooting(pkg):
    r3.getPort("a").putPkg(pkg)
    return


r1.setRooting(rooter1Rooting)
r2.setRooting(rooter2Rooting)
r3.setRooting(rooter3Rooting)

# Wygenerowanie pakietów


while True:
    print("step")

    # Obsługa zdarzeń

    event = Event.popEvent()

    if event is None:
        time.sleep(2)
        continue

    print(event.name + " " + str(event.when))

    if event.name == "arrival":
        # {rooter, pkg}
        params = event.params

        rooter = params["rooter"]
        pkg = params["pkg"]

        rooter.acceptPkg(pkg)

        pass

    if event.name == "serviced":
        # {port}
        params = event.params

        port = params["port"]
        pkg = port.popPkg()
        rooter = port.getTargetRooter()

        Event(100, "arrival", {
            "rooter": rooter,
            "pkg": pkg
        })

        if port.hasPkg():
            port.makeService()

    if event.name == "pkggen":
        # {rooter, pkg}
        params = event.params

        rooter = params["rooter"]
        pkg = params["pkg"]
        host = params["host"]

        Event(100, "arrival", {
            "rooter": rooter,
            "pkg": pkg
        })

        host.genPkg()

