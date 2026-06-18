from datetime import datetime, timezone

from fastapi import FastAPI, requests, status
from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from starlette.status import HTTP_404_NOT_FOUND

from utils import b62_encode


class Settings(BaseSettings):
    base_url: str = "http://localhost:8000"


settings = Settings()


app = FastAPI()

urls: dict[str, dict[str, int | str | datetime]] = {
    "0": {
        "id": 0,
        "short_url": "http://localhost:8000/0",
        "long_url": "https://www.google.com",
        "created_at": datetime.now(),
        "click_count": 0,
    }
}


class UrlCreate(BaseModel):
    long_url: str


class UrlPublic(BaseModel):
    id: int
    short_url: str
    long_url: str
    created_at: datetime
    click_count: int = 0


@app.post("/shorten", response_model=UrlPublic)
async def shorten(url: UrlCreate):
    id = len(urls)
    short_code = b62_encode(id)
    short_url = f"{settings.base_url}/{short_code}"

    new_url = {
        "id": id,
        "click_count": 0,
        "created_at": datetime.now(timezone.utc),
        "long_url": url.long_url,
        "short_url": short_code,
    }

    urls[short_code] = new_url

    return UrlPublic(
        id=new_url["id"],
        click_count=new_url["click_count"],
        created_at=new_url["created_at"],
        long_url=new_url["long_url"],
        short_url=short_url,
    )


@app.get("/{short_code}")
async def redirect(short_code: str):
    print("short code", short_code)
    url = urls.get(short_code, "")
    if not url:
        return Response(status_code=HTTP_404_NOT_FOUND)

    long_url = url.get("long_url", "")
    print(long_url)
    return RedirectResponse(url=long_url, status_code=status.HTTP_302_FOUND)
