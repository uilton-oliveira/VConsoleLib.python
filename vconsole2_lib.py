from packet_prnt import PacketPRNT
from packet_ainf import PacketAINF
from packet_adon import PacketADON
from packet_chan import PacketCHAN
from packet_cvar import PacketCVAR
from packet_cfgv import PacketCFGV

import time

__author__ = 'DarkSupremo'

import socket
from binary import BinaryStream
from threading import Thread


class VConsole2Lib:
    def __init__(self):
        self.stream = None
        self.channels = list()
        self.cvars = list()
        self.ainf = None
        self.adon_name = None
        self.on_prnt_received = None
        self.on_cvars_loaded = None
        self.on_adon_received = None
        self.on_disconnected = None
        self.ignore_channels = []
        self.client_socket = None
        self.log_to_screen = True
        self.log_to_file = None

    def connect(self, ip='127.0.0.1', port=29000):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))

            thread = Thread(target=self.__listen)
            thread.start()
            return True
        except:
            return False

    def log(self, text):
        if self.log_to_file:
            with open(self.log_to_file, "a") as myfile:
                myfile.write("[%s] %s" % (time.strftime("%H:%M:%S"), text))
        if self.log_to_screen:
            print "[%s] %s" % (time.strftime("%H:%M:%S"), text),

    def __listen(self):

        cvars_loaded = False
        channel = None

        try:
            while 1:
                self.stream = BinaryStream(self.client_socket)
                self.stream.load_packet_info()

                if self.stream.msg_type == 'PRNT':
                    prnt = PacketPRNT(self.stream)
                    this_channel = channel.channelById(prnt.channelID, self.channels)
                    if this_channel not in self.ignore_channels:
                        self.log("PRNT (%s): %s" % (this_channel, prnt.msg))
                        if self.on_prnt_received:
                            self.on_prnt_received(self, this_channel, prnt.msg)

                elif self.stream.msg_type == 'AINF':
                    self.ainf = PacketAINF(self.stream)
                elif self.stream.msg_type == 'ADON':
                    adon = PacketADON(self.stream)
                    self.adon_name = adon.name
                    self.log("ADON: %s \n" % (self.adon_name))
                    if self.on_adon_received:
                        self.on_adon_received(self, self.adon_name)
                elif self.stream.msg_type == 'CHAN':
                    channel = PacketCHAN(self.stream, self.channels)
                elif self.stream.msg_type == 'CVAR':
                    PacketCVAR(self.stream, self.cvars)
                elif self.stream.msg_type == 'CFGV':
                    PacketCFGV(self.stream)  # unknow, does nothing.
                    # when cfgv is called, cvars is already loaded.
                    if not cvars_loaded and self.on_cvars_loaded:
                        cvars_loaded = True
                        self.on_cvars_loaded(self, self.cvars)
                else:
                    self.stream.readAllBytes()

        except socket.error as error:
            if self.on_disconnected:
                self.on_disconnected(self)
