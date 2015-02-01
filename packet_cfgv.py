__author__ = 'Uilton'

from binary import BinaryStream


class PacketCFGV:
    def __init__(self, stream):
        """
        @type stream: BinaryStream
        """
        self.stream = stream

        self.unknow = stream.readAllBytes()  # 129 bytes

    def __repr__(self):
        return self.unknow
