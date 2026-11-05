from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# load_dotenv()


class Base(DeclarativeBase):
    pass


DB_RL = settings.DATABASE_URL.get_secret_value()


if DB_RL:

    engine = create_engine(DB_RL)

    SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
