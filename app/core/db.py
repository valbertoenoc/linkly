from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.main import SQLModel

from app.core.config import settings
from app.models.url import Url

# trying async
engine = create_async_engine(str(settings.POSTGRES_URL))

# remove this and use alembic instead
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
