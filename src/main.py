from flask import Flask
from waitress import serve
import logging
import easy_scpi as scpi
import socket
import time

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    s = socket.socket()
    s.connect(("10.3.20.12", 5025))
    s.settimeout(3)
    logging.warning("init ok")

    s.send(str.encode("SYST:LOCK ON\n"))
    s.send(str.encode("SOUR:CURR 1A\n"))
    s.send(str.encode("SOUR:VOLT 1V\n"))
    s.send(str.encode("OUTP ON\n"))
    s.send(str.encode("*IDN?\n"))
    print(s.recv(2048))
    try:
        while True:
            s.send(str.encode("MEAS:CURR?\n"))
            s.send(str.encode("MEAS:VOLT?\n"))
            print(s.recv(2048))
            time.sleep(1)
    except KeyboardInterrupt:
        s.send(str.encode("SOUR:CURR 0A\n"))
        s.send(str.encode("SOUR:VOLT 0V\n"))
        s.send(str.encode("OUTP OFF\n"))
        print("PS stopped")
