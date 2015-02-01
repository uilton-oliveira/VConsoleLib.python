__author__ = 'DarkSupremo'

from libs.binary import BinaryStream


class PacketADON:
    def __init__(self, stream):
        """
        @type stream: BinaryStream
        """
        self.stream = stream

        self.unknown = stream.readInt16()
        self.length = stream.readInt16()
        self.name = str(stream.readAllBytes())  # same as stream.readBytes(self.length)
