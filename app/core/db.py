from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import create_engine
from sqlmodel.main import SQLModel

from app.core.config import settings

# trying async
engine = create_async_engine(str(settings.POSTGRES_URL))
