import os

from sqlmodel import Session, col, select

from models import Url, UrlCreate
from utils import b62_encode, generate_id

MACHINE_ID = os.getenv("MACHINE_ID", 1)
BASE_URL = os.getenv("BASE_URL")


def create_url(*, session: Session, url_create: UrlCreate) -> Url:
    sf_id: int | None = generate_id(int(MACHINE_ID))
    if not sf_id:
        raise

    short_code = b62_encode(sf_id)
    short_url = f"{BASE_URL}/{short_code}"

    new_url = Url(
        short_url=short_url,
        long_url=url_create.long_url,
    )

    session.add(new_url)
    session.commit()
    session.refresh(new_url)

    return new_url


def get_url(*, session: Session, short_url: str) -> Url:
    statement = select(Url).where(col(short_url) == short_url)
    url = session.exec(statement).one()

    return url
