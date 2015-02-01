__author__ = 'DarkSupremo'

import struct

class BinaryStream:
    def __init__(self, socket):
        self.socket = socket
        self.pos = 0
        self.length = 0
        self.msg_type = None
        self.version = None
        self.handle = None

    def load_packet_info(self):
        self.msg_type = self.readBytes(4)  # size = 4
        self.version = self.readInt32()  # size = 4
        self.length = self.readInt16()  # size = 2
        self.handle = self.readInt16()  # size = 2

    def readByte(self):
        self.pos += 1
        return self.socket.recv(1)

    def readBytes(self, length):
        self.pos += length
        return self.socket.recv(length)

    def readBytesNullTerminated(self, length):
        self.pos += length
        return self.socket.recv(length).split(b'\0', 1)[0]


    def readAllBytes(self):
        return self.socket.recv(self.length - self.pos)

    def readChar(self):
        return self.unpack('b')

    def readUChar(self):
        return self.unpack('B')

    def readBool(self):
        return self.unpack('?')

    def readInt16(self):
        return self.unpack('!h', 2)

    def readUInt16(self):
        return self.unpack('!H', 2)

    def readInt32(self):
        return self.unpack('!i', 4)

    def readInt32Little(self):
        return self.unpack('i', 4)

    def readUInt32(self):
        return self.unpack('!I', 4)

    def readUInt32Little(self):
        return self.unpack('I', 4)

    def readInt64(self):
        return self.unpack('!q', 8)

    def readUInt64(self):
        return self.unpack('!Q', 8)

    def readFloat(self):
        return self.unpack('!f', 4)

    def readDouble(self):
        return self.unpack('!d', 8)

    def readString(self):
        length = self.readUInt16()
        return self.unpack(str(length) + 's', length)

    # def writeBytes(self, value):
    #     self.base_stream.write(value)
    #
    # def writeChar(self, value):
    #     self.pack('c', value)
    #
    # def writeUChar(self, value):
    #     self.pack('C', value)
    #
    # def writeBool(self, value):
    #     self.pack('?', value)
    #
    # def writeInt16(self, value):
    #     self.pack('h', value)
    #
    # def writeUInt16(self, value):
    #     self.pack('H', value)
    #
    # def writeInt32(self, value):
    #     self.pack('i', value)
    #
    # def writeUInt32(self, value):
    #     self.pack('I', value)
    #
    # def writeInt64(self, value):
    #     self.pack('q', value)
    #
    # def writeUInt64(self, value):
    #     self.pack('Q', value)
    #
    # def writeFloat(self, value):
    #     self.pack('f', value)
    #
    # def writeDouble(self, value):
    #     self.pack('d', value)
    #
    # def writeString(self, value):
    #     length = len(value)
    #     self.writeUInt16(length)
    #     self.pack(str(length) + 's', value)

    #def pack(self, fmt, data):
    #    return self.writeBytes(pack(fmt, data))

    def unpack(self, fmt, length = 1):
        self.pos += length
        return struct.unpack(fmt, self.socket.recv(length))[0]