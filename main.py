from vconsole2_lib import VConsole2Lib

__author__ = 'DarkSupremo'


def my_on_disconnected(vconsole):
    """
    :param vconsole: VConsole2Lib
    """
    print "Disconnected, trying reconnect..."
    while not vconsole.connect():
        pass
    print "Connected..."


def my_on_adon_received(vconsole, name):
    """
    :param vconsole: VConsole2Lib
    :param name: str
    """
    pass


def my_on_cvars_loaded(vconsole, cvars):
    """
    @param vconsole: VConsole2Lib
    @param cvars: list
    """
    print 'cvars loaded'


def my_on_prnt_received(vconsole, channel_name, msg):
    """
    :param vconsole: VConsole2Lib
    :param channel_name: str
    :param msg: str
    """
    pass


def main():
    vconsole = VConsole2Lib()
    vconsole.log_to_file = "D:/vconsole.txt"
    vconsole.log_to_screen = True
    vconsole.on_disconnected = my_on_disconnected
    vconsole.on_adon_received = my_on_adon_received
    vconsole.on_cvars_loaded = my_on_cvars_loaded
    vconsole.on_prnt_received = my_on_prnt_received

    print "Trying connect..."
    while not vconsole.connect():
        pass
    print "Connected..."


if __name__ == "__main__":
    main()