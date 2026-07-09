import os

from sqlmodel import create_engine

from config import settings

engine = create_engine(str(settings.POSTGRES_URL))
