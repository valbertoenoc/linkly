from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, Response

from crud import create_url, get_url
from deps import SessionDeps
from models import UrlCreate, UrlPublic

app = FastAPI()


@app.post("/shorten", response_model=UrlPublic)
async def shorten(session: SessionDeps, url: UrlCreate):
    new_url = create_url(session=session, url_create=url)

    return UrlPublic(
        click_count=new_url.click_count,
        created_at=new_url.created_at,
        long_url=new_url.long_url,
        short_url=new_url.short_url,
    )


@app.get("/{short_code}")
async def redirect(session: SessionDeps, short_url: str):
    url = get_url(session=session, short_url=short_url)
    if not url:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return RedirectResponse(url=url.long_url, status_code=status.HTTP_302_FOUND)
