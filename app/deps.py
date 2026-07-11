from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.db import engine


# def get_db() -> Generator[Session]:
#     with Session(engine) as session:
#         yield session

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

SessionDeps = Annotated[AsyncSession, Depends(get_db)]
