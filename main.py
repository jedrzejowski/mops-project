import signal
import sys
import numpy as numpy
from mm1 import MM1

lam = 25
mi = 25
queueSize = 25

r1 = MM1(queueSize, mi)
r2 = MM1(queueSize, mi)
r3 = MM1(queueSize, mi)


def genPkg():
    r1.newArrival(numpy.random.poisson(lam))


r1.onArrival(lambda event: genPkg())
r1.onDrop(lambda event: genPkg())
r1.onService(lambda event: r2.newArrival(0))
r2.onService(lambda event: r3.newArrival(0))


def findNextMM1():
    t1 = r1.eventList.nextTime()
    t2 = r2.eventList.nextTime()
    t3 = r3.eventList.nextTime()

    time = min(t1, t2, t3)

    if time == t1:
        return r1
    if time == t2:
        return r2
    if time == t3:
        return r3


def log():
    print(f"r1({r1.pkgInQ}), r2({r2.pkgInQ}), r3({r3.pkgInQ})")


def signal_handler(sig, frame):

    print("Dane:")
    print(f"    λ               = {lam}")
    print(f"    µ               = {mi}")
    print(f"    queueSize       = {queueSize}")
    print("")
    print("Wyniki teoretyczne:")
    print(f"    servicePrec     = {lam/mi*100:14.1f} [%]")
    print("")
    print("Wyniki symulacji:")
    print("r1:")
    r1.printStatus()
    print("r2:")
    r2.printStatus()
    print("r3:")
    r3.printStatus()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

genPkg()
while True:
    rooter = findNextMM1()
    rooter.step2next()
    # log()

