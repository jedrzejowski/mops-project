class Package:
    def __init__(self, header, content):
        self.__header = header
        self.__content = content

    def getHeader(self):
        return self.__header

    def getContent(self):
        return self.__content
