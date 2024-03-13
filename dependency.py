
# check if is local ip
from fastapi import Request
import socket
import os

def is_local_ip(request: Request):
    if(request.client.host == socket.gethostbyname(socket.gethostname())):
        return True
    
    else:
        clientHostSplit = request.client.host.split(".")
        if(clientHostSplit[0] == "127" and clientHostSplit[1] == "0"):
            return True
        else:
            return False
        
    
    # return request.client.host in ["127.0.0.1", socket.gethostbyname(socket.gethostname())]

def get_os():
    return os.name