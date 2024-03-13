
# check if is local ip
from fastapi import Request
import socket
import os

def is_local_ip(request: Request):
    # return request.client.host == socket.gethostbyname(socket.gethostname())
    return request.client.host in [socket.gethostbyname(socket.gethostname())]

def get_os():
    return os.name