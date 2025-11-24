from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from .models import Base

engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)