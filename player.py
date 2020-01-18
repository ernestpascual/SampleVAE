#python3
import socket, struct, threading, time
import datetime
# import pygame.mixer

from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

NONE=0
NEXT=1
PREV=2
PLAY=3
STOP=4
DOUBLE_TAP=10


def utcnow():
    return round(datetime.datetime.utcnow().timestamp() * 1000)


class Osc:
    def __init__(self, pd_host_addr, pd_osc_port):
        self.client = udp_client.UDPClient(pd_host_addr, pd_osc_port)

    def send(self, addr, v1 = None, v2 = None, v3 = None, v4 = None):
        msg = osc_message_builder.OscMessageBuilder(address=addr)
        for v in [v1,v2,v3,v4]:
            if v is not None:
                msg.add_arg(v)
        msg = msg.build()
        self.client.send(msg)

    def send_list(self, addr, lst):
        msg = osc_message_builder.OscMessageBuilder(address=addr)
        for l in lst:
            msg.add_arg(l)
        msg = msg.build()
        self.client.send(msg)


class Player:
    def __init__(self, pd_host_addr, pd_osc_port):
        self.osc = Osc(pd_host_addr, pd_osc_port)
        self.lock = threading.Lock()  

    
    def playSampleVAE(self):
        with self.lock:
            self.osc.send("/generate")
    
    def playSampleVAE_Snare(self):
        with self.lock:
            self.osc.send("/snare")










