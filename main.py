from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from starlette.requests import Request
from controller import ping_router, power_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ping_router, prefix="/ping")
app.include_router(power_router, prefix="/system/power")

# remove json error response for all http status code
@app.exception_handler(400)
@app.exception_handler(401)
@app.exception_handler(403)
@app.exception_handler(404)
@app.exception_handler(405)
@app.exception_handler(406)
@app.exception_handler(409)
@app.exception_handler(415)
@app.exception_handler(422)
@app.exception_handler(500)
@app.exception_handler(501)
@app.exception_handler(502)
@app.exception_handler(503)
@app.exception_handler(504)
@app.exception_handler(505)
@app.exception_handler(506)
@app.exception_handler(507)
@app.exception_handler(508)
async def http_exception_handler(request: Request, exc: HTTPException):
    return Response(content="", status_code=exc.status_code)