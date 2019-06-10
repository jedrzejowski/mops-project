from old.event import Event


class Port:
    def __init__(self, name, targetRooter):
        self.__name = name
        self.__pkgs = []
        self.__targetRooter = targetRooter

    def __str__(self):
        l = len(self.__pkgs)
        return f"Port(name={self.__name}, len={l})"

    def getName(self):
        return self.__name

    def getTargetRooter(self):
        """
        :return:
        :rtype: Rooter
        """
        return self.__targetRooter

    def hasPkg(self):
        """
        :return:
        :rtype: bool
        """
        return len(self.__pkgs) > 0

    def popPkg(self):
        """
        :return:
        :rtype: Package
        """
        return self.__pkgs.pop(0)

    def putPkg(self, pkg):
        """
        :param pkg:
        :type pkg: Package
        :return:
        """

        makeServiceEvent = False
        if len(self.__pkgs) == 0:
            makeServiceEvent = True

        self.__pkgs.append(pkg)

        if makeServiceEvent:
            self.makeService()

    def makeService(self):
        Event(100, "serviced", {
            "port": self
        })
