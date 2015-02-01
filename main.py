from libs.vconsole2_lib import VConsole2Lib

__author__ = 'DarkSupremo'


def my_on_disconnected(vconsole):
    """
    :param vconsole: VConsole2Lib
    """
    vconsole.log("Disconnected, trying reconnect...")
    while not vconsole.connect():
        pass
    vconsole.log("Connected...")


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
    vconsole.log('cvars loaded')


def my_on_prnt_received(vconsole, channel_name, msg):
    """
    :param vconsole: VConsole2Lib
    :param channel_name: str
    :param msg: str
    """
    pass


def main():
    vconsole = VConsole2Lib()
    vconsole.log_to_file = "D:/vconsole.htm"
    vconsole.html_output = True
    vconsole.log_to_screen = True
    vconsole.channels_custom_color = {'VConComm': '009900', 'VScript': '3333CC'}
    #vconsole.ignore_channels = ['Scaleform', 'ScaleformScript']
    vconsole.on_disconnected = my_on_disconnected
    vconsole.on_adon_received = my_on_adon_received
    vconsole.on_cvars_loaded = my_on_cvars_loaded
    vconsole.on_prnt_received = my_on_prnt_received

    vconsole.log("Trying connect...")
    while not vconsole.connect():
        pass
    vconsole.log("Connected...")


if __name__ == "__main__":
    main()