#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import socket
import time
import select


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.bind(('0.0.0.0', 50008))

    start_tp = time.time()

    while True:

        DEST = '<broadcast>', 50007
        broadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcaster.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        broadcaster.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        infds, outfds, errfds = select.select([server], [broadcaster], [], 1)

        if len(infds):
            data = server.recv(1024)
            if data == 'OK':
                server.close()
                break

        if len(outfds):
            broadcaster.sendto("Hello-World", DEST)

        broadcaster.close()
        time.sleep(1)

        if time.time() - start_tp > 60*15:
            break

    sys.exit(0)

main()
