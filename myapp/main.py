from urllib.parse import quote

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from lib.utils import isoformat_now

app = FastAPI()


@app.get("/")
async def root() -> JSONResponse:
    res_body = {"timestamp": isoformat_now()}
    response = JSONResponse(content=res_body, status_code=status.HTTP_200_OK)
    return response


@app.get("/{short_key}")
async def get_short_key(short_key: str) -> JSONResponse:
    q = f"{quote(short_key)}+{quote(isoformat_now())}"
    response = JSONResponse(
        content=None,
        status_code=status.HTTP_302_FOUND,
        headers={"Location": f"https://duckduckgo.com/?q={q}"},
    )
    return response
