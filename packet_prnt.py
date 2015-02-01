__author__ = 'DarkSupremo'


class PacketPRNT:
    def __init__(self, stream):
        self.stream = stream

        self.channelID = stream.readInt32()
        self.unknow = stream.readBytes(24)
        self.msg = stream.readAllBytes()