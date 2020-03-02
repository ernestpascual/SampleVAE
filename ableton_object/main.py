from reciever import *
from samplevae import *
import os, signal, sys


signal.signal(signal.SIGINT, signal.SIG_DFL)


class App:
    def __init__(self,reciever,samplevae):
        self.reciever = reciever
        self.reciever.start()
        self.samplevae = samplevae

    def run(self):
        while True:
            time.sleep(0.02)
            rawdata = self.reciever.getRawData()
            path = self.reciever.getName()
            var = self.reciever.getVar()
            self.samplevae.update(rawdata,path,var)


def main():
    reciver = Receiver()
    samplevae = SampleVAE()
    app = App(reciver,samplevae)
    app.run()

if __name__ == "__main__":
    main()
