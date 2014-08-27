#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SocketServer
import socket
import sys


class MyUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data


def start_server():
    HOST, PORT = '0.0.0.0', 50007
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()


def stop_remote(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto("OK", (ip, 50008))

if __name__ == "__main__":

    isStartServer = 1
    if len(sys.argv) > 1:
        isStartServer = 0

    if isStartServer:
        start_server()
    else:
        stop_remote(sys.argv[1])


