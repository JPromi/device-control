from fastapi import APIRouter, Request
import socket
from dependency import is_local_ip

router = APIRouter()

@router.get("")
async def ping():
    return True

@router.get("/auth")
async def read_item(request: Request):
    return is_local_ip(request)

@router.get("/ip")
async def ip():
    return {
        "ip": socket.gethostbyname(socket.gethostname())
        }
