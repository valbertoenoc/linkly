from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import create_engine
from sqlmodel.main import SQLModel

from config import settings

# engine = create_engine(str(settings.POSTGRES_URL))
# SQLModel.metadata.create_all(engine)

# trying async
engine = create_async_engine(str(settings.POSTGRES_URL))

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)
