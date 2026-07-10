
from sqlmodel import col, select
from sqlmodel.ext.asyncio.session import AsyncSession


from models import Url, UrlCreate
from utils import b62_encode, generate_id
from config import settings


async def create_url(*, session: AsyncSession, url_create: UrlCreate) -> Url:
    sf_id: int | None = generate_id()
    if not sf_id:
        raise

    short_code = b62_encode(sf_id)
    short_url = f"{settings.BASE_URL}/{short_code}"

    new_url = Url(
        short_url=short_url,
        long_url=url_create.long_url,
    )

    session.add(new_url)
    await session.commit()
    await session.refresh(new_url)

    return new_url


async def get_url(*, session: AsyncSession, short_url: str) -> Url | None:
    statement = select(Url).where(col(Url.short_url) == short_url)
    results = await session.exec(statement)
    url = results.first()

    return url
