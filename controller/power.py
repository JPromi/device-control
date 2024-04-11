from fastapi import APIRouter, Request, HTTPException
from dependency import is_local_ip, get_os
import os

router = APIRouter()

@router.get("/shutdown")
async def shutdown(request: Request):
    if(is_local_ip(request)):
        if get_os() == "nt":
            os.system("shutdown /s /t 1")
            return {
                "system": "Windows",
                "status": "shutdown"
            }
        else:
            os.system("shutdown now")
            return {
                "system": "Linux",
                "status": "shutdown"
            }
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
@router.get("/reboot")
async def reboot(request: Request):
    if(is_local_ip(request)):
        if get_os() == "nt":
            os.system("shutdown /r /t 1")
            return {
                "system": "Windows",
                "status": "reboot"
            }
        else:
            os.system("reboot now")
            return {
                "system": "Linux",
                "status": "reboot"
            }
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")