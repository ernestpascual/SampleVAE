import socket, struct, threading, time
import datetime
import numpy as np
import socket
# for osc
import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client
#for osc server
from pythonosc import dispatcher
from pythonosc import osc_server


LOCAL_HOST_ADDR="127.0.0.1"
LOCAL_OSC_PORT=8787



class Receiver(threading.Thread):
    def __init__(self):
        self.data = 0
        self.wav_name = "generate.wav"
        self.var = 0.1 #@param 0.0~20.0
        threading.Thread.__init__(self)

    def setConnection(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip",default=LOCAL_HOST_ADDR, help="The ip to listen on")
        parser.add_argument("--port",type=int, default=LOCAL_OSC_PORT, help="The port to listen on")
        args = parser.parse_args()        
        self.dispatcher = dispatcher.Dispatcher()

        self.dispatcher.map("/data", self.recieve)
        self.dispatcher.map("/name", self.recieveFileName)
        self.dispatcher.map("/var", self.recieveVar)

        server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), self.dispatcher)
        print("Serving on {}".format(server.server_address))
        server.serve_forever()

    def run(self):
        self.setConnection()
        
    def recieve(self,addr,data):
        print("recieved")
        print(addr)
        print(data)
        self.data = data

    def getRawData(self):
        v = self.data
        self.data = 0
        return v
    
    def recieveFileName(self,addr,name):
        print("recieved file name")
        self.wav_name = name
        print(name)
    
    def getName(self):
        return self.wav_name

    def recieveVar(self,addr,var):
        print("changed variation")
        self.var = round(var,1)
        print(self.var)
    
    def getVar(self):
        return self.var







