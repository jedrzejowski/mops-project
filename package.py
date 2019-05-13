class Package:
    def __init__(self, header, content):
        """

        :param header:
        :param content:
        :type header: int
        :type content: str
        """
        self.__header = header
        self.__content = content

    def getHeader(self):
        """

        :return:
        :rtype: int
        """
        return self.__header

    def getContent(self):
        """

        :return:
        :rtype: str
        """
        return self.__content
