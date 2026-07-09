from datetime import datetime

from sqlmodel import Field, SQLModel


class Url(SQLModel, table=True):
    short_url: str = Field(primary_key=True)
    long_url: str
    created_at: datetime = Field(default=datetime.now())
    click_count: int = 0


class UrlCreate(SQLModel):
    long_url: str


class UrlPublic(SQLModel):
    short_url: str
    long_url: str
    created_at: datetime
    click_count: int = 0
