import os

from sqlmodel import create_engine
from sqlmodel.main import SQLModel

from config import settings

engine = create_engine(str(settings.POSTGRES_URL))

SQLModel.metadata.create_all(engine)
