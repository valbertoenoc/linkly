from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session

from db import engine


def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDeps = Annotated[Session, Depends(get_db)]
