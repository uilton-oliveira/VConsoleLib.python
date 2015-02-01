from channel import Channel

__author__ = 'DarkSupremo'

from binary import BinaryStream


class PacketCHAN:
    def __init__(self, stream, channels):
        """
        @type stream: BinaryStream
        """
        self.length = stream.readInt16()
        for index in range(self.length):
            channel = Channel()
            channel.id = stream.readInt32()
            channel.unknown1 = stream.readInt32()
            channel.unknown2 = stream.readInt32()
            channel.verbosity_default = stream.readInt32()
            channel.verbosity_current = stream.readInt32()
            channel.RGBA_Override = stream.readInt32()
            channel.name = stream.readBytesNullTerminated(34)
            channels.append(channel)

    def channelById(self, channel_id, channels):
        for channel in channels:
            if channel.id == channel_id:
                return channel.name
        return 'Unknow: ' + str(channel_id)