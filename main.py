from vconsole2_lib import VConsole2Lib

__author__ = 'DarkSupremo'


def on_disconnected(vconsole):
    print "Disconnected, trying reconnect..."
    while not vconsole.connect():
        pass
    print "Connected..."


def main():
    vconsole = VConsole2Lib()
    vconsole.log_to_file = "D:/vconsole.txt"
    vconsole.on_disconnected = on_disconnected

    print "Trying connect..."
    while not vconsole.connect():
        pass
    print "Connected..."


if __name__ == "__main__":
    main()