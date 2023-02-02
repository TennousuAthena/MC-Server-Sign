from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse, Response
from libs.mcserver import Mcserver
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("doc/index.html")


@app.get("/server/{host}")
@app.get("/server/{host}:{port}")
@app.get("/i/{d}")
async def get_img(host: str = 'qcminecraft.com', port: int = 25565, srv: bool = False, d=False):
    if d:
        server = Mcserver('qcminecraft.com', srv=True)
    else:
        server = Mcserver(host, port, srv)
    img = server.get_img().getvalue()
    return Response(img, media_type="image/png")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
